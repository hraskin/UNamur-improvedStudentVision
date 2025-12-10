import cv2

class ZoomStabilizer:
    def __init__(self, alpha=0.2):
        """
        alpha : facteur de lissage (0.1 = très stable, 0.5 = plus réactif)
        """
        self.alpha = alpha
        self.prev_x = None
        self.prev_y = None

    def smooth(self, x, y):
        """Lissage exponentiel de la position (x, y)."""
        if self.prev_x is None or self.prev_y is None:
            self.prev_x, self.prev_y = x, y
        else:
            self.prev_x = self.alpha * x + (1 - self.alpha) * self.prev_x
            self.prev_y = self.alpha * y + (1 - self.alpha) * self.prev_y
        return int(self.prev_x), int(self.prev_y)


def zoom_on_interest_zone_stable(frame, position, stabilizer, zoom_ratio, zone_ratio):
    """
    Zoom stabilisé sur la zone d'intérêt autour du doigt, en gardant les proportions.

    - frame : image OpenCV
    - position : landmark MediaPipe (coordonnées normalisées 0–1)
    - stabilizer : instance de ZoomStabilizer (pour lisser la position)
    - zoom_ratio : intensité du zoom
    - zone_ratio : proportion visible de l’image (ex: 0.5 = moitié du cadre)
    """
    if position is None:
        return frame

    h, w, _ = frame.shape
    aspect_ratio = w / h

    cx = int(position.x * w)
    cy = int(position.y * h)

    # Lissage de la position
    cx, cy = stabilizer.smooth(cx, cy)

    zoomed_zone_ratio = max(0.05, zone_ratio / zoom_ratio)

    # Taille de la zone visible (proportion de l’image)
    visible_w = int(w * zoomed_zone_ratio)
    visible_h = int(visible_w / aspect_ratio)

    # Définition du rectangle centré sur la position lissée
    x1 = max(cx - visible_w // 2, 0)
    y1 = max(cy - visible_h // 2, 0)
    x2 = min(cx + visible_w // 2, w)
    y2 = min(cy + visible_h // 2, h)

    # Recadrage
    roi = frame[y1:y2, x1:x2]
    if roi.size == 0:
        return frame

    # Zoom (agrandit le ROI pour remplir tout le cadre)
    zoomed = cv2.resize(roi, (w, h), interpolation=cv2.INTER_LINEAR)
    return zoomed
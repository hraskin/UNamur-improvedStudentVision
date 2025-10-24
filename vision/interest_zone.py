import cv2

def zoom_on_interest_zone(frame, index_position, zone_ratio=0.6):
    """
    Zoom sur la zone d'intérêt autour du doigt, en gardant les proportions de l'image.

    - frame : image OpenCV
    - index_position : landmark MediaPipe (coordonnées normalisées 0–1)
    - zoom_ratio : intensité du zoom (1.2 = léger, 2.0 = fort)
    - zone_ratio : proportion du cadre à garder visible autour du doigt (0.4 = 40% de l’image)
    """
    if index_position is None:
        return frame

    h, w, _ = frame.shape
    aspect_ratio = w / h

    # Position du doigt en pixels
    cx = int(index_position.x * w)
    cy = int(index_position.y * h)

    # Taille de la zone d’intérêt (en proportion de l’image)
    visible_w = int(w * zone_ratio)
    visible_h = int(visible_w / aspect_ratio)

    # Coordonnées centrées autour du doigt
    x1 = max(cx - visible_w // 2, 0)
    y1 = max(cy - visible_h // 2, 0)
    x2 = min(cx + visible_w // 2, w)
    y2 = min(cy + visible_h // 2, h)

    # Ajustement si la zone sort du cadre (garde le ratio)
    if x2 - x1 < visible_w:
        diff = visible_w - (x2 - x1)
        x1 = max(x1 - diff // 2, 0)
        x2 = min(x2 + diff // 2, w)
    if y2 - y1 < visible_h:
        diff = visible_h - (y2 - y1)
        y1 = max(y1 - diff // 2, 0)
        y2 = min(y2 + diff // 2, h)

    # Recadrage de la zone
    roi = frame[y1:y2, x1:x2]

    if roi.size == 0:
        return frame

    # Zoom léger avec interpolation douce
    zoomed = cv2.resize(roi, (w, h), interpolation=cv2.INTER_LINEAR)

    return zoomed

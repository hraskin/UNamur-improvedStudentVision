import cv2

def center_interest_zone(frame, index_position, zone_size=100):
    """Dessine une zone d'intérêt centrée autour de la position du doigt (index)."""
    if index_position is None:
        return frame

    h, w, _ = frame.shape

    # Conversion des coordonnées normalisées (0-1) -> pixels
    x_px = int(index_position.x * w)
    y_px = int(index_position.y * h)

    # Calcul des coins du carré, en restant dans les limites de l'image
    half = zone_size // 2
    top_left = (max(x_px - half, 0), max(y_px - half, 0))
    bottom_right = (min(x_px + half, w), min(y_px + half, h))

    # Dessin du carré
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    # Optionnel : marquer le centre
    cv2.circle(frame, (x_px, y_px), 5, (0, 0, 255), -1)

    return frame
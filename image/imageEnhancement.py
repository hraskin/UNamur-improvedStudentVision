import cv2
import numpy as np

def enhance_board_light(frame, contrast=1.3, brightness=15, edge_intensity=0.5):
    """
    Améliore le tableau pour malvoyants :
    - Contraste et netteté
    - Bords noirs épais autour des écritures et formes
    """
    # Ajustement contraste + luminosité
    enhanced = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

    # Accentuation des détails
    blurred = cv2.GaussianBlur(enhanced, (0, 0), 1)
    sharp = cv2.addWeighted(enhanced, 1.8, blurred, -0.8, 0)

    # Détection des contours
    gray = cv2.cvtColor(sharp, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 20, 100)

    # Épaissir les contours pour créer de véritables bordures
    edges = cv2.dilate(edges, np.ones((5, 5), np.uint8), iterations=2)

    # Créer une image finale où les contours sont noirs
    output = sharp.copy()
    output[edges > 0] = (0, 0, 0)  # noir pur

    return output
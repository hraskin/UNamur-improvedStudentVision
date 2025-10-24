import cv2
import numpy as np

def enhance_board_light(frame, contrast=1.4, brightness=20, thickness=3):
    """
    Améliore le tableau pour malvoyants :
    - Contraste et netteté
    - Bords noirs épais autour des écritures et formes
    """
    # Ajustement contraste + luminosité
    # 1️⃣ Contraste + luminosité
    enhanced = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

    # 2️⃣ Accentuation légère (sharpen)
    blurred = cv2.GaussianBlur(enhanced, (0, 0), 1)
    sharp = cv2.addWeighted(enhanced, 1.8, blurred, -0.8, 0)

    # 3️⃣ Conversion en gris pour contour
    gray = cv2.cvtColor(sharp, cv2.COLOR_BGR2GRAY)

    # 4️⃣ Détection des contours avec Canny
    edges = cv2.Canny(gray, 20, 100)

    # 5️⃣ Trouver tous les contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 6️⃣ Dessiner les contours noirs épais
    output = sharp.copy()
    cv2.drawContours(output, contours, -1, (0, 0, 0), thickness)

    return output
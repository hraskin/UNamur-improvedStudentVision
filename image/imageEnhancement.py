import cv2
import numpy as np

def enhance_board_light(frame, contrast=1.3, brightness=15, contour_color=(0,0,0)):
    """
    Améliore la lisibilité pour malvoyants :
    - Contraste et luminosité modérés
    - Détection rapide de contours avec Sobel
    - Superposition des contours noirs sur l'image originale
    """
    # 1️⃣ Contraste et luminosité
    enhanced = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

    # 2️⃣ Niveaux de gris pour le filtre Sobel
    gray = cv2.cvtColor(enhanced, cv2.COLOR_BGR2GRAY)

    # 3️⃣ Sobel horizontal et vertical
    grad_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    magnitude = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    # 4️⃣ Seuillage pour isoler les contours
    _, edges = cv2.threshold(magnitude, 50, 255, cv2.THRESH_BINARY)

    # 5️⃣ Épaissir les contours
    edges = cv2.dilate(edges, np.ones((3,3), np.uint8), iterations=1)

    # 6️⃣ Superposer les contours sur l'image originale
    output = enhanced.copy()
    output[edges>0] = contour_color

    return output
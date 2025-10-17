import cv2
from tkinter import messagebox

# ======================
# CLASSE DE BASE
# ======================
class BaseCamera:
    def __init__(self):
        self.available = self.detect_cameras()
        self.cap = None

    def detect_cameras(self):
        """Détecte les caméras disponibles et retourne leurs index."""
        available = []
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available.append(i)
                cap.release()
        return available

    def open_camera(self, index):
        """Ouvre une caméra donnée."""
        self.cap = cv2.VideoCapture(index)
        if not self.cap.isOpened():
            raise Exception(f"Impossible d’ouvrir la caméra sur l’index {index}.")
        return self.cap

    def show_feed(self, title="Camera"):
        """Affiche le flux vidéo de la caméra ouverte."""
        if not self.cap:
            raise Exception("Aucune caméra ouverte.")

        messagebox.showinfo("Flux vidéo", f"Appuie sur 'q' pour quitter la fenêtre.")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            cv2.imshow(title, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
import cv2
from camera.camera import Camera
from tkinter import messagebox

# ======================
# CLASSES DÉRIVÉES
# ======================
class IPhoneCamera(Camera):
    """Classe spécifique pour les caméras iPhone."""

    def __init__(self):
        super().__init__()
        self.available = self.detect_cameras()

    def start(self):
        if not self.available:
            messagebox.showerror("Erreur", "Aucune caméra iPhone détectée.")
            return
        index = self.available[1]  # Exemple : premier index disponible
        self.open_camera(index)
        self.run("Camera iPhone")

    def detect_cameras(self):
        """Détecte les caméras disponibles et retourne leurs index."""
        available = []
        for i in range(2):
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
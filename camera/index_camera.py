import cv2
from tkinter import messagebox

from camera.camera import Camera


# ======================
# CLASSES DÉRIVÉES
# ======================
class IndexCamera(Camera):

    def __init__(self):
        super().__init__()
        self.available = self.detect_cameras()

    def start(self):
        if not self.available:
            messagebox.showerror("Erreur", "Aucune caméra par index détectée.")
            return
        index = self.available[0]  # Exemple : premier index disponible
        self.open_camera(index)
        self.run("Caméra Index")

    def detect_cameras(self):
        available = []
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available.append(i)
                cap.release()
        return available

    def open_camera(self, index):
        self.cap = cv2.VideoCapture(index)
        if not self.cap.isOpened():
            raise Exception(f"Impossible d’ouvrir la caméra sur l’index {index}.")
        return self.cap
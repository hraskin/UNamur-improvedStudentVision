import cv2
from tkinter import messagebox
from camera.BaseCamera import BaseCamera


# ======================
# CLASSE DE BASE
# ======================
class AndroidCamera(BaseCamera):
    """Classe spécifique pour les caméras Android."""
    def start(self):
        if not self.available:
            messagebox.showerror("Erreur", "Aucune caméra Android détectée.")
            return
        index = self.available[-1]  # Exemple : dernier index disponible
        self.open_camera(index)
        self.show_feed("Caméra Android")
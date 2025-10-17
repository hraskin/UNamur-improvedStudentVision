from camera.BaseCamera import BaseCamera
from tkinter import messagebox

# ======================
# CLASSES DÉRIVÉES
# ======================
class IPhoneCamera(BaseCamera):
    """Classe spécifique pour les caméras iPhone."""
    def start(self):
        if not self.available:
            messagebox.showerror("Erreur", "Aucune caméra iPhone détectée.")
            return
        index = self.available[1]  # Exemple : premier index disponible
        self.open_camera(index)
        self.show_feed("Caméra iPhone")
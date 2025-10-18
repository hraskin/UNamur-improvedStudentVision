import cv2
from camera.Camera import Camera


# ======================
# CLASSE DÉRIVÉES
# ======================
class AndroidCamera(Camera):
    """Classe spécifique pour les caméras Android."""
    def start(self):
        self.open_camera()
        self.show_feed("Camera Android")

    def open_camera(self):
        """Ouvre une caméra donnée."""
        url = "http://127.0.0.1:4747/video"
        self.cap = cv2.VideoCapture(url)
        if not self.cap.isOpened():
            raise Exception("Impossible d'accéder au flux vidéo.")
        return self.cap
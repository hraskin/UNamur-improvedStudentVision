import cv2
from camera.camera import Camera


# ======================
# CLASSE DÉRIVÉES
# ======================
class FlowCamera(Camera):
    def __init__(self, ip_address):
        super().__init__()
        self.ip_address = ip_address

    def start(self):
        self.open_camera()
        self.run("Caméra Flux Réseau")

    def open_camera(self):
        """Ouvre une caméra donnée."""
        url = f"http://{self.ip_address}:4747/video"
        self.cap = cv2.VideoCapture(url)
        if not self.cap.isOpened():
            raise Exception("Impossible d'accéder au flux vidéo.")
        return self.cap
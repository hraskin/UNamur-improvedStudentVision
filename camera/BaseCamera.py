import cv2
from tkinter import messagebox

# ======================
# CLASSE DE BASE
# ======================
class BaseCamera:
    def __init__(self):
        self.cap = None

    def show_feed(self, title="Camera"):
        """Affiche le flux vidéo de la caméra ouverte."""
        if not self.cap:
            raise Exception("Aucune caméra ouverte.")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            cv2.imshow(title, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
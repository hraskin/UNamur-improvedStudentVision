import cv2
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QImage

from camera.fps_tracker import FpsTracker
from camera.pipeline import Pipeline

class CameraWorker(QObject):
    frame_ready = Signal(QImage)

    def __init__(self, camera: str|int):
        super().__init__()
        self.running = False
        if isinstance(camera, int):
            self.cap = cv2.VideoCapture(camera)
        else:
            url = f"http://{camera}:4747/video"
            self.cap = cv2.VideoCapture(url)
        if not self.cap.isOpened():
            raise RuntimeError("Impossible d’ouvrir la caméra.")

    @Slot()
    def start(self):
        self.running = True
        fps_tracker = FpsTracker()
        pipeline = Pipeline()

        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break

            fps_tracker.start()
            frame = pipeline.execute(frame)
            fps_tracker.stop()

            fps_info = fps_tracker.get_info()
            cv2.putText(frame, fps_info, (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            qimg = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
            self.frame_ready.emit(qimg.copy())

        self.cap.release()

    @Slot()
    def stop(self):
        self.running = False

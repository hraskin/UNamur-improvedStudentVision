from datetime import datetime

from PySide6.QtCore import QObject, QThread, Signal
from camera.camera_worker import CameraWorker
from camera.camera_image_provider import CameraImageProvider

class CameraPresenter(QObject):
    frameUpdated = Signal()
    captureSuccessful = Signal()

    def __init__(self, engine):
        super().__init__()
        self._engine = engine
        self._provider = CameraImageProvider()
        self._engine.addImageProvider("camera", self._provider)
        self._last_image = None

    def launch(self, camera):
        self._worker = CameraWorker(camera)
        self._thread = QThread()
        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.start)
        self._worker.frame_ready.connect(self._on_frame_ready)
        self._worker.raw_frame_ready.connect(self._on_raw_frame_ready)
        self._thread.start()

    def stop(self):
        if hasattr(self, "_worker"):
            self._worker.stop()
        if hasattr(self, "_thread"):
            self._thread.quit()
            self._thread.wait()

    def want_capture_image(self):
        if self._last_image:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = f"capture_{timestamp}"

            success = self._last_image.save(f'{file_path}.jpg')
            if success:
                self.captureSuccessful.emit()
                return file_path
        return None

    def _on_frame_ready(self, qimg):
        self._provider.update_image(qimg)
        self.frameUpdated.emit()

    def _on_raw_frame_ready(self, qimg):
        self._last_image = qimg
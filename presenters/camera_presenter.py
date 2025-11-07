# camera_presenter.py
from PySide6.QtCore import QObject, QThread, Signal
from camera.camera_worker import CameraWorker
from camera.camera_image_provider import CameraImageProvider

class CameraPresenter(QObject):
    frameUpdated = Signal()  # 👈 exposé à QML

    def __init__(self, engine):
        super().__init__()
        self._engine = engine
        self._provider = CameraImageProvider()
        self._engine.addImageProvider("camera", self._provider)

    def launch(self, camera_type):
        self._worker = CameraWorker(camera_type)
        self._thread = QThread()
        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.start)
        self._worker.frame_ready.connect(self._on_frame_ready)
        self._thread.start()

    def _on_frame_ready(self, qimg):
        self._provider.update_image(qimg)
        self.frameUpdated.emit()

    def stop(self):
        if hasattr(self, "_worker"):
            self._worker.stop()
        if hasattr(self, "_thread"):
            self._thread.quit()
            self._thread.wait()

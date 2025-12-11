from threading import Lock

from PySide6.QtCore import QThread
from keywords_detection.keywords_listerner import KeywordsListener
from ocr.ocr_manager import OCRManager
from presenters.camera_presenter import CameraPresenter
from cv2_enumerate_cameras import enumerate_cameras
from tts.audio_manager import AudioManager
from workers.capture_process_worker import CaptureProcessWorker


class MainPresenter:
    def __init__(self, view):
        self._view = view
        self._engine = self._view.engine
        self._camera_presenter = None
        self._keyword_listener = KeywordsListener(on_wakeword_detected=self._handle_capture)
        self._ocr_manager = OCRManager()
        self._audio_manager = AudioManager()
        self._capture_lock = Lock()
        self._threads = []
        self._workers = []

        self._view.wantCamera.connect(self._handle_camera_type)
        self._view.startAnalysis.connect(self.launch_camera)
        self._view.wantReturnToMenu.connect(self.return_to_menu)
        self._view.wantCapture.connect(self._handle_capture)
        self._view.wantStopApplication.connect(self._stop_application)

        self._view.start()

    def launch_camera(self, camera : str|int):
        if self._camera_presenter:
            self._camera_presenter.stop()

        self._camera_presenter = CameraPresenter(self._engine)
        self._camera_presenter.launch(camera)

        self._camera_presenter.frameUpdated.connect(self._view.frameUpdated)
        self._camera_presenter.captureSuccessful.connect(self._view.capture_successful)

        self._view.show_view("camera")
        self._keyword_listener.start()

    def _handle_camera_type(self, camera_type):
        if camera_type == "index":
            cameras = list(dict.fromkeys(camera_info.name for camera_info in enumerate_cameras()))
            self._view.update_camera_list(cameras)
        elif camera_type == "flow":
            self._view.update_camera_list([])

    def return_to_menu(self):
        self._stop_camera()
        self._view.show_view("menu")

    def _stop_camera(self):
        self._keyword_listener.stop()
        if self._camera_presenter:
            self._camera_presenter.stop()
            self._camera_presenter = None

    def _handle_capture(self):
        if not self._camera_presenter:
            return

        thread = QThread()
        worker = CaptureProcessWorker(
            self._camera_presenter,
            self._ocr_manager,
            self._audio_manager,
            self._capture_lock
        )

        worker.moveToThread(thread)
        thread.started.connect(worker.run)

        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(lambda: self._cleanup(thread, worker))

        self._threads.append(thread)
        self._workers.append(worker)
        thread.start()

    def _cleanup(self, thread, worker):
        self._threads.remove(thread)
        self._workers.remove(worker)

    def _stop_application(self):
        for thread in self._threads:
            thread.quit()
            thread.wait()
        self._stop_camera()

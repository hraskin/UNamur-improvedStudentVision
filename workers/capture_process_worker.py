from PySide6.QtCore import QObject, Signal, Slot
from braille.braille import text_to_braille


class CaptureProcessWorker(QObject):
    finished = Signal()

    def __init__(self, camera, ocr, audio, lock):
        super().__init__()
        self._camera = camera
        self._ocr = ocr
        self._audio = audio
        self._lock = lock

    @Slot()
    def run(self):
        with self._lock:
            file_path = self._camera.want_capture_image()

        text = self._ocr.extract_text(file_path)
        text_to_braille(text)
        self._audio.play_audio(file_path, text)
        self.finished.emit()
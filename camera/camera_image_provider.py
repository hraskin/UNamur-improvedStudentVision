# camera_image_provider.py
from PySide6.QtQuick import QQuickImageProvider
from PySide6.QtGui import QImage
from PySide6.QtCore import QMutex, QMutexLocker

class CameraImageProvider(QQuickImageProvider):
    def __init__(self):
        super().__init__(QQuickImageProvider.Image)
        self._image = QImage()
        self._mutex = QMutex()

    def update_image(self, img: QImage):
        with QMutexLocker(self._mutex):
            self._image = img

    def requestImage(self, id, size, requestedSize):
        with QMutexLocker(self._mutex):
            if not self._image.isNull():
                return self._image
            return QImage()

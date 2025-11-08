from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
import os


class MainView(QObject):
    wantCamera = Signal(str)
    cameraListReady = Signal(list)
    wantReturnToMenu = Signal()
    startAnalysis = Signal(object)
    frameUpdated = Signal()

    def __init__(self):
        super().__init__()
        self._app = QApplication.instance()
        self._engine = QQmlApplicationEngine()
        self._main_window = None

    @property
    def engine(self):
        return self._engine

    def start(self):
        self._engine.load(os.path.join(os.path.dirname(__file__), "views", "main.qml"))
        self._main_window = self._engine.rootObjects()[-1]
        self._engine.rootContext().setContextProperty("backend", self)
        self._app.exec()

    @Slot()
    def stop_application(self):
        if hasattr(self, "_main_window"):
            self._main_window.destroy()

    @Slot(str)
    def want_camera(self, camera_type: str):
        self.wantCamera.emit(camera_type)

    @Slot()
    def return_to_menu(self):
        self.wantReturnToMenu.emit()

    @Slot(int)
    @Slot(str)
    def start_analysis(self, value):
        self.startAnalysis.emit(value)

    def update_camera_list(self, cameras):
        self.cameraListReady.emit(cameras)

    def show_view(self, view_name: str):
        if self._main_window:
            self._main_window.setProperty("currentView", view_name)

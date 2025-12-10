import os

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

from settings.settings_singleton import SettingsSingleton


class MainView(QObject):
    wantCamera = Signal(str)
    cameraListReady = Signal(list)
    wantReturnToMenu = Signal()
    wantCapture = Signal()
    wantStopApplication = Signal()
    startAnalysis = Signal(object)
    frameUpdated = Signal()
    captureSuccessfulSignal = Signal()

    def __init__(self):
        super().__init__()
        self._app = QApplication.instance()
        self._engine = QQmlApplicationEngine()
        self._main_window = None

    @property
    def engine(self):
        return self._engine

    def start(self):
        qml_path = os.path.join(os.path.dirname(__file__), "views", "main.qml")
        self._engine.rootContext().setContextProperty("backend", self)
        self._engine.load(qml_path)
        self._main_window = self._engine.rootObjects()[-1]

        shortcut = QShortcut(QKeySequence("Ctrl+S"), self._main_window)
        shortcut.activated.connect(self._want_capture)

        self._app.exec()

    def capture_successful(self):
        self.captureSuccessfulSignal.emit()

    def _want_capture(self):
        self.wantCapture.emit()

    @Slot()
    def stop_application(self):
        self.wantStopApplication.emit()
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

    @Slot(bool)
    def zoom_on(self, value: bool):
        SettingsSingleton.get_instance().set_zoom_on(value)

    @Slot(bool)
    def edge_on(self, value: bool):
        SettingsSingleton.get_instance().set_edge_on(value)

    @Slot(int)
    def set_zoom(self, zoom_level: int):
        SettingsSingleton.get_instance().set_zoom_level(zoom_level)

    @Slot(int, int)
    def zoom(self, x: int, y: int):
        SettingsSingleton.get_instance().update_zoom(x, y)
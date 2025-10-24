import os
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication


class MainView(QObject):
    wantIndexCamera = Signal()
    wantFlowCamera = Signal()

    def __init__(self):
        super().__init__()
        self._app = QApplication.instance()
        self._engine = QQmlApplicationEngine()
        self._main_window = None

    def start(self):
        self._engine.load(os.path.join(os.path.dirname(__file__), "views", "main.qml"))
        self._main_window = self._engine.rootObjects()[-1]

        self._engine.rootContext().setContextProperty("backend", self)
        self._app.exec()

    @Slot()
    def stop_application(self):
        if hasattr(self, "_main_window"):
            self._main_window.destroy()

    @Slot()
    def want_index_camera(self):
        self.wantIndexCamera.emit()

    @Slot()
    def want_flow_camera(self):
        self.wantFlowCamera.emit()

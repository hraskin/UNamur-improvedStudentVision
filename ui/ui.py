import os
from PySide6.QtCore import QObject
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication


class Ui(QObject):
    def __init__(self):
        super().__init__()
        self._app = QApplication.instance()
        self._engine = QQmlApplicationEngine()
        self._main_window = None

    def setup_ui(self):
        self._engine.load(os.path.join(os.path.dirname(__file__), "views", "main.qml"))
        self._main_window = self._engine.rootObjects()[-1]
        self._app.exec()
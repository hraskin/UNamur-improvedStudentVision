from PySide6.QtWidgets import QApplication
from presenters.main_presenter import MainPresenter
from ui.main_view import MainView

if __name__ == "__main__":
    q_app = QApplication()
    view = MainView()
    MainPresenter(view)


from PySide6.QtWidgets import QApplication
from presenters.main_presenter import MainPresenter
from ui.main_view import MainView
import cProfile
import pstats

def main():
    q_app = QApplication()
    view = MainView()
    MainPresenter(view)

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats(20)

from presenters.camera_presenter import CameraPresenter

class MainPresenter:
    def __init__(self, view):
        self._view = view
        self._engine = self._view.engine
        self._camera_presenter = None

        self._view.wantCamera.connect(self.launch_camera)
        self._view.wantReturnToMenu.connect(self.return_to_menu)

        self._view.start()

    def launch_camera(self, camera_type: str):
        if self._camera_presenter:
            self._camera_presenter.stop()

        self._camera_presenter = CameraPresenter(self._engine)
        self._camera_presenter.launch(camera_type)

        self._camera_presenter.frameUpdated.connect(self._view.frameUpdated)

        self._view.show_view("camera")

    def return_to_menu(self):
        self._stop_camera()
        self._view.show_view("menu")

    def _stop_camera(self):
        if self._camera_presenter:
            self._camera_presenter.stop()
            self._camera_presenter = None
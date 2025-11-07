from camera.camera_switch import launch_camera


class MainPresenter:
    def __init__(self, view):
        self._view = view

        self._view.wantIndexCamera.connect(self.launch_index_camera)
        self._view.wantFlowCamera.connect(self.launch_flow_camera)

        self._view.start()

    def close(self):
        self._view.close()

    def launch_index_camera(self):
        launch_camera("index")

    def launch_flow_camera(self):
        launch_camera("flow")

    def detect_index_cameras(self):
        from camera.index_camera import IndexCamera

        index_camera = IndexCamera()
        return index_camera.detect_cameras()

class SettingsSingleton(object):
    _instance = None
  
    def __init__(self):
        self.zoomOn = True
        self.edgeOn = True

    @staticmethod
    def get_instance():
        if SettingsSingleton._instance is None:
            SettingsSingleton._instance = SettingsSingleton()
        return SettingsSingleton._instance

    def get_zoom_on(self):
        return self.zoomOn

    def set_zoom_on(self, zoomOn):
        self.zoomOn = zoomOn

    def get_edge_on(self):
        return self.edgeOn

    def set_edge_on(self, edgeOn):
        self.edgeOn = edgeOn
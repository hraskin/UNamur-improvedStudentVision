class SettingsSingleton(object):
    _instance = None
  
    def __init__(self):
        self._zoom_on = True
        self._edge_on = True
        self._zoom_level = 1
        self._zoom_x = 0
        self._zoom_y = 0

    @staticmethod
    def get_instance():
        if SettingsSingleton._instance is None:
            SettingsSingleton._instance = SettingsSingleton()
        return SettingsSingleton._instance

    def get_zoom_on(self):
        return self._zoom_on

    def set_zoom_on(self, zoom_on):
        self._zoom_on = zoom_on

    def get_edge_on(self):
        return self._edge_on

    def set_edge_on(self, edge_on):
        self._edge_on = edge_on

    def get_zoom_level(self):
        return self._zoom_level
    
    def set_zoom_level(self, zoom_level):
        self._zoom_level = zoom_level
    
    def get_zoom_x(self):
        return self._zoom_x

    def get_zoom_y(self):
        return self._zoom_y

    def update_zoom(self, x, y):
        if self._zoom_x == 0:
            self._zoom_x = x
            self._zoom_y = y
        else:
            self._zoom_x = 0
            self._zoom_y = 0
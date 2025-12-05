class SettingsSingleton(object):
    _instance = None
  
    def __init__(self):
        self.zoomOn = True
        self.edgeOn = True
        self.zoomLevel = 0
        self.zoomX = 0
        self.zoomY = 0

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

    def get_zoomLevel(self):
        return self.zoomLevel
    
    def set_zoomLevel(self, zoomLevel):
        self.zoomLevel = zoomLevel
    
    def get_zoomX(self):
        return self.zoomX
    
    def set_zoomX(self, zoomX):
        self.zoomX = zoomX

    def get_zoomY(self):
        return self.zoomY
    
    def set_zoomY(self, zoomY):
        self.zoomY = zoomY

    def updateZoom(self, x, y, screen_width, screen_height):
        # dimension image: 640 * 480
        print(x, y, screen_width, screen_height)
        x = int(x*640/screen_width)
        y = int(y*480/screen_height)
        if self.zoomX == 0 and 0 < x < 640 and 0 < y < 480:
            self.zoomX = x
            self.zoomY = y
        else:
            self.zoomX = 0
            self.zoomY = 0
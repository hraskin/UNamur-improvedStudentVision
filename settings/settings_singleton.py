class SettingsSingleton(object):
    instance = None
  
    def __init__(self):
        self.zoomOn = True
        self.edgeOn = True

    def getInstance():
        if SettingsSingleton.instance == None:
            SettingsSingleton.instance = SettingsSingleton()
        return SettingsSingleton.instance

    def getZoomOn(self):
        return self.zoomOn

    def setZoomOn(self, zoomOn):
        self.zoomOn = zoomOn

    def getEdgeOn(self):
        return self.edgeOn

    def setEdgeOn(self, edgeOn):
        self.edgeOn = edgeOn
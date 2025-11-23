from camera.interest_zone import (ZoomStabilizer, zoom,
                                  zoom_on_interest_zone_stable)
from image.imageEnhancement import enhance_frame_edge, enhance_frame_light
from recognition.hand_recognition import HandRecognizer
from settings.settings_singleton import SettingsSingleton


class Pipeline:
    def __init__(self):
        self.recognizer = HandRecognizer()
        self.stabilizer = ZoomStabilizer(alpha=0.15)

    def execute(self, frame):
        self.recognizer.detect_async(frame)
        settings = SettingsSingleton.get_instance()
        if settings.get_zoomX() != 0:
            frame = zoom(frame, settings.get_zoomLevel(), settings.get_zoomX(), settings.get_zoomY())

        if settings.get_edge_on():
            frame = enhance_frame_light(frame, contrast=1.15, brightness=8)
            frame = enhance_frame_edge(frame)

        if self.recognizer.landmarks_to_draw and settings.get_zoom_on():
            index_position = self.recognizer.index_position
            self.recognizer.draw_landmarks(frame)
            frame = zoom_on_interest_zone_stable(
                frame, index_position, self.stabilizer,
                zoom_ratio=1.4, zone_ratio=0.55
            )

        return frame
from camera.interest_zone import (ZoomStabilizer, zoom_on_interest_zone_stable)
from image.imageEnhancement import enhance_frame_edge, enhance_frame_light
from recognition.hand_recognition import HandRecognizer
from settings.settings_singleton import SettingsSingleton
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmark


class Pipeline:
    def __init__(self):
        self.recognizer = HandRecognizer()
        self.stabilizer = ZoomStabilizer(alpha=0.15)

    def execute(self, frame):
        self.recognizer.detect_async(frame)
        settings = SettingsSingleton.get_instance()
        if settings.get_zoom_x() != 0:
            position = self._landmark_from_pixels(settings.get_zoom_x(), settings.get_zoom_y(), frame)
            frame = zoom_on_interest_zone_stable(
                frame,position, self.stabilizer,
                zoom_ratio=settings.get_zoom_level(), zone_ratio=0.55
            )

        elif self.recognizer.landmarks_to_draw and settings.get_zoom_on():
            index_position = self.recognizer.index_position
            self.recognizer.draw_landmarks(frame)
            frame = zoom_on_interest_zone_stable(
                frame, index_position, self.stabilizer,
                zoom_ratio=1.4, zone_ratio=0.55
            )

        if settings.get_edge_on():
            frame = enhance_frame_light(frame, contrast=1.15, brightness=8)
            frame = enhance_frame_edge(frame)

        return frame

    @staticmethod
    def _landmark_from_pixels(x_px, y_px, frame):
        h, w, _ = frame.shape
        lm = NormalizedLandmark()
        lm.x = x_px / w
        lm.y = y_px / h
        lm.z = 0.0
        return lm

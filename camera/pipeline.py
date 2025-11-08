from camera.interest_zone import ZoomStabilizer, zoom_on_interest_zone_stable
from image.imageEnhancement import enhance_frame_light, enhance_frame_edge
from recognition.hand_recognition import HandRecognizer

class Pipeline:
    def __init__(self):
        self.recognizer = HandRecognizer()
        self.stabilizer = ZoomStabilizer(alpha=0.15)

    def execute(self, frame):
        self.recognizer.detect_async(frame)

        frame = enhance_frame_light(frame, contrast=1.15, brightness=8)
        frame = enhance_frame_edge(frame)

        if self.recognizer.landmarks_to_draw:
            index_position = self.recognizer.index_position
            self.recognizer.draw_landmarks(frame)
            frame = zoom_on_interest_zone_stable(
                frame, index_position, self.stabilizer,
                zoom_ratio=1.4, zone_ratio=0.55
            )

        return frame
import cv2

from camera.fps_tracker import FpsTracker
from camera.pipeline import Pipeline

class Camera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise Exception("Impossible d’ouvrir la caméra.")

    def run(self, window_name="Camera"):
        fps_tracker = FpsTracker()
        pipeline = Pipeline()

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            fps_tracker.start()

            frame = pipeline.execute(frame)

            fps_tracker.stop()
            fps_info = fps_tracker.get_info()

            cv2.putText(frame, fps_info, (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            cv2.imshow(window_name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
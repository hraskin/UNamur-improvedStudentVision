import cv2
import time

from image.imageEnhancement import enhance_board_light
from camera.interest_zone import ZoomStabilizer, zoom_on_interest_zone_stable
from recognition.hand_recognition import HandRecognizer

class Camera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise Exception("Impossible d’ouvrir la caméra.")
        self.recognizer = HandRecognizer()
        self.stabilizer = ZoomStabilizer(alpha=0.15)  # petit alpha = mouvement plus doux

    def run(self, window_name="Camera"):
        prev_time = 0
        fps = 0
        latency_ms = 0

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # ⏱ Début mesure
            start_time = time.time()

            # Détection main
            self.recognizer.detect_async(frame)

            if self.recognizer.landmarks_to_draw:
                index_position = self.recognizer.index_position
                frame = enhance_board_light(frame, contrast=1.15, brightness=8)
                self.recognizer.draw_landmarks(frame)
                frame = zoom_on_interest_zone_stable(
                    frame, index_position, self.stabilizer,
                    zoom_ratio=1.4, zone_ratio=0.55
                )
            else:
                cv2.putText(frame, "Aucune main detectee", (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # ⏱ Fin mesure + calcul du FPS et latence
            end_time = time.time()
            dt = end_time - prev_time
            frame_time = (end_time - start_time) * 1000  # latence en ms
            latency_ms = 0.9 * latency_ms + 0.1 * frame_time
            if dt > 0:
                fps = 0.9 * fps + 0.1 * (1.0 / dt)
            prev_time = end_time

            # 🔹 Afficher FPS et latence
            text = f"FPS: {fps:.1f} | {latency_ms:.1f} ms/frame"
            cv2.putText(frame, text, (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            # 🔹 Affichage du flux
            cv2.imshow(window_name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
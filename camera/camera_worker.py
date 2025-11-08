import cv2
import time
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QImage
from image.imageEnhancement import enhance_board_light
from camera.interest_zone import ZoomStabilizer, zoom_on_interest_zone_stable
from recognition.hand_recognition import HandRecognizer

class CameraWorker(QObject):
    frame_ready = Signal(QImage)

    def __init__(self, camera_type="index"):
        super().__init__()
        self.running = False
        self.camera_type = camera_type
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("Impossible d’ouvrir la caméra.")
        self.recognizer = HandRecognizer()
        self.stabilizer = ZoomStabilizer(alpha=0.15) # petit alpha = mouvement plus doux

    @Slot()
    def start(self):
        prev_time = 0
        fps = 0
        latency_ms = 0
        self.running = True

        while self.running:
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
                cv2.putText(frame, "Aucune main détectée", (30, 60),
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

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            qimg = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
            self.frame_ready.emit(qimg.copy())

        self.cap.release()

    @Slot()
    def stop(self):
        self.running = False

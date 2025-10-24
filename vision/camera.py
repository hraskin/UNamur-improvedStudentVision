import cv2

from vision.interest_zone import center_interest_zone
from recognition.hand_recognition import HandRecognizer

class Camera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise Exception("Impossible d’ouvrir la caméra.")
        self.recognizer = HandRecognizer()

    def run(self, window_name="Camera"):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Envoyer la frame au recognizer
            self.recognizer.detect_async(frame)

            # Dessiner les résultats
            if self.recognizer.landmarks_to_draw:
                self.recognizer.draw_landmarks(frame)
                index_position = self.recognizer.index_position
                center_interest_zone(frame, index_position)

            else:
                cv2.putText(frame, "Aucune main detectee", (30, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow(window_name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
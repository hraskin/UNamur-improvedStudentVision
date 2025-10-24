import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL_PATH = "models/hand_landmarker.task"
VisionRunningMode = mp.tasks.vision.RunningMode

class HandRecognizer:
    def __init__(self, max_hands=1):
        self.landmarks_to_draw = []
        self.handedness_to_draw = []
        self.index_position = None

        # Configuration du modèle
        base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=max_hands,
            running_mode=VisionRunningMode.LIVE_STREAM,
            result_callback=self.on_result
        )
        self.detector = vision.HandLandmarker.create_from_options(options)

    def on_result(self, result, image, timestamp_ms):
        """Callback appelé par MediaPipe après traitement de chaque frame"""
        if result and result.hand_landmarks:
            self.landmarks_to_draw = [result.hand_landmarks[0]]
            self.handedness_to_draw = [result.handedness[0]]
            self.index_position = result.hand_landmarks[0][8] # Index of the index finger tip
        else:
            self.landmarks_to_draw = []
            self.handedness_to_draw = []

    def draw_landmarks(self, frame):
        """Dessine les landmarks directement avec OpenCV"""
        connections = [
            (0,1),(1,2),(2,3),(3,4),
            (0,5),(5,6),(6,7),(7,8),
            (0,9),(9,10),(10,11),(11,12),
            (0,13),(13,14),(14,15),(15,16),
            (0,17),(17,18),(18,19),(19,20)
        ]
        h, w, _ = frame.shape

        for idx, hand_landmarks in enumerate(self.landmarks_to_draw):
            points = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks]

            # Dessiner les points
            for x, y in points:
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            # Dessiner les connexions
            for start, end in connections:
                cv2.line(frame, points[start], points[end], (255, 0, 0), 2)

            # Afficher la main gauche/droite
            if idx < len(self.handedness_to_draw):
                hand_label = self.handedness_to_draw[idx][0].category_name
                cv2.putText(frame, hand_label, (points[0][0], points[0][1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (88, 205, 54), 2)

    def detect_async(self, frame):
        """Envoyer la frame au modèle"""
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        timestamp_ms = int(cv2.getTickCount() / cv2.getTickFrequency() * 1000)
        self.detector.detect_async(mp_image, timestamp_ms=timestamp_ms)
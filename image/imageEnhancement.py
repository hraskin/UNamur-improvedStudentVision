import cv2
import numpy as np

def enhance_frame_light(frame, contrast=1.3, brightness=15, contour_color=(0, 0, 0)):
    enhanced = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

    return enhanced

def enhance_frame_edge(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (3, 3))
    edges = cv2.Canny(gray, 60, 120)

    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    frame[edges > 0] = (0, 0, 0)

    return frame

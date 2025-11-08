import time

class FpsTracker:
    def __init__(self):
        self.prev_time = 0

        self.fps = 0
        self.latency_ms = 0

        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        dt = self.end_time - self.prev_time
        frame_time = (self.end_time - self.start_time) * 1000  # latence en ms
        self.latency_ms = 0.9 * self.latency_ms + 0.1 * frame_time
        if dt > 0:
            self.fps = 0.9 * self.fps + 0.1 * (1.0 / dt)
        self.prev_time = self.end_time

    def get_info(self):
        return f"FPS: {self.fps:.1f} | {self.latency_ms:.1f} ms/frame"
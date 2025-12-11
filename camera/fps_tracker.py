import time

class FpsTracker:
    def __init__(self):
        self._prev_time = 0

        self._fps = 0
        self._latency_ms = 0

        self._start_time = None
        self._end_time = None

    def start(self):
        self._start_time = time.time()

    def stop(self):
        self._end_time = time.time()
        dt = self._end_time - self._prev_time
        frame_time = (self._end_time - self._start_time) * 1000  # latence en ms
        self._latency_ms = 0.9 * self._latency_ms + 0.1 * frame_time
        if dt > 0:
            self._fps = 0.9 * self._fps + 0.1 * (1.0 / dt)
        self._prev_time = self._end_time

    def get_info(self):
        return f"FPS: {self._fps:.1f} | {self._latency_ms:.1f} ms/frame"
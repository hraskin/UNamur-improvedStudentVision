import os
import threading
import time
import sounddevice as sd
import numpy as np
import pvporcupine
from typing import Optional

class KeywordsListener:
    def __init__(self, on_wakeword_detected):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        self._porc_en = pvporcupine.create(
            access_key="Pnng6/uadi9yKghjeO9gW0wInNTP+mG6Fqd4cAu/Z2i7xqwwgJMF0g==",
            keyword_paths=[os.path.join(base_dir, "keywords/screen_en_mac_v3_0_0.ppn")]
        )

        self._porc_fr = pvporcupine.create(
            access_key="Nt3JEg9Agd6lGfI0zoi20F+K4YkvwZRpa5kCrfjzS1yYBOyeOPEdEw==",
            keyword_paths=[os.path.join(base_dir, "keywords/capture_fr_mac_v3_0_0.ppn")],
            model_path=os.path.join(base_dir, "models/porcupine_params_fr.pv")
        )

        self._sample_rate: int = self._porc_en.sample_rate
        self._frame_length: int = self._porc_en.frame_length

        self._running: bool = False
        self._thread: Optional[threading.Thread] = None

        self._wakeword_callback = on_wakeword_detected

    def _audio_callback(self, indata, frames, time_info, status):
        pcm = (indata[:, 0] * 32767).astype(np.int16)

        result_en = self._porc_en.process(pcm)
        result_fr = self._porc_fr.process(pcm)

        if result_en >= 0 or result_fr >= 0:
            self._wakeword_callback()

    def _listen_thread(self):
        with sd.InputStream(
            channels=1,
            samplerate=self._sample_rate,
            blocksize=self._frame_length,
            dtype='float32',
            callback=self._audio_callback
        ):
            while self._running:
                time.sleep(0.1)

    def start(self):
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._listen_thread, daemon=True)
        self._thread.start()

    def stop(self):
        if not self._running:
            return
        self._running = False
        if self._thread:
            self._thread.join()
import asyncio
import edge_tts
from pydub import AudioSegment
from pydub.playback import play
import threading

class AudioManager:
    def __init__(self):
        self._loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self._loop.run_forever, daemon=True)
        self._thread.start()

    async def _text_to_speech_async(self, message: str, out_path: str):
        tts = edge_tts.Communicate(message, voice="fr-FR-RemyMultilingualNeural")
        await tts.save(out_path)

    def _run_async(self, coro):
        return asyncio.run_coroutine_threadsafe(coro, self._loop).result()

    def play_audio(self, file_path: str, message: str) -> None:
        out_path = f"{file_path}.mp3"
        self._run_async(self._text_to_speech_async(message, out_path))
        audio = AudioSegment.from_mp3(out_path)
        play(audio)
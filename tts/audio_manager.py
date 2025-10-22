import edge_tts

async def text_to_speech(message: str) -> None:
    """
    Converts the input text message into speech and saves it to a generated audio file.

    Args:
        message (str): The text message to convert into speech.

    This method uses the configured voice and converts the input message
    to speech using the edge_tts library. The generated audio is saved to the path specified.
    """
    tts = edge_tts.Communicate(message, voice='fr-FR-RemyMultilingualNeural')
    await tts.save('output_audio.mp3')
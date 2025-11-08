import os
import platform
import subprocess
import re

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FFMPEG_DIR = os.path.join(PROJECT_ROOT, "ffmpeg")


def _get_ffmpeg_path():
    system = platform.system().lower()
    if system == "windows":
        return os.path.join(FFMPEG_DIR, "win32", "ffmpeg.exe")
    elif system == "darwin":
        return os.path.join(FFMPEG_DIR, "macos", "ffmpeg")
    elif system == "linux":
        return os.path.join(FFMPEG_DIR, "linux", "ffmpeg")
    else:
        raise RuntimeError(f"Système non supporté : {system}")


def detect_index_cameras():
    ffmpeg_path = _get_ffmpeg_path()
    system = platform.system().lower()

    if system == "darwin":
        cmd = [ffmpeg_path, "-f", "avfoundation", "-list_devices", "true", "-i", ""]
        pattern = r"AVFoundation video devices:(.*?)AVFoundation audio devices:"
        parse_regex = r"\[(\d+)\]\s+(.*?)\r?\n"

    elif system == "windows":
        cmd = [ffmpeg_path, "-list_devices", "true", "-f", "dshow", "-i", "dummy"]
        pattern = None
        parse_regex = r'^\[dshow.*?\]\s+"(.*?)"\s+\(video\)$'

    elif system == "linux":
        cmd = [ffmpeg_path, "-f", "v4l2", "-list_devices", "true", "-i", ""]
        pattern = r"video devices:(.*?)$"
        parse_regex = r"\[video\d+\]\s+(.*?)\r?\n"

    else:
        return []

    result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
    output = result.stderr

    if system == "windows":
        cameras = re.findall(parse_regex, output, re.MULTILINE)
    else:
        match = re.search(pattern, output, re.S | re.MULTILINE)
        if not match:
            return []
        section = match.group(1)

        if system == "darwin":
            cameras = [name.strip() for _, name in re.findall(parse_regex, section)]
        elif system == "linux":
            cameras = [name.strip() for name in re.findall(parse_regex, section)]

    ignore_keywords = ["capture screen", "desk view", "virtual", "obs virtual"]
    cameras = [
        name for name in cameras
        if not any(k.lower() in name.lower() for k in ignore_keywords)
    ]

    return cameras
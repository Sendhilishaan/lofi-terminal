from pick import pick
from stream_manager import play_stream

"""
yt-dl: convert into and fetch url
mpv.io: play the stream live
rich: terminal ui
    - progress bar

"""
KEY_CTRL_C = 3
KEY_ESCAPE = 27
QUIT_KEYS = (KEY_CTRL_C, KEY_ESCAPE, ord("q"))

streams = {
    "lofi_girl": "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl",
    "jazz_cafe": "https://www.youtube.com/watch?v=fTb6yJ7AlT8&ab_channel=JazzCafeAmbience"
}

def main():
    title = "what music woiuld you like to listen to?"
    options = ["lofi_girl", "jazz_cafe"]
    option = pick(
    options, title, indicator="=>", default_index=1, quit_keys=QUIT_KEYS
    )
    return option[0]

if __name__ == "__main__":
    stream = main()
    play_stream(streams[stream])
from pick import pick
from stream_manager import play_stream
from rich.tree import Tree
from menu import create_tree

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

tree_dict = {
    "lofi": ["lofi_girl", "test123"],
    "jazz": ["jazz cafe"],
    "end": ''
}

def main():
    title = "what music woiuld you like to listen to?"
    options = create_tree(tree_dict)
    option = pick(
    options, title, indicator="=>", default_index=0, quit_keys=QUIT_KEYS # See if can use io for printed styles, might bug bc printing mul;tple tree to console
    )
    # returns tuple (selected, index)
    return option[0]

if __name__ == "__main__":
    stream = main()
    if stream == "quit":
        print("bye")
    else:
        play_stream(streams[stream])
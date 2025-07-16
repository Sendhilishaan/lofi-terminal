from stream_manager import play_stream
from menu import create_tree, tree_dict
from rich import print

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
    1: "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl", #lofi girl
    2: "https://www.youtube.com/watch?v=ix7eAk1mfvk&ab_channel=SmoothJazzBGM", #rain lofi
    3: "https://www.youtube.com/watch?v=fTb6yJ7AlT8&ab_channel=JazzCafeAmbience" #jazz cafe
}

def main():
    print("what would you like to listen to?")
    for genres in create_tree(tree_dict):
        print(genres)
    ans = int(input())
    try:
        play_stream(streams[ans])
    except:
        print("Selection Error")
        
if __name__ == "__main__":
    main()
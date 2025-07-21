from rich.tree import Tree
from rich import print
from rich.progress import track
from pick import pick
import time
from textual.widgets import Tree
from textual.app import App, ComposeResult
from textual.widget import Widget
from stream_manager import play_stream

streams = {
    '1. lofi_girl': "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl", #lofi girl
    "2. lofi_rain": "https://www.youtube.com/watch?v=ix7eAk1mfvk&ab_channel=SmoothJazzBGM", #rain lofi
    "3. jazz cafe": "https://www.youtube.com/watch?v=fTb6yJ7AlT8&ab_channel=JazzCafeAmbience" #jazz cafe
}

class PlaylistTree(Widget):
    """
    the class that displays our playslists as a tree
    * maybe see if we use RadioSet as our display for our streams, more dynamic?
    """
    def __init__(self):
        super().__init__()
        self.tree_dict = {
            "lofi": ["1. lofi_girl", "2. lofi_rain"],
            "jazz": ["3. jazz cafe"]
        }
    def compose(self) -> ComposeResult:
        """
        creating the playlist tree, allows easy addition of new streams
        to the app by changing tree_dict. key: genre, values: options
        """
        main_tree: Tree[str] = Tree("Music")
        main_tree.root.expand()
        
        for genre, streams in self.tree_dict.items():
            genre_branch = main_tree.root.add(genre)
            genre_branch.expand()

            for stream in streams:
                genre_branch.add_leaf(stream)

        yield main_tree

    def on_tree_node_selected(self, event: Tree.NodeSelected[str]):
        """
        overriding the node selected method, and calling the specific stream to be played
        using play_stream
        """
        if not event.node.children:
            stream_name = str(event.node.label)
            play_stream(streams[stream_name])



def options(player_obj):
    """
    options for the user after selecting initial stream
    1. volume
    2. change stream (display the tree again)
    3. exit

    use rich select?
    """
    options_tree = Tree("options:")
    options_tree.add("1. volume"), options_tree.add("2. change stream"), options_tree.add("3. quit")
    print(options_tree)
    ans = str(input())
    if ans == '1':
        volume(player_obj)
    elif ans =='2':
        from app import main # add this function, import here due to circular import error
        main()
    elif ans == '3':
        quit

def volume(player_obj):
    """
    volume settings, using pick
    i think we switch to rich and figure out how to do keyboard controls
    """
    curr_volume = player_obj.audio_get_volume() // 10


    title = 'Set your volume:'
    options = ['█' if i < curr_volume else '-' for i in range(10)]
    option, index = pick(options, title, default_index=curr_volume)
    player_obj.audio_set_volume(index * 10)

    time.sleep(5)

if __name__ == "__main__":
    app = PlaylistTree()
    app.run()
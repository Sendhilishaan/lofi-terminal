from rich.tree import Tree
from rich import print
from rich.progress import track
from pick import pick
import time
from textual.widgets import Tree
from textual.app import App, ComposeResult
from textual.widget import Widget
#from stream_manager import play_stream
from textual.containers import Center
from textual_slider import Slider
from textual import on
import yt_dlp
import vlc

class PlaylistTree(Widget):
    """
    the class that displays our playslists as a tree
    * maybe see if we use RadioSet as our display for our streams, more dynamic?
    """
    play_obj = None

    streams = {
    '1. lofi_girl': "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl", #lofi girl
    "2. lofi_rain": "https://www.youtube.com/watch?v=ix7eAk1mfvk&ab_channel=SmoothJazzBGM", #rain lofi
    "3. jazz cafe": "https://www.youtube.com/watch?v=fTb6yJ7AlT8&ab_channel=JazzCafeAmbience" #jazz cafe
    }

    def __init__(self):
        super().__init__()
        self.tree_dict = {
            "lofi": ["1. lofi_girl", "2. lofi_rain"],
            "jazz": ["3. jazz cafe"]
        }
        self.player = vlc.Instance(['--no-video', '--quiet'])
        self.opts = {'quiet': True, 'no warnings': True}
    
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

        with Center():
            yield main_tree

    def play_stream(self, selected_stream: str):
        """
        playing the stream using vlc, the input should be a string url
        """
        with yt_dlp.YoutubeDL(self.opts) as ydl:
            
            info = ydl.extract_info(selected_stream, download=False)
            url = info["url"]
        
        #creating our player object with these settings
        PlaylistTree.play_obj = self.player.media_player_new(url)
        PlaylistTree.play_obj.play()

    def on_tree_node_selected(self, event: Tree.NodeSelected[str]):
        """
        overriding the node selected method, and calling the specific stream to be played
        using play_stream
        """
        if not event.node.children:
            stream_name = str(event.node.label)
            self.player = PlaylistTree.play_stream(self, self.streams[stream_name])

class VolumeButton(PlaylistTree):
    """
    class for the volume button slider. Inheriting playlist tree to access the player
    object (clean up).
    """
    def __init__(self):
        super().__init__()
        self.slider = Slider(min=0, max=10, step=1)
    
    def compose(self):
        yield self.slider

    @on(Slider.Changed)
    def change_volume(self):
        if PlaylistTree.play_obj is not None:
            PlaylistTree.play_obj.audio_set_volume(self.slider.value * 10)  # *10 for full range
        else:
            print("[red]No stream is playing. Select a stream first.[/red]")

if __name__ == "__main__":
    app = PlaylistTree()
    app.run()
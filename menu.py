from rich.tree import Tree
from rich.progress import track
import time

# Tree storing genres: [stream names]
tree_dict = {
    "lofi": ["1 - lofi_girl", "2 - test123"],
    "jazz": ["3 - jazz cafe"],
    "    4 - end": ''
}

# creating the tree menu
def create_tree(songs: dict) -> list[Tree]:
    headers = songs.keys()
    menu = []
    for song in headers:
        tree = Tree(song)
        for stream in songs[song]:
            tree.add(stream)
        
        menu.append(tree)

    return menu

def loading():
    for i in track(range(5), description="[cyan]Processing..."):
        time.sleep(1)
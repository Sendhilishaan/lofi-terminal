from rich.tree import Tree
from rich import print
from rich.progress import track
from pick import pick
import time

# Tree storing genres: [stream names]
tree_dict = {
    "lofi": ["1. lofi_girl", "2. lofi_rain"],
    "jazz": ["3. jazz cafe"]
}

# creating the tree menu
def create_tree(tree_dict: dict) -> list[Tree]:
    headers = tree_dict.keys()
    menu = []
    for song in headers:
        tree = Tree(song)
        for stream in tree_dict[song]:
            tree.add(stream)
        
        menu.append(tree)

    return menu

def loading():
    for i in track(range(5), description="[cyan]Loading..."):
        time.sleep(1)

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
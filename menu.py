from rich.tree import Tree
from rich import print

# Tree storing genres: [stream names]
tree_dict = {
    "lofi": ["lofi_girl", "test123"],
    "jazz": ["jazz cafe"],
    "end": ''
}

# creating the tree menu
def create_tree(songs: dict) -> list[Tree]: # I think making it all under one tree is easiuer for pick
    headers = songs.keys()
    menu = []
    for song in headers:
        tree = Tree(song)
        for stream in songs[song]:
            tree.add(stream)
        
        menu.append(tree)

    return menu

a = create_tree(tree_dict)
for i in a:
    print(i)


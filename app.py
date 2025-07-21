from stream_manager import*
from menu import options, PlaylistTree
from rich import print
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual.containers import Horizontal, Vertical, Center, Middle
from textual.widget import Widget

# container for the playlist display
class LeftCont(Widget):
    DEFAULT_CSS = """
    LeftCont {
    width: 1fr;
    height: 1fr;
    }
"""

# container for animations
class TopRight(Widget):
    DEFAULT_CSS = """
    TopRight {
    width: 1fr;
    height: 1fr;
    }
"""

# container for settings
class TopLeft(Widget):
    DEFAULT_CSS = """
    TopLeft {
    width: 1fr;
    height: 1fr;
    }
"""

# container for the settings and the animation tab
class RightCont(Widget):
    DEFAULT_CSS = """
    RightCont {
    width: 1fr;
    height: 1fr;
    }
"""

class lofiterminal(App):
    """
    our main class for the app
    """
    #keybinds, (key, command, description)
    BINDINGS = [('d', 'toggle_dark', 'toggle dark mode')]

    def compose(self) -> ComposeResult:
        #create child widgets for app
        with Horizontal():
            with LeftCont():
                yield PlaylistTree()
            with RightCont():
                yield TopLeft()
                yield TopRight()
        yield Footer()
        yield Header()
    
    def action_toggle_dark(self) -> None:
        """overriding the toggle dark class"""
        self.theme = (
                "textual-dark" if self.theme == "textual-light" else "textual-light"
            )

if __name__ == "__main__":
    app = lofiterminal()
    app.run()
    
from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from .functions import *


def setup_keys(mod, terminal):
    return [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
        Key(["mod1"], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
        Key([mod], "d", minimize_all(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "mod1"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "mod1"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "mod1"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "mod1"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod, "mod1"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "mod1"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "mod1"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "mod1"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Move between adjacent groups
        Key([mod, "control"], "h", lazy.screen.prev_group(), desc="Move window focus to other window"),
        Key([mod, "control"], "l", lazy.screen.next_group(), desc="Move window focus to other window"),
        Key([mod, "control"], "Left", lazy.screen.prev_group(), desc="Move window focus to other window"),
        Key([mod, "control"], "Right", lazy.screen.next_group(), desc="Move window focus to other window"),
        # Move window between adjacent groups
        Key([mod, "control", "shift"], "h", window_to_prev_group(), desc="Move window focus to other window"),
        Key([mod, "control", "shift"], "l", window_to_next_group(), desc="Move window focus to other window"),
        Key([mod, "control", "shift"], "Left", window_to_prev_group(), desc="Move window focus to other window"),
        Key([mod, "control", "shift"], "Right", window_to_next_group(), desc="Move window focus to other window"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([mod], "f", lazy.window.toggle_floating()),
        # Launchers
        KeyChord([mod], "Return",
            [
                Key([], "Return", lazy.spawn(terminal), lazy.ungrab_all_chords(), desc="Launch terminal"),
                Key([], "b", lazy.spawn("firefox"), lazy.ungrab_all_chords(), desc="Launch browser"),
                Key([], "p", lazy.spawn("firefox --private-window"), lazy.ungrab_all_chords(), desc="Launch private browser"),
                Key([], "e", lazy.spawn("nautilus"), lazy.ungrab_all_chords(), desc="Launch file browser"),
                Key([], "i", lazy.spawn("gnome-control-center"), lazy.ungrab_all_chords(), desc="Launch settings manager"),
            ],
            name=" Run"
        ),
        # Toggle between different layouts as defined below
        Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod], "l", lazy.spawn("betterlockscreen -l"), desc="Lock the screen"),
    ]

from libqtile.config import ScratchPad, Group, DropDown, Key, Match
from libqtile.lazy import lazy

def setup_scratchpads(mod, terminal):
    groups = [
        ScratchPad("scratchpad", [
            DropDown(
                "term",
                terminal,
                width=0.5,
                height=0.5,
                x=0.25,
                y=0.25,
                opacity=1.0,
            ),
            DropDown(
                "nvim",
                f"{terminal} -e nvim",
                width=0.5,
                height=0.5,
                x=0.25,
                y=0.25,
                opacity=1.0,
            ),
            DropDown(
                "files",
                "nautilus",
                width=0.5,
                height=0.5,
                x=0.25,
                y=0.25,
                opacity=1.0,
            )
        ]),
    ]
    keys = [
        Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("term"), desc="Terminal scratchpad"),
        Key([mod], "v", lazy.group["scratchpad"].dropdown_toggle("nvim"), desc="Neovim scratchpad"),
        Key([mod], "e", lazy.group["scratchpad"].dropdown_toggle("files"), desc="File Browser scratchpad"),
    ]
    
    return groups, keys

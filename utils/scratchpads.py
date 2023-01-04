from libqtile.config import ScratchPad, Group, DropDown, Key, Match
from libqtile.lazy import lazy

def setup_scratchpads(mod, terminal):
    defaults = dict(
        width=0.5,
        height=0.5,
        x=0.25,
        y=0.25,
        opacity=1.0,
    )
    groups = [
        ScratchPad("scratchpad", [
            DropDown(
                "term",
                terminal,
                **defaults
            ),
            DropDown(
                "nvim",
                f"{terminal} -e nvim",
                **defaults
            ),
            DropDown(
                "btop",
                f"{terminal} -e btop",
                **defaults
            ),
        ]),
    ]
    keys = [
        Key(
            [mod], "t",
            lazy.group["scratchpad"].dropdown_toggle("term"),
            desc="Terminal scratchpad"
        ),
        Key(
            [mod], "v",
            lazy.group["scratchpad"].dropdown_toggle("nvim"),
            desc="Neovim scratchpad"
        ),
        Key(
            ["control", "shift"], "Escape",
            lazy.group["scratchpad"].dropdown_toggle("btop"),
            desc="Monitor scratchpad"
        ),
    ]
    return groups, keys

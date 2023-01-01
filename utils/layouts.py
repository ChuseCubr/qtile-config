from libqtile import layout
from .colors import Colors


def setup_layouts():
    defaults = {
        "border_focus"     : Colors.BLUE3,
        "border_normal"    : Colors.BLACK0,
        "border_on_single" : True,
        "border_width"     : 0,
        "margin"           : 5
    }
    return [
        layout.Columns(**defaults),
        layout.Max(**defaults),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
    ]

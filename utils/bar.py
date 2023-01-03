from libqtile import bar, widget
from libqtile.lazy import lazy

from .colors import Colors
from .rofi import get_command


def setup_bar():
    widget_defaults = dict(
        font="FantasqueSansMono Nerd Font",
        foreground=Colors.WHITE2,
        fontsize=18,
        padding=12,
    )
    extension_defaults = widget_defaults.copy()
    screen_bar = bar.Bar(
        [
            widget.CurrentLayoutIcon(
                background=Colors.BLUE2,
                padding=5,
                scale=0.5,
            ),
            widget.Chord(
                background=Colors.BLUE2,
            ),
            widget.GroupBox(
                font="FantasqueSansMono Nerd Font",
                active=Colors.BLUE2,
                block_highlight_text_color=Colors.BLUE2,

                inactive=Colors.WHITE0,

                highlight_color=Colors.BLACK3,
                this_current_screen_border=Colors.BLUE3,
                highlight_method="line",

                padding=10,
                fontsize=14,
            ),
            widget.WindowName(
                foreground=Colors.BLUE0,
                max_chars=50,
            ),
            # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
            # widget.StatusNotifier(),
            widget.Systray(),
            widget.PulseVolume(
                fmt="墳",  # \ufa7d
                # fmt=" {}",  # \uf028
                volume_app="pavucontrol",
                foreground=Colors.WHITE0,
                mouse_callbacks={
                    "Button1": lazy.spawn(get_command("volume")),
                },
            ),
            widget.Spacer(length=15),
            widget.Battery(
                format="{char} {percent:2.0%}",
                foreground=Colors.GREEN,
                full_char="",  # \u578
                unknown_char="",
                charge_char="",  # \uf588
                discharge_char="",  # \uf57e
                empty_char="",  # \uf579
                low_percentage=0.2,
                low_foreground=Colors.ORANGE,
                update_interval=1,
            ),
            widget.Clock(
                format="  %a %b %-d",  # \uf5ec
                # format="  %a %b %-d",  # \uf073
                foreground=Colors.BLUE1,
            ),
            widget.Clock(
                format="  %H:%M",  # \uf64f
                # format="  %H:%M", #  \uf017
            ),
            widget.Spacer(length=15),
            widget.QuickExit(
                foreground=Colors.BLACK0,
                background=Colors.RED,
                default_text=" 襤 ",  # \uf011
                # default_text="  ", #  \uf924
                countdown_format=" {} ",
            ),
        ],
        36,
        background=Colors.BLACK1,
        opacity=1.0,
        margin=5,
        # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    )
    return screen_bar, widget_defaults, extension_defaults

from os.path import expanduser
from libqtile.config import Key
from libqtile.lazy import lazy


def setup_rofi(mod):
    alt = "mod1"
    rofi_path = expanduser("~/.config/rofi")
    launcher_path = rofi_path + "/launchers/type-1/launcher.sh"
    return [
        Key([alt], "space", lazy.spawn(launcher_path), desc="Spawn rofi launcher"),
    ]

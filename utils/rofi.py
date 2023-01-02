from os.path import expanduser
from libqtile.config import Key
from libqtile.lazy import lazy


def setup_rofi(mod):
    rofi_path = expanduser("~/.config/rofi")
    return [
        Key(["mod1"], "space", lazy.spawn(f"{rofi_path}/launchers/launcher.sh"), desc="Spawn rofi launcher"),
        Key([mod], "Tab", lazy.spawn(f"{rofi_path}/launchers/window.sh"), desc="Spawn rofi window walker"),
        Key([mod, "shift"], "s", lazy.spawn(f"{rofi_path}/applets/bin/screenshot.sh"), desc="Interactive screenshot")
    ]

def get_command(command):
    rofi_path = expanduser("~/.config/rofi")
    match command:
        case "volume":
            return rofi_path + "/applets/bin/volume.sh"
        case "launcher":
            return rofi_path + "/launchers/launcher.sh"

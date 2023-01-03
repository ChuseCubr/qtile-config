from os.path import expanduser
from libqtile.config import Key
from libqtile.lazy import lazy


def setup_rofi(mod):
    rofi_path = expanduser("~/.config/rofi")
    keys = [
        Key(
            ["mod1"], "space",
            lazy.spawn(f"{rofi_path}/launchers/launcher.sh"),
            desc="Rofi launcher"
        ),
        Key(
            [mod], "Tab",
            lazy.spawn(f"{rofi_path}/launchers/window.sh"),
            desc="Rofi window walker"
        ),
        Key([mod, "shift"], "s",
            lazy.spawn(f"{rofi_path}/applets/bin/screenshot.sh"),
            desc="Interactive screenshot"
        ),
        Key(
            [mod, "control"], "q",
            lazy.spawn(f"{rofi_path}/applets/bin/powermenu.sh"),
            desc="Rofi power menu"
        ),
    ]
    return rofi_path, keys

def get_command(command):
    rofi_path = expanduser("~/.config/rofi")
    match command:
        case "volume":
            return lazy.spawn(f"{rofi_path}/applets/bin/volume.sh")
        case "powermenu":
            return lazy.spawn(f"{rofi_path}/applets/bin/powermenu.sh")
        case _:
            raise Exception("Invalid rofi command")

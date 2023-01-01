from libqtile.config import Group, Key
from libqtile.lazy import lazy


def setup_groups(mod):
    groups = []
    keys = []
    defaults = {
        "layout": "columns",
    }
    for idx, label in enumerate("一二三四五六七八九十"):
        groups.append(
            Group(name=str((idx+1)%10),
                  label=label,
                  **defaults)
        )
    for group in groups:
        keys.extend([  # mod1 + letter of group = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ])
    return groups, keys

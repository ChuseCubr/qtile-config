from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy


def setup_groups(mod):
    groups, keys = setup_special(mod)
    specials = len(groups)
    defaults = dict(
        layout="columns",
    )
    kanji = "一二三四五六七八九十"
    labels = kanji[:7]

    for idx, label in enumerate(labels):
        groups.append(
            Group(
                name=str((idx+1)%10),
                label=label,
                **defaults
            )
        )

    for group in groups[specials:]:
        keys.extend([  # mod1 + letter of group = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc=f"Switch to group {group.name}"
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc=f"Switch to & move focused window to group {group.name}"
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ])

    return groups, keys

def setup_special(mod):
    groups = [
        Group(
            name="settings",
            label=" ",
            matches=[
                Match(wm_class="easyeffects")
            ]
        ),
        Group(
            name="chat",
            label="ﭮ",
            matches=[
                Match(wm_class="discord"),
                Match(wm_class="caprine"),
            ]
        ),
    ]
    keys = [
        Key(
            [mod], "i",
            lazy.group["settings"].toscreen(toggle=True),
            desc="Settings scratchpad"
        ),
        Key([mod], "c",
            lazy.group["chat"].toscreen(toggle=True),
            desc="Chat group"
        ),
    ]
    return groups, keys

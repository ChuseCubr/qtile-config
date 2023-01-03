from libqtile.lazy import lazy

@lazy.function
def window_to_prev_group(qtile):
    group_count = len(qtile.groups)
    idx = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None:
        new_idx = (idx - 1) % (group_count - 1)
        qtile.current_window.togroup(qtile.groups[new_idx].name)
        qtile.current_screen.prev_group()

@lazy.function
def window_to_next_group(qtile):
    group_count = len(qtile.groups)
    idx = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None:
        new_idx = (idx + 1) % (group_count - 1)
        qtile.current_window.togroup(qtile.groups[new_idx].name)
        qtile.current_screen.next_group()

@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

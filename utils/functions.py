from libqtile.lazy import lazy

@lazy.function
def window_to_prev_group(qtile):
    group_count = len(qtile.groups)
    idx = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None:
        new_idx = (idx - 1) % group_count
        qtile.current_window.togroup(qtile.groups[new_idx].name)
        qtile.current_screen.prev_group()

@lazy.function
def window_to_next_group(qtile):
    group_count = len(qtile.groups)
    idx = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None:
        new_idx = (idx + 1) % group_count
        qtile.current_window.togroup(qtile.groups[new_idx].name)
        qtile.current_screen.next_group()

def fix_cli_app(terminal, app):
    '''Quick fix of github.com/qtile/qtile/issues/2167 bug'''
    fix_environment = 'export -n LINES; export -n COLUMNS; sleep 0.1 &&'
    return f'{terminal} -t {app} -e sh -c "{fix_environment} {app}"'

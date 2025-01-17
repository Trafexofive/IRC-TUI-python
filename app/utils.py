import curses

def debug_print(message, window=None):
    """Print debug output if debug mode is enabled."""
    if window:
        safe_addstr(window, f"[DEBUG] {message}\n", curses.color_pair(4))

def safe_addstr(win, text, color_attr=0):
    """Safely add text to a curses window."""
    try:
        win.addstr(text, color_attr)
        win.refresh()
    except curses.error:
        pass

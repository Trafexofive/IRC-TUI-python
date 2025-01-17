import curses
from app.client import IRCClient
from app.commands import handle_slash_command
from app.utils import debug_print, safe_addstr

class IRCTUI:
    def __init__(self, stdscr, args):
        self.stdscr = stdscr
        self.args = args
        self.chat_window = None
        self.input_window = None
        self.client = IRCClient(
            server=args.server,
            port=args.port,
            nick=args.nick,
            user=args.user,
            realname=args.real,
            password=args.password
        )
        self.running = True

    def setup_curses(self):
        """Initialize curses settings and windows."""
        curses.curs_set(1)
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_YELLOW, -1)
        curses.init_pair(3, curses.COLOR_CYAN, -1)
        curses.init_pair(4, curses.COLOR_MAGENTA, -1)

        height, width = self.stdscr.getmaxyx()
        self.chat_window = curses.newwin(height - 2, width, 0, 0)
        self.input_window = curses.newwin(1, width, height - 1, 0)

    def run(self):
        """Main TUI event loop."""
        self.setup_curses()
        self.client.connect()
        self.client.start_reader(self.handle_server_message)

        safe_addstr(self.chat_window, f"[Info] Connected to {self.args.server}:{self.args.port}\n", curses.color_pair(3))
        safe_addstr(self.chat_window, "[Info] Type '/commands' for help. Type '/exit' to quit.\n\n", curses.color_pair(3))

        while self.running:
            self.input_window.clear()
            self.input_window.refresh()
            try:
                curses.echo()
                user_input = self.input_window.getstr(0, 0).decode('utf-8').strip()
                curses.noecho()
            except (KeyboardInterrupt, EOFError):
                self.running = False
                break

            if not user_input:
                continue

            if user_input.startswith("/"):
                handle_slash_command(user_input, self.client, self.chat_window)
            else:
                self.client.send(user_input)

        self.client.disconnect()
        safe_addstr(self.chat_window, "[Info] Disconnected from server.\n", curses.color_pair(3))
        self.chat_window.refresh()
        curses.napms(1000)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Enhanced Interactive IRC Client with a TUI.")
    parser.add_argument("-s", "--server", default="localhost", help="Server hostname/IP")
    parser.add_argument("-p", "--port", type=int, default=22200, help="Server port")
    parser.add_argument("-n", "--nick", default="myNickname", help="Nickname to use")
    parser.add_argument("-u", "--user", default="myUsername", help="USER field")
    parser.add_argument("-r", "--real", default="myRealName", help='Real name')
    parser.add_argument("-P", "--password", default=None, help="IRC password (optional)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    curses.wrapper(lambda stdscr: IRCTUI(stdscr, args).run())

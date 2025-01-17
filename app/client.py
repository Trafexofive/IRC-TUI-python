import socket
import threading

class IRCClient:
    def __init__(self, server, port, nick, user, realname, password=None):
        self.server = server
        self.port = port
        self.nick = nick
        self.user = user
        self.realname = realname
        self.password = password
        self.socket = None
        self.running = False
        self.reader_thread = None

    def connect(self):
        """Connect to the IRC server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server, self.port))
        self.running = True

        # Send initial registration commands
        if self.password:
            self.send(f"PASS {self.password}")
        self.send(f"NICK {self.nick}")
        self.send(f"USER {self.user} 0 * :{self.realname}")

    def send(self, message):
        """Send a message to the IRC server."""
        if not message.endswith('\r\n'):
            message += '\r\n'
        self.socket.sendall(message.encode('utf-8'))

    def start_reader(self, callback):
        """Start a thread to read messages from the server."""
        def reader():
            while self.running:
                try:
                    data = self.socket.recv(4096)
                    if not data:
                        break
                    callback(data.decode('utf-8', errors='replace').rstrip('\r\n'))
                except Exception as e:
                    callback(f"[Error] Reading from server: {e}")
                    break
        self.reader_thread = threading.Thread(target=reader, daemon=True)
        self.reader_thread.start()

    def disconnect(self):
        """Disconnect from the IRC server."""
        self.running = False
        if self.socket:
            self.socket.close()

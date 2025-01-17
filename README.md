# IRC TUI Client

A lightweight, terminal-based IRC client with a **Text User Interface (TUI)** built using Python and `curses`. Connect to IRC servers, join channels, and chat with others—all from the comfort of your terminal.

![Demo Screenshot](demo.png) <!-- Add a screenshot later if you want -->

---

## Features

- **Terminal-Based Interface**: A clean, intuitive TUI powered by `curses`.
- **Slash Commands**: Quickly execute IRC commands like `/join`, `/msg`, `/nick`, and more.
- **Auto-Connect**: Automatically authenticate with the server using `/auto`.
- **Debug Mode**: Enable detailed debug output for troubleshooting.
- **Modular Design**: Code is organized into reusable modules for easy maintenance and extension.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/irc_tui.git
   cd irc_tui
   ```

2. Run the client:
   ```bash
   python3 irc_tui.py --server irc.example.com --port 6667 --nick YourNick
   ```

---

## Usage

### Command-Line Options

| Option         | Description                          | Default Value   |
|----------------|--------------------------------------|-----------------|
| `--server`     | IRC server hostname or IP            | `localhost`     |
| `--port`       | IRC server port                      | `22200`         |
| `--nick`       | Your nickname                        | `myNickname`    |
| `--user`       | Your username                        | `myUsername`    |
| `--real`       | Your real name                       | `myRealName`    |
| `--password`   | IRC server password (optional)       | `None`          |
| `--debug`      | Enable debug output                  | `False`         |

### Slash Commands

| Command               | Description                                      |
|-----------------------|--------------------------------------------------|
| `/auto`               | Automatically sends PASS, NICK, and USER.        |
| `/password <password>`| Sets the IRC password and sends PASS.            |
| `/nickname <nickname>`| Changes your nickname.                           |
| `/login <username>`   | Logs in with the specified username.             |
| `/channel <channel>`  | Joins the specified channel.                     |
| `/ping <target>`      | Sends a PING to the target.                      |
| `/msg <target> <msg>` | Sends a private message to the target.           |
| `/exit`               | Exits the client.                                |
| `/commands`           | Displays a list of available slash commands.     |

---

## Project Structure

```
irc_tui/
├── irc_tui.py          # Main entry point
├── app/                # Application logic
│   ├── __init__.py     # Package initialization
│   ├── client.py       # IRC client logic (socket handling, messaging)
│   ├── tui.py          # Curses-based TUI (interface, input handling)
│   ├── commands.py     # Slash command parsing and execution
│   └── utils.py        # Utility functions (debug, safe printing)
├── tests/              # Unit and integration tests
│   ├── __init__.py
│   ├── test_client.py
│   ├── test_tui.py
│   └── test_commands.py
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── .gitignore          # Git ignore file
```

---

## Contributing

We welcome contributions! Here’s how you can help:

1. **Fork the repository** and clone it locally.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push your branch to GitHub:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a **Pull Request** and describe your changes.

Please ensure your code follows the project's style and includes relevant tests.

---

## Roadmap

### Planned Features
- **SSL/TLS Support**: Secure connections to IRC servers.
- **Multi-Channel Support**: Join and switch between multiple channels.
- **Command History**: Navigate previous commands with arrow keys.
- **Configuration File**: Save server details, nicknames, and preferences.

### Known Issues
- Limited error handling for network disruptions.
- No support for DCC (Direct Client-to-Client) file transfers.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by classic IRC clients like `irssi` and `weechat`.
- Built with ❤️ using Python and `curses`.

---

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/Trafexofive/IRC-TUI-python/issues).


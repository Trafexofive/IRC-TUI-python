def handle_slash_command(cmd_input, client, chat_window):
    """Handle slash commands."""
    parts = cmd_input.strip().split(maxsplit=1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""

    if command == "/exit":
        client.running = False

    elif command == "/commands":
        # Display help (implement this function)
        pass

    elif command == "/auto":
        if client.password:
            client.send(f"PASS {client.password}")
        client.send(f"NICK {client.nick}")
        client.send(f"USER {client.user} 0 * :{client.realname}")

    # Add other commands here...

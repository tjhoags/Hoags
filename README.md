# Discord Bot

A simple Discord bot built with Python and discord.py.

## Features

- `!hello` - Greets the user
- `!ping` - Check bot latency
- `!info` - Get bot information
- `!echo <message>` - Echo a message
- `!help` - Show all available commands

## Setup

1. Install Python 3.8 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```
DISCORD_TOKEN=your_discord_bot_token_here
```

4. Get your Discord bot token:
   - Go to https://discord.com/developers/applications
   - Create a new application or select an existing one
   - Go to the "Bot" section
   - Copy the token and add it to your `.env` file

5. Invite the bot to your server:
   - In the Discord Developer Portal, go to OAuth2 > URL Generator
   - Select "bot" scope
   - Select necessary permissions (Send Messages, Read Messages, etc.)
   - Copy the generated URL and open it in your browser
   - Select your server and authorize

6. Run the bot:
```bash
python bot.py
```

## Commands

- `!hello` - Greets the user
- `!ping` - Check bot latency
- `!info` - Get bot information
- `!echo <message>` - Echo a message
- `!help` - Show all available commands

## License

MIT


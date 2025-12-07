# Discord Bot Setup Instructions

## Quick Start

1. **Get your Discord Bot Token:**
   - Go to https://discord.com/developers/applications
   - Create a new application or select an existing one
   - Navigate to the "Bot" section
   - Click "Reset Token" or "Copy" to get your bot token
   - Make sure to enable "Message Content Intent" in the Bot settings

2. **Create your .env file:**
   ```bash
   # In the discord-bot directory, create a .env file with:
   DISCORD_TOKEN=your_actual_token_here
   ```

3. **Run the bot:**
   ```bash
   python bot.py
   ```

4. **Invite the bot to your server:**
   - In Discord Developer Portal, go to OAuth2 > URL Generator
   - Select "bot" scope
   - Select permissions: Send Messages, Read Messages, Use Slash Commands
   - Copy the generated URL and open it in your browser
   - Select your server and authorize

## Bot Commands

Once running, the bot supports these commands:
- `!hello` - Greets the user
- `!ping` - Check bot latency  
- `!info` - Get bot information
- `!echo <message>` - Echo a message
- `!help` - Show all available commands

## Troubleshooting

- **"DISCORD_TOKEN not found"**: Make sure you created a `.env` file with your token
- **Bot doesn't respond**: Check that the bot is online in your server and has proper permissions
- **Import errors**: Run `pip install -r requirements.txt` to install dependencies


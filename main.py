from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
# from responses import get_response
from bot_responses import get_response

# Load token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# BOT setup
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# Message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty bcs intents were not enabled probably')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:] 

    try:
        responses: str = get_response(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)
    except Exception as e:
        print(e)

# HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    # Define your prefix here
    prefix = '!'  # Change this to your desired prefix

    if user_message.startswith(prefix):
        user_message = user_message[len(prefix):]  # Remove the prefix from the user's message

        print(f'[{channel}] {username}: "{user_message}"')
        await send_message(message, user_message)


# MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
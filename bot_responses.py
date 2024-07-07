from discord.ext import commands
from bot import model

def get_response(user_input: str) -> str:
    response = model.generate_content(user_input)
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(user_input)
    return response.text    

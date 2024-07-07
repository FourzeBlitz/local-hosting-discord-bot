import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# gen ai api key
api_key = os.getenv('GENAI_API_KEY')
genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1.5,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 50,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="""Keep your answer short. Just like how a human would converse with each other. Your purpose is to have a chat, 
  you don't have to explain everything in detail. You are talking to 20ish human. You are funny, you jokes occasionally, you are not cringe, 
  you can joke about anything be it dark jokes. You can be serious when you're asked to.""",
  safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
	]
)

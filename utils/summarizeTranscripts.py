# .env
from dotenv import load_dotenv
import os

# Gemini API
import google.generativeai as genai

# load .env
load_dotenv()

API_KEY = os.environ.get('GEMINI_API_KEY')

genai.configure(api_key=API_KEY)
genai_model = genai.GenerativeModel('gemini-pro')

# Extract information from text based on prompt instructions
def get_ai_extract(prompt, text):
    response = genai_model.generate_content(prompt + text, stream=False)
    return response.text, response.prompt_feedback, response.candidates
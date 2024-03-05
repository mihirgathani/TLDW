"""
Module for summarizing transcripts using Gemini AI API.
"""

# Gemini API
import google.generativeai as genai

GEMINI_API_KEY = 'AIzaSyAIDOlnc6NVX9LCwvNNuF6zXqBWplJsVpM' # Anurag Key



genai.configure(api_key=GEMINI_API_KEY)
genai_model = genai.GenerativeModel('gemini-pro')

# Extract information from text based on prompt instructions
def get_ai_extract(prompt, text):
    """
    Extract information from text based on prompt instructions.

    Args:
        prompt (str): The prompt to be used for extraction.
        text (str): The text from which information needs to be extracted.

    Returns:
        tuple: A tuple containing extracted text, prompt feedback, and candidates.
    Raises:
        ValueError: If prompt or text is empty.
    """
    if len(prompt) == 0:
        raise ValueError("Prompt cannot be empty")
    if len(text) == 0:
        raise ValueError("Text cannot be empty")
    response = genai_model.generate_content(prompt + text, stream=False)
    return response.text, response.prompt_feedback, response.candidates

from dotenv import load_dotenv
import openai
import os

load_dotenv

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=1,
        max_tokens=100
    )

    response_dict = response.get("choice")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["message"]
from dotenv import load_dotenv
import openai
import os

load_dotenv

openai.api_key = os.getenv('OPENAI_API_KEY')

def chatgpt_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        #prompt=prompt,
        temperature=1,
        max_tokens=100
    )
  #  print(response)
    
    
    choices = response.choices
    print(choices)

    if choices and len(choices) > 0:
        prompt_response = choices[0].message.content
        return prompt_response
    else:
        return "No response, try again."

    
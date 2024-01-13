from dotenv import load_dotenv
import openai
import os

load_dotenv

openai.api_key = os.getenv('OPENAI_API_KEY')

def chatgpt_response(prompt, conversation_history=[]):
    conversation_history.append({"role": "user", "content": prompt})# add prompt to conversation history
    conversation_history = conversation_history[-10:] # limit to the last 10 sent messages

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
       # messages=[
          #  {"role": "user", "content": prompt}
       # ],
        #prompt=prompt,
        temperature=1,
        max_tokens=1999
    )
  #  print(response)
    
    
    choices = response.choices
    print(choices)

    if choices and len(choices) > 0:
        prompt_response = choices[0].message.content
        if len(prompt_response) < 2000:
            conversation_history.append({"role": "assistant", "content": prompt_response}) # add conversation history
            return prompt_response
        else:
            return "Response generated was longer than 2000 characters (discord's limit). Try ending your prompt with 'less than 2000 characters'"
    else:
        return "No response, try again."

    
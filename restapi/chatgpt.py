import json
import os
import openai
import requests

openai.organization = "org-DNxfXWzcLdaOuK6iRqMXhsDb"
openai.api_key = os.getenv('OPENAI_API_KEY')
while True:
    text = input("You : ")
    if text == 'exit':
        break
    api_url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + str(openai.api_key)}
    request = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": text}]}
    response = requests.post(api_url, data=json.dumps(request), headers=headers)
    responsejson = response.json()
    output = responsejson['choices'][0]['message']['content']
    print(output)

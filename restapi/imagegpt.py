import json
import os
import openai
import requests

openai.organization = "org-DNxfXWzcLdaOuK6iRqMXhsDb"
openai.api_key = os.getenv('OPENAI_API_KEY')
while True:
    text = input("You : ")
    if text == 'exit':
        break;
    api_url = "https://api.openai.com/v1/images/generations"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + str(openai.api_key)}
    request = {'prompt': text, "n": 3, "size": "1024x1024"}
    response = requests.post(api_url, data=json.dumps(request), headers=headers)
    resonsejson = response.json()
    urls=resonsejson['data'];
    for item in urls:
        print(item['url'])


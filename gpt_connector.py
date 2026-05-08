import os
import requests

from dotenv import load_dotenv #package is called python-dotenv
load_dotenv()
PPLX_API_KEY=os.environ.get("PPLX_API_KEY")

url = "https://api.perplexity.ai/chat/completions"

#possible models: https://docs.perplexity.ai/docs/model-cards

payload = {
    "model": "mistral-7b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
    ]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer {0}".format(PPLX_API_KEY)
}


#add question
payload["messages"].append({"role": "user", "content": "New question"})
#change question
payload["messages"][1].update({"role": "user", "content": "New question"})

response = requests.post(url, json=payload, headers=headers)

print(response.text)
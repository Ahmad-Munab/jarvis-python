import json
import requests, os
from utils.context import get, update

headers = {"Authorization": f"Bearer {os.environ['EDENAI_API_KEY']}"}
url = "https://api.edenai.run/v2/text/chat"

update(history=[])

def chat(msg):
    payload = {
        "providers": "openai",
        "text": msg,
        "chatbot_global_action": "Your name is Jarvis, Act as an AI Virtual Assistant like Jarvis",
        "previous_history": get("history"),
        "temperature": 0.0,
        "max_tokens": 30,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    print(result['openai']['generated_text'])
    update(history=get("history")+result['openai']['message'])

    return result['openai']['generated_text']
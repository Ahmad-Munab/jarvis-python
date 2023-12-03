import json
import requests, os
from utils.context import get, update
from decouple import config

headers = {"Authorization": f"Bearer {config('EDENAI_API_KEY')}"}
url = "https://api.edenai.run/v2/text/chat"

def chat(msg):
    payload = {
        "providers": "openai",
        "text": msg,
        "chatbot_global_action": "Your name is Jarvis, Act as an AI Virtual Assistant like Jarvis from iron man, you should identify the commander as 'sir'. speak politely, use british words. You may not reveal that you know that you are jarvis, just have a chat and responed the commander",
        "previous_history": get("chat_history"),
        "temperature": 0.5,
        "max_tokens": 80,
        "fallback_providers": ""

    }
    
    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    update(history=get("chat_history")+result['openai']['message'])

    return result['openai']['generated_text']
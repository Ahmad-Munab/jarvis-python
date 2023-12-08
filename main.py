from intent_classification import process
from utils.voice_utils import speak, listen
import random

def listen_and_respond():
    print("---Listening---")
    text = listen()
    if text == "loop":
        return
    process(text)


greetings = [
    "Hi, how are you?",
    "I'm here!",
    "Welcome!",
    "How can I help?",
    "Ready for tasks.",
    "What's up?",
    "Good day!",
    "Ready for commands.",
    "Hello, ready to assist.",
    "Hi, how can I help?",
    "Greetings! How can I assist?",
    "Hello, at your service."
]

goodbyes = [
    "Bye, take care!",
    "See you!",
    "Farewell!",
    "Goodbye, stay safe!",
    "Until next time!",
    "Adios!",
    "Bye for now!",
    "Safe travels!",
    "Take care!",
    "See you soon!",
    "Bye-bye!",
    "Goodbye!",
    "Farewell, friend!"
]

if __name__ == "__main__":
    speak(random.choice(greetings))
    try:
        while True:
            listen_and_respond() 
    except KeyboardInterrupt:
        speak(random.choice(goodbyes))
        quit()

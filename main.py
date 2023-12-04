from funcionality import process
from utils.voice_utils import speak, listen
import random

def listen_and_respond():
    text = listen()
    process(text)


greetings = [
    "Hi sir, how are you doing?",
    "Hello sir, thanks for starting me",
    "I'm awake!",
    "Welcome",
    "Greetings, how may I assist you today?",
    "Hello there, ready to tackle tasks.",
    "Hi, what can I do for you now?",
    "Good day! How can I be of service?",
    "Hey, I'm here and ready for your commands.",
    "Hello, how can I make your day better?",
    "Hi there! Ready to help with anything.",
    "Greetings! What's on your agenda today?",
    "Hello, I'm at your service. What do you need?"
]

if __name__ == "__main__":
    speak(random.choice(greetings))

    try:
        while True:
            listen_and_respond() 
    except KeyboardInterrupt:
        speak("Bye sir; Closing...")
        quit()

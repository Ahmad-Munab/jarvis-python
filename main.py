import speech_recognition as sr
from funcionality import process
from utils.voice_utils import speak
import random

def listen_and_respond():
    # Initialize the speech recognizer
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=0.5)

                # Listen for audio input
                audio = recognizer.listen(source)
                # Recognize the speech
                text = recognizer.recognize_google(audio)

                # Process the recognized text
                print(text)
                print("Understanding and Processing")
                process(text)

            # Handle errors if no speech is recognized
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except Exception as e:
                if "timed out" in str(e):
                    continue
                print("Error:", e)
                speak("Error taking voice input")


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
            try:
                listen_and_respond()
            except (sr.UnknownValueError, sr.WaitTimeoutError):
                continue
    except KeyboardInterrupt:
        speak("Bye sir; Closing...")
        quit()

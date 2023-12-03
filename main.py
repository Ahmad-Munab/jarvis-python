# Import the libraries

import speech_recognition as sr

import vosk
import pyaudio

from funcionality import process
from utils.voice_utils import speak

import random


### ONE ###
r = sr.Recognizer()
r.pause_threshold = 0.5
r.phrase_threshold = -25
r.operation_timeout = 3

#### TWO #####
# # Define the Vosk model path
# model_path = "./vosk_models/vosk-model-en-us-0.22-lgraph"  # Replace with the actual path to your Vosk model

# # Define the sample rate and the chunk size
# sample_rate = 16000
# chunk_size = 8000

# # Initialize the Vosk recognizer
# model = vosk.Model(model_path)
# recognizer = vosk.KaldiRecognizer(model, sample_rate)

# # Capture audio input from the microphone
# pa = pyaudio.PyAudio()
# # Use the pyaudio.open() method to create a stream object
# stream = pa.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

def listen_and_respond():
    ### ONE ###
    print("...")
    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src, duration=0.5)
        audio = r.listen(src)
        text = r.recognize_google(audio)
        print(text)
        print("Understanding and Processing")
        process(text)
    

    #### TWO ####
    # stream.start_stream()
    # # Use the stream object as a context manager
    # print("Listening...")
    # while True:
    #     # Read a chunk of data from the stream
    #     data = stream.read(chunk_size)
    #     # Check if the recognizer has a partial or final result
    #     if recognizer.AcceptWaveform(data):
    #         # Print the final result as JSON
    #         result = recognizer.Result()
    #         if result:
    #             print(f"You said: {result}")

    #             # Process the recognized command and generate a response
    #             process(input("Type: "))
    #         break
    #     else:
    #         # Print the partial result as JSON
    #         # print(recognizer.PartialResult())
    #         pass

    #### THREE ####
    # process(input("Type: "))

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
            except sr.UnknownValueError or sr.WaitTimeoutError:
                continue
            except Exception as e:
                if "timed out" in str(e):
                    continue
                print("Error:", e)
                speak("Error taking voice input")

    except KeyboardInterrupt:
        speak("Bye sir; Closing...")
        quit()

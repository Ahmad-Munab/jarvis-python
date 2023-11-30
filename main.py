# Import the libraries
import vosk
import pyaudio

from funcionality import process
from utils.voice_utils import speak

# Define the Vosk model path
model_path = "./vosk_models/vosk-model-en-us-0.22-lgraph"  # Replace with the actual path to your Vosk model

# Define the sample rate and the chunk size
sample_rate = 16000
chunk_size = 8000

# Initialize the Vosk recognizer
model = vosk.Model(model_path)
recognizer = vosk.KaldiRecognizer(model, sample_rate)

# Capture audio input from the microphone
pa = pyaudio.PyAudio()
# Use the pyaudio.open() method to create a stream object
stream = pa.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

def listen_and_respond():
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

    process(input("Type: "))

if __name__ == "__main__":
    speak("Hi sir, how are you doing?")
    while True:
        try:
            listen_and_respond()
        except KeyboardInterrupt:
            speak("Closing Jarvis")
            quit()

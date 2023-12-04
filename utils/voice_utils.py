import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', 'sapi5:Microsoft Sam',)
engine.setProperty('rate', 157) # (slower speech)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

def speak(text) -> None:
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen() -> str:      
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
                print(text, end=" ")
                return text

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

def ask(ques: str) -> str:
    try:
        speak(ques)
        return listen()
    except Exception as e:
        return f"Error: {e}"
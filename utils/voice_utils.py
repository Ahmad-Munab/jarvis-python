import pyttsx3
import speech_recognition as sr

# Text-to-Speech settings
engine = pyttsx3.init()
engine.setProperty('voice', 'sapi5:Microsoft Sam')
engine.setProperty('rate', 160) # (slower speech)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

# Speech-to-Text settings
recognizer = sr.Recognizer()
recognizer.non_speaking_duration = 0.3
recognizer.pause_threshold = 1
recognizer.phrase_threshold = -30


def speak(text) -> None:
    try:
        print(text)
        engine.say(text)
        engine.runAndWait()
    except KeyboardInterrupt:
        quit()
    except Exception as e:
        print(e)
        speak("There was an error")
        quit()

def listen() -> str:      
    with sr.Microphone() as source:
        while True:
            try:
                # Adjust for ambient noise
                # recognizer.adjust_for_ambient_noise(source, duration=0.5)
                # Listen for audio input

                audio = recognizer.listen(source)
                
                # Recognize the speech
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                # Process the recognized text
                print(text)
                return text
            # Handle errors if no speech is recognized
            except sr.UnknownValueError:
                return "loop"
            except sr.RequestError as e:
                print(f"Request Error: {e}")
                return "loop"
            except KeyboardInterrupt:
                quit()
            except Exception as e:
                if "timed out" in str(e):
                    return "loop"
                print("Error:", e)
                speak("Error taking voice input")
                quit()

def ask(ques: str) -> str:
    try:
        speak(ques)
        return listen()
    except Exception as e:
        return f"Error: {e}"
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', 'sapi5:Microsoft Sam')

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
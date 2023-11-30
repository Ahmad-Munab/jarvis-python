import os
import pywhatkit as kit
from utils.voice_utils import speak

def open_youtube():
    os.system("start https://youtube.com")

def search_on_youtube(sentence: str):
    sentence = sentence.lower()

    prefixes = [
                "search on YouTube about",
                "youTube search",
                "look up on YouTube",
                "find videos on",
                "query youtube for",
                "search youtube for",
                "find something on youtube about",
                "search for",
                "search about",
                "look up",
                "find information about",
                "query",
                "search",
                "find something about"
            ]
    
    for prefix in prefixes:
        if prefix in sentence:
            sentence = sentence.replace(prefix, "")
            break

    url = f"https://www.youtube.com/results?search_query={sentence.replace(' ', '+')}"
    try:
        os.system(f"start {url}")
    except Exception as e:
        print(f"Error: {e}")
        speak("Error fetchiing youtube")

def play_youtube_video(sentence: str):
    sentence = sentence.lower()

    prefixes = [
                "play a video on",
                "play a video about",
                "play a YouTube video on",
                "play a youtube video about",
                "find a video about",
                "show me a video about",
                "play a video related to",
            ]
    
    for prefix in prefixes:
        if prefix in sentence:
            sentence = sentence.replace(prefix, "")
            break

    try: 
        kit.playonyt(sentence)
    except Exception as e:
        print(f"Error: {e}")
        speak("Couldn't find a video to play")
import os
import pywhatkit as kit
from utils.voice_utils import speak
from utils.context import get
# from selenium import webdriver
import pygetwindow as gw
import time
import pyautogui as gui

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# driver = webdriver.Chrome(options=chrome_options, )


def open_youtube():
    os.system("start https://youtube.com")

def search_on_youtube(sentence: str):
    sentence = sentence.lower()

    prefixes = [
                "search on youtube about",
                "youTube search",
                "look up on youtube",
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
                "play a youTube video on",
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


def toggle_video(action):
    try:
        delay = 0  # Seconds
        time.sleep(delay)
        windows_to_activate = gw.getWindowsWithTitle("Brave") + gw.getWindowsWithTitle("Google Chrome")
        if len(windows_to_activate) == 0:
            return "No browser opened"
        for window in windows_to_activate:
            window.activate()
            tabs_dp = set()
            cwt = window.title
            while "- YouTube -" not in cwt:
                if cwt in tabs_dp:
                    tabs_dp = "DUP"
                    break
                tabs_dp.add(cwt)
                gui.hotkey("ctrl", "tab")
                cwt = gw.getActiveWindowTitle()
                time.sleep(delay)
            if tabs_dp == "DUP":
                continue
            gui.press("k")
            return action
        return "Youtube not opened"
    except Exception as e:
        return e

def toggle_youtube_video(sentence):
    sentence = sentence.lower()
    if any(word in sentence for word in ["play", "resume", "start", "continue"]):
        speak(toggle_video("Video Resumed"))
    elif any(word in sentence for word in ["pause", "stop", "hold"]):
        speak(toggle_video("Video Paused"))
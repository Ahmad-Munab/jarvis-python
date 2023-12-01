import os
import pywhatkit as kit
from utils.voice_utils import speak

from utils.context import get

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(options=chrome_options, )


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


def find_youtube_tab():
    cmnd_history = get("command_history")
    print(driver.current_url)
    if any(command in cmnd_history for command in ["open_youtube", "play_youtube_video", "search_on_youtube"]):
        speak("Youtube isn't open yet")
        return False
    try:
        if "https://www.youtube.com/watch?v=" in driver.current_url:
            return True
        
        tabs = driver.window_handles
        for tab in tabs:
            driver.switch_to.window(tab)
            print(driver.current_url)
            if "https://www.youtube.com/watch?v=" in driver.current_url:
                return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def toggle_youtube_video():
    try:
        if find_youtube_tab():
            play_button = driver.find_element_by_css_selector(".ytp-play-button")
            if "Play" in play_button.title:
                speak("Video continuing")
            elif "Pause" in play_button.title:
                speak("Video Paused")

            play_button.click()
    except Exception as e:
        print(f"Error: {e}")
        speak("Couldn't play/pause the video")
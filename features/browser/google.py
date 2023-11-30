import os
import pywhatkit as kit
from utils.voice_utils import speak


def open_google():
    os.system("start https://google.com")

def search_on_google(sentence: str):
    sentence = sentence.lower()

    prefixes = [
                "search in google",
                "search on google",
                "google search",
                "look up on google",
                "find information on",
                "find information about",
                "query foogle",
                "google",
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

    try: 
        kit.search(sentence.replace(' ', '+'))
    except Exception as e:
        print(f"Error: {e}")
        speak("Couldn't find anything")

def open_google_docs():
    os.system("start https://docs.google.com/document/u/1/")

def open_google_sheets():
    os.system("start https://docs.google.com/spreadsheets/u/1/")
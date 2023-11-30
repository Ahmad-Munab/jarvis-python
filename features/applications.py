# Define the functions for each command
import os
import subprocess

from utils.context import get
from features.browser.youtube import search_on_youtube
from features.browser.google import search_on_google

def search_anything(sentence):
    for i in get("commands_history")[::-1]:
        if "google" in i:
            search_on_google(sentence)
            return
        if "youtube" in i:
            search_on_youtube(sentence)
            return  
 
    search_on_google(sentence)
  


def open_chrome_browser():
    subprocess.run("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

def open_code_editor():
    os.system("code")

def open_chatgpt():
    os.system("start https://chat.openai.com/chat")

def open_notepad_editor():
    os.system("notepad")

def open_calendar_app():
    subprocess.run("start outlookcal:")

def open_command_prompt():
    os.system("start cmd")

def open_calculator_app():
    subprocess.run("calc")

def open_default_browser():
    os.system("start https://www.google.com")

def open_email_client():
    os.system("start https://mail.google.com/mail/u/1/#inbox")

def open_discord():
    os.system("start https://discord.com/channels/@me")

def open_facebook():
    os.system("start https://www.facebook.com/")

def start_google_meet():
    os.system("start https://meet.google.com/pzt-psqh-mxs?pli=1&authuser=1")

def open_github():
    os.system("start https://github.com/")


def open_camera_app():
    os.system("start microsoft.windows.camera:")

def open_photo_viewer():
    os.system("start microsoft.photos:")

def open_maps_app():
    os.system("start https://www.google.com/maps")

def open_clock_app():
    os.system("start ms-clock:")

def check_weather():
    # Functionality for checking weather (can be implemented based on requirements)
    pass

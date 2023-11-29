# Define the functions for each command
import os
import subprocess

def open_chrome_browser():
    subprocess.run("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

def open_code_editor():
    os.system("code")

def open_youtube():
    os.system("start https://youtube.com")

def open_google():
    os.system("start https://google.com")

def open_chatgpt():
    os.system("start https://chat.openai.com/chat")

def open_notepad_editor():
    os.system("notepad")

def open_calendar_app():
    subprocess.run("start outlookcal:")

def open_word_processor():
    subprocess.run("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

def open_excel_sheet():
    subprocess.run("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

def open_powerpoint_app():
    subprocess.run("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

def open_command_prompt():
    os.system("start cmd")

def open_calculator_app():
    subprocess.run("calc")

def open_default_browser():
    os.system("start https://www.google.com")

def open_email_client():
    subprocess.run("start outlook")

def open_camera_app():
    os.system("start microsoft.windows.camera:")

def open_photo_viewer():
    os.system("start microsoft.photos:")

def open_maps_app():
    os.system("start bingmaps:")

def open_clock_app():
    os.system("start ms-clock:")

def check_weather():
    # Functionality for checking weather (can be implemented based on requirements)
    pass

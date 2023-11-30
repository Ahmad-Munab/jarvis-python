from selenium import webdriver
import webbrowser
import pyautogui as gui

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(options=chrome_options)

print(webbrowser.open("https://github.com"))


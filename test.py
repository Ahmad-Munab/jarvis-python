
import pygetwindow as gw
import time
import pyautogui as gui

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

print(toggle_video("Pause video"))
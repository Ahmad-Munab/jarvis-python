import os
import time
from decouple import config

from utils.voice_utils import ask, speak
from utils.wrapper import fail_safe

def update_codebase(commit_msg, branch="munab"):
    delay = 0.1
    print("Adding files...")
    os.system(f"git add .")
    time.sleep(delay)
    
    print("Commiting changes...")
    os.system(f'git commit -m "{commit_msg}"')
    time.sleep(delay)
    
    print("Fetching updates...")
    os.system(f"git fetch")
    time.sleep(delay)
    
    print("Rebasing with main...")
    os.system(f"git rebase origin/main")
    time.sleep(delay)
    
    print("Pushing changes...")
    os.system(f"git push --force-with-lease origin {branch}")

    os.system(f"start {config('REPO_URL')}")

def update_jarvis_codebase():
    commit_msg = ask("What should be the commit message sir?")
    if "Error:" in commit_msg:
        print(commit_msg)
        speak("There was an error")
        return
    
    status = fail_safe(update_codebase, commit_msg)
    if status == 0:
        speak("Pushed to GitHub Successfully")
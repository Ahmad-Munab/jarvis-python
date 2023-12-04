import os
import time

def  update_jarvis_codebase(commit_msg, branch="munab"):
    delay = 0.1
    try:
        print("Adding files...")
        os.system(f"git add .")
        time.sleep(delay)
        
        print("Commiting changes...")
        os.system(f'git commit -m "{commit_msg}"')
        time.sleep(delay)
        
        # print("Swithing to your branch...")
        # os.system(f"git checkout -b {branch}")
        # time.sleep(delay)
        
        print("Fetching updates...")
        os.system(f"git fetch")
        time.sleep(delay)
        
        print("Rebasing with main...")
        os.system(f"git rebase origin/main")
        time.sleep(delay)
        
        print("Pushing changes...")
        os.system(f"git push --force-with-lease origin {branch}")
    except Exception as e:
        print(f"Error: {e}")


update_jarvis_codebase("Testing 2")


import os
import time

def  update_jarvis_codebase(commit_msg, branch="munab"):
    try:
        print("Adding files...")
        os.system(f"git add .")
        time.sleep(0.5)
        
        print("Committing changes...")
        os.system(f"git commit -m {commit_msg}")
        time.sleep(0.5)
        
        # print("Creating new branch...")
        # os.system(f"git checkout -b {branch}")
        # time.sleep(2)
        
        print("Fetching updates...")
        os.system(f"git fetch")
        time.sleep(0.5)
        
        print("Rebasing with main...")
        os.system(f"git rebase origin/main")
        time.sleep(0.5)
        
        print("Pushing changes...")
        os.system(f"git push --force-with-lease origin {branch}")
        
    except Exception as e:
        print(f"Error: {e}")


update_jarvis_codebase("Testing ")


import os
import time
import subprocess

def  update_jarvis_codebase(commit_msg, branch="munab"):
    delay = 0.1
    try:
        print("Adding files...")
        os.system(f"git add .")
        time.sleep(delay)
        
        print("Commiting changes...")
        os.system(f"git commit -m {commit_msg}")
        time.sleep(delay)
        
        # print("Swithing to your branch...")
        # os.system(f"git checkout -b {branch}")
        # time.sleep(2)
        
        print("Fetching updates...")
        os.system(f"git fetch")
        time.sleep(delay)
        
        print("Rebasing with main...")
        os.system(f"git rebase origin/main")
        time.sleep(delay)
        
        print("Pushing changes...")
        result = subprocess.run(f"git push --force-with-lease origin {branch}", capture_output=True, text=True, shell=True)
        output = result.stdout.strip()
        url_start = output.find('https://')
        url_end = output.find('.git')
        repo_url = output[url_start:url_end + 4]
        os.system(f"start {repo_url}")
        return "Pushed to successfully"
    except Exception as e:
        return f"Error: {e}"
    
update_jarvis_codebase("Testing ")






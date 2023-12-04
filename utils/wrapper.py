from utils.voice_utils import speak

def fail_safe(func, *args) -> int:
    try:
        func(*args)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        speak(f"There was an error executing {func}")
        return 1
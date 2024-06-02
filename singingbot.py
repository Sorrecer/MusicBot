import pyautogui
import keyboard
import time

# Lyrics to be sung
lyrics = [
  "We don't talk anymore",
    "We don't talk anymore",
    "We don't talk anymore",
    "Like we used to do",
]

# Function to type out lyrics line by line
def sing_lyrics():
    for line in lyrics:
        # Wait for the hotkey to be pressed
        keyboard.wait('`')

        pyautogui.press('enter')
        # Type the line
        pyautogui.typewrite(':musical_note: ')
        pyautogui.typewrite(line)
        pyautogui.typewrite(' :musical_note:')
        # Press enter
        pyautogui.press('enter')
        # Adding a short delay to avoid potential issues with rapid inputs
        time.sleep(0.1)

if __name__ == "__main__":
    print("Ready to sing! Press '``' to start typing each line of the lyrics.")
    sing_lyrics()

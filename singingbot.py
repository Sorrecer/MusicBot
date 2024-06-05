import pyautogui
import keyboard
import time

output_file = 'D:/xampp/htdocs/MusicBot/input_lyrics.txt'

# Function to read lyrics from file
def read_lyrics(file_path):
    try:
        with open(file_path, 'r') as file:
            lyrics = [line.strip() for line in file]
        return lyrics
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

# Lyrics to be sung
lyrics = read_lyrics(output_file)


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

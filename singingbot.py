import pyautogui
import keyboard
import time
import re  # Import regex module for word matching and replacing

output_file = 'D:/xampp/htdocs/MusicBot/input_lyrics.txt'
words_file = 'D:/xampp/htdocs/MusicBot/badwordsenter.txt'

def read_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []
    
# Function to read lyrics from file
def read_lyrics(file_path):
    try:
        with open(file_path, 'r') as file:
            lyrics = [line.strip() for line in file]
        return lyrics
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

# Function to censor specific words in a line
def censor_words(line, words):
    # Use regular expression to replace words with asterisks
    for word in words:
        line = re.sub(rf'\b{word}\b', '*' * len(word), line, flags=re.IGNORECASE)
    return line

# Read the words and lyrics
words = read_words(words_file)
lyrics = read_lyrics(output_file)

censor = True

# Function to type out lyrics line by line
def sing_lyrics():
    for line in lyrics:
        # Censor words in the current line
        if censor == True :
            censored_line = censor_words(line, words)
        else : 
            censored_line = line
        # Wait for the hotkey to be pressed
        keyboard.wait('`')

        pyautogui.press('enter')
        # Type the line
        # pyautogui.typewrite(':musical_note: ')
        pyautogui.typewrite(censored_line)
        # pyautogui.typewrite(' :musical_note:')
        # Press enter
        pyautogui.press('enter')
        # Adding a short delay to avoid potential issues with rapid inputs
        time.sleep(0.1)

if __name__ == "__main__":
    print("Ready to sing! Press '``' to start typing each line of the lyrics.")
    sing_lyrics()

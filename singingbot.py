import pyautogui
import keyboard
import time

# Lyrics to be sung
lyrics = [
    "Dream",
    "Just dream",
    "Long ago, long ago, long ago",
    "Dream",
    "Just dream",
    "Dream",
    "Are we still friends",
    "Can we be friends",
    "Are we still friends",
    "I've got to kn- know",
    "If we can see each other",
    "Shake your hand, say hi",
    "Long ago, long ago, long ago",
    "I can't stop you, I can't rock too",
    "I've been back there and I can not die too",
    "But I've got to know",
    "Are we still friends? Can we be friends?",
    "Are we still friends? Can we be- (can we be friends?)",
    "Are we still friends? Can we be friends? (Yeah)",
    "Are we still friends?",
    "Are we still friends? Are we still friends?",
    "Are we still friends? Are we still friends?",
    "Are we still friends? (Friends, friends)",
    "I said, are we still friends? (Friends, friends)",
    "Are we still friends? (Friends, friends, friends, friends, friends)",
    "Don't get green skin (green skin), keep contact (keep contact)",
    "Don't say, 'Goodbye, smell you later' (bye, later)",
    "Nah, I can't",
    "I don't want to end this season on a bad episode, nigga, nah",
    "Bouncing off things and you don't know how you fall",
    "Your power is drained, so you cannot go through walls",
    "You're caught in this matrix, don't know where you play it",
    "You hate it, it could be your favorite if you make it your friend",
    "Are we still friends? (This can't end)",
    "Are we still friends? Are we still friends? (I still wanna say hi)",
    "Are we, are we, are we, are we still friends?",
    "Oh whoa",
    "Can't say goodbye (check it, ahh)",
    "Can't say goodbye, goodbye (woo)"
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

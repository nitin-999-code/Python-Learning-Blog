import time
import random
import sys
import os

# Terminal colors
colors = {
    "calm": ["\033[36m", "\033[96m", "\033[34m"],       # cyan shades
    "happy": ["\033[33m", "\033[93m", "\033[32m"],     # yellow-green
    "sad": ["\033[94m", "\033[34m", "\033[90m"],       # blue-gray
    "angry": ["\033[31m", "\033[91m", "\033[33m"],     # red-yellow
    "mysterious": ["\033[35m", "\033[95m", "\033[30m"],# purple-dark
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def animate_colors(mood: str):
    if mood not in colors:
        print("\033[0mUnknown mood! Try calm, happy, sad, angry, or mysterious.")
        return

    mood_colors = colors[mood]
    print(f"\033[1mMood detected: {mood.capitalize()} 🎭\033[0m\n")
    
    try:
        for _ in range(80):
            color = random.choice(mood_colors)
            pattern = "".join(random.choice("░▒▓█") for _ in range(40))
            print(color + pattern + "\033[0m")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n\033[0mExited animation.")
    finally:
        print("\n\033[1;37mColor Whisper ended.\033[0m")

if __name__ == "__main__":
    clear()
    print("\033[1;37mWelcome to Color Whisper 🌈\033[0m")
    print("Tell me your mood (calm, happy, sad, angry, mysterious):")
    mood = input("→ ").strip().lower()
    clear()
    animate_colors(mood)

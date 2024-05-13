# Hangman Game in Python
This repository contains a Python implementation of the classic word-guessing game Hangman. The game was developed by Yael Dinar as part of the self.py course offered by CampusIL.

## Game Description

Hangman is a straightforward yet engaging word guessing game where a player tries to figure out a hidden word by guessing letters. For each incorrect guess, a part of the hangman is drawn. The game ends when either the entire word is revealed or the hangman is fully drawn, indicating a loss. This particular implementation brings additional flair to the traditional game with visual and sound enhancements.

## Features

- **Visual Hangman States**: Displays progressive hangman states depending on the number of incorrect guesses.
- **Colorful Display**: Uses ANSI colors to represent different stages of the game, enhancing visual feedback.
- **Sound Effects**: Incorporates sound effects to signal game start, win, and loss events, adding an immersive experience.
- **Dynamic Word Selection**: Allows the player to input a path to a text file and choose a word based on an index, providing customizable gameplay.

## Requirements

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **playsound Library**: Required for playing sound effects.
- **winsound Library**: Utilized for sound playback on Windows systems.

### Installation of Dependencies

Before running the game, make sure to install the necessary Python library:
```bash
pip install playsound
```
### Setup
Clone this repository to your local machine using the command:
Navigate to the Project Directory, Change into the project directory
```bash
cd hangman
```
Install Dependencies:
Install the necessary Python libraries as described above.

### How to Run the Game
To run the game, follow these steps:

Start the Game:
Run the script using Python from the terminal:
```bash
python hangman.py
```
Follow On-Screen Prompts:
The game will guide you through entering the path to a text file containing potential secret words and choosing an index number to select a word.


### Description of each file:
- HangMan 10.py - the main code of the game
- HangMan_Words.txt -  the optional words list. it can be modified and you can you other file for words (in the game you enter the words file path so any txt file that is the shape of this file will do).
- mixkit-bonus-extra-in-a-video-game-2064 - Game Start Sound
- mixkit-long-game-over-notification-276 - Losing Game Sound
- mixkit-winning-an-extra-bonus-2060 - Winning Game Sound


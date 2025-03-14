
---

# Number Guessing Game

## Overview
This is a fun and interactive **Number Guessing Game** built using Python's **Tkinter** library. The game asks the player to guess a secret number between 1 and 1000. The player will receive hints if their guesses are too high or too low. The game tracks the number of attempts and stores game history in a CSV file. The player can also view the secret number at any time by clicking the "Show Answer" button.

## Features
- **Interactive UI**: Built with Python's Tkinter library for a user-friendly interface.
- **Game Flow**: Player inputs their name and starts guessing a secret number between 1 and 1000.
- **Hint System**: Provides hints on whether the guess is too high or too low.
- **Attempts Tracking**: Displays the number of attempts taken by the player.
- **History Tracking**: Saves game history (player's name, secret number, guesses, and attempts) to a CSV file for future reference.
- **Show Answer**: Option to view the secret number at any point in the game.
- **Restart Game**: After guessing correctly, the game automatically restarts.

## Getting Started
To run the game on your local machine, follow the instructions below.

### Prerequisites
- **Python 3.x**: Make sure you have Python installed.
- **Tkinter**: Tkinter should be installed with Python by default. If it's not installed, you can install it using your package manager.

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Thinpm/data-visualization.git
   ```
   
2. Navigate into the project directory:
   ```bash
   cd number-guessing-game
   ```

3. If necessary, install Tkinter (usually comes with Python):
   ```bash
   sudo apt-get install python3-tk
   ```

4. Run the game by executing the following command:
   ```bash
   python game.py
   ```

## How to Play
1. **Enter Player's Name**: Type your name in the provided field and click "Start Game".
2. **Make a Guess**: Enter your guess for the secret number and click "Guess". The game will tell you if your guess is too high or too low.
3. **Track Your Progress**: The number of attempts and a list of your guesses will be displayed.
4. **Show Answer**: At any point, you can click "Show Answer" to reveal the secret number.
5. **Victory**: Once you guess the number correctly, you will be congratulated and the game will automatically start a new round.

## Game History
The game history is stored in a file named `history.csv`. Each record in the file contains:
- **Player Name**
- **Secret Number**
- **Guessed Numbers**
- **Attempts Taken**

### Example:
```csv
Player Name,Secret Number,Guessed Numbers,Attempts
John,345,[100, 500, 200, 345],4
```

## Customization
You can modify the secret number range, colors, and fonts in the `game.py` file to tailor the game to your preferences.

## Future Improvements
- **Difficulty Levels**: Add options for easy, medium, and hard difficulty levels with varying number ranges.
- **Leaderboard**: Display the top players with the fewest attempts.
- **Time Tracking**: Track how long it takes to guess the number.

## Acknowledgments
- The game is built using **Tkinter** for the graphical user interface.
- The **random** library is used to generate the secret number.

---


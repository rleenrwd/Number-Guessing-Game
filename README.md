# Number Guessing Game
## By Robert L. Norwood
A Python-based command-line game where players attempt to guess a randomly generated number between 1 and 100. The game provides feedback on whether the guess is too high or too low, offering an engaging way to practice programming fundamentals.

## 🎮 How to Play
The game will generate a random number between 1 and 100.

You will be prompted to guess the number.

After each guess, the game will inform you if your guess is too high, too low, or correct.

The game continues until you guess the correct number.

## 🚀 Features
Random Number Generation: The game selects a random number within the specified range.

User Input Handling: Accepts and validates user input to ensure it's a number within the range.

Feedback Mechanism: Provides hints whether the guess is too high or too low.

Replay Option: Allows the player to play multiple rounds without restarting the program.

## 🧪 Requirements
Python 3.x

## 🧑‍💻 How to Run
Clone this repo:

git clone https://github.com/rleenrwd/number-guessing-game.git
cd number-guessing-game

Run the game with: 

python main.py

## 🧪 Testing
This project includes automated test cases written using Python’s built-in unittest framework.

To run the tests:

python -m unittest test_main.py

These tests check the following:

Validating input and user guesses

Checking that the guess is within the specified range (1–100).

Game logic correctness (e.g., too high, too low, correct guess)

## 🧠 What I Learned
Enhanced understanding of Python's random module for generating random numbers.

Improved skills in handling user input and providing real-time feedback.

Developed a simple yet engaging command-line game, reinforcing programming fundamentals.

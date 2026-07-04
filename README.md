# Number Guessing Game

A simple command-line number guessing game built with Python as part of the roadmap.sh Number Guessing Game project.

**Project URL:** https://roadmap.sh/projects/number-guessing-game

---

## About the Project

In this game, the computer randomly selects a number between **1 and 100**. Your goal is to guess the correct number before you run out of attempts.

You can choose between three difficulty levels, each providing a different number of guesses. After every incorrect guess, the game lets you know whether the secret number is higher or lower than your guess.

The game also validates user input and allows you to play multiple rounds without restarting the program.

---

## Features

- Random number generation
- Three difficulty levels
- Input validation
- Higher/Lower hints
- Limited number of attempts
- Option to play again after each game

---

## Technologies Used

- Python 3
- `random` module

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/pvllo/number-guessing-game.git
```

Go to the project directory:

```bash
cd number-guessing-game
```

Run the program:

```bash
python Number_Guessing_Game.py
```

---

## How to Play

1. Launch the program.
2. Select a difficulty level.
3. Enter a number between **1** and **100**.
4. Read the hint after each incorrect guess.
5. Keep guessing until you find the correct number or run out of attempts.
6. Choose whether you want to play another round.

---

## Project Structure

```
number-guessing-game/
│
├── Number_Guessing_Game.py
└── README.md
```

---

## Future Improvements

- Add a scoring system.
- Display the remaining attempts after each guess.
- Allow players to customize the range of numbers.
- Save the best score.

---

## Author

Created by **pvllo**.

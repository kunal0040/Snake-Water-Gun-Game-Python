# Snake, Water, Gun Game

A command-line implementation of the classic "Snake, Water, Gun" game (a variation of Rock, Paper, Scissors) written in Python. This is my very first Python project, built to practice core programming fundamentals!

## 🎮 Game Rules
* **Snake** beats **Water** (Snake drinks water)
* **Gun** beats **Snake** (Gun shoots snake)
* **Water** beats **Gun** (Water douses gun)
* If both players make the same choice, it results in a tie.

## 🚀 Features
* **Best of 3 Format:** Tracks user and computer scores across multiple rounds.
* **Input Validation:** Handles incorrect user entries gracefully without crashing.
* **Dynamic Commentary:** Includes randomized victory words and unique Easter eggs for multiple tie rounds.

## 🛠️ Concepts Practiced
* Using the `random` module for AI choices and varied text output.
* Managing game state with Python dictionaries (`choices` and `reversechoices`).
* Control flow using `while` loops and nested `if-elif-else` statements.

## 📦 How to Run
1. Ensure you have Python installed.
2. Run the script using your terminal:
   ```bash
   python main.py
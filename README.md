# 🎮 Python Wordle Clone

A CLI (Command Line Interface) implementation of the popular word guessing game "Wordle", developed in Python.

## 🚀 Overview
This project replicates the core logic of Wordle within a terminal environment. The game selects a secret word from a database, and the user has 6 attempts to guess it. The algorithm provides real-time feedback on the accuracy of each letter.

## ✨ Key Features
* **Input Validation:** Ensures the user enters a valid 5-letter word that exists in the database.
* **Smart Feedback System:**
    * 🟢 **Green:** Correct letter in the correct position.
    * 🟡 **Yellow:** Correct letter but in the wrong position.
    * ⚪ **Gray:** Letter not in the word.
* **Duplicate Letter Handling:** The logic correctly handles words with repeated letters (e.g., "APPLE") using a frequency counter, ensuring the feedback priorities (Green > Yellow) work perfectly.
* **File I/O:** Reads the vocabulary dynamically from an external text file.

## 🛠️ How to Run

1.  **Prerequisites:** Ensure you have Python 3.x installed.
2.  **Files:** Make sure both `Wordle.py` and `wordList.txt` are in the same directory.
3.  **Run the Game:**
    Open your terminal/command prompt and run:
    ```bash
    python Wordle.py
    ```

## 🧩 How It Works (Code Logic)
1.  The program reads `wordList.txt` and selects a random `the_word`.
2.  It enters a `while` loop allowing a maximum of 6 attempts.
3.  For every guess, it creates a frequency map of the secret word to manage duplicate letters.
4.  **First Pass:** Checks for exact matches (Green) and decrements the counter.
5.  **Second Pass:** Checks for misplaced letters (Yellow) based on the remaining counts.
6.  The result is printed to the console.

## 📂 Project Structure
* `Wordle.py`: The main game script.
* `wordList.txt`: A text file containing valid 5-letter words (Required for the script to run).

---
**Author:** Enes Uzun

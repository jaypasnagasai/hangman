# Hangman

This is a simple command-line Hangman game implemented in Python. The game allows players to guess words within a time limit and awards points based on correct guesses.

# Requirements

Python 3.x

# Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:
   `python hangman.py`
5. Follow the instructions provided by the game to play.

# Gameplay

1. Enter the number of times you want to play when prompted.
2. Enter the time limit (in seconds) for each game.
3. For each game, enter the number of words you want to include.
4. Enter each word one by one.
5. The game will start, and you need to guess letters to form the word.
6. You have a limited number of tries (6 by default) to guess the word correctly.
7. If you guess a letter that is in the word, it will be revealed in the correct position(s).
8. If you guess a letter not in the word, you will lose a try.
9. The game ends when you guess the word correctly, run out of tries, or exceed the time limit.
10. After each game, you will receive a score based on the number of correct guesses.
11. The game will display the word, elapsed time, and final score.

# Customization

You can modify the following aspects of the game to customize it according to your preferences:

1. Number of tries: The default is six tries per word. You can modify the tries variable in the `play_hangman` function.
2. Time limit: The default time limit is set in seconds. You can change it by modifying the `time_limit` variable when prompted.

Feel free to experiment and modify the code to add more features or enhance the gameplay. Have fun playing Hangman!

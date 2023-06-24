import random
import time

def get_word_list():
    word_list = []
    num_words = int(input('Enter the number of words: '))
    for i in range(num_words):
        word = input(f'Enter word {i+1}: ')
        word_list.append(word)
    return word_list

def choose_word(word_list):
    return random.choice(word_list)

def increase_difficulty(word_list):
    new_word_list = []
    for word in word_list:
        new_word = word.upper()
        new_word_list.append(new_word)
    return new_word_list

def play_hangman(time_limit, word_list):
    word_list = increase_difficulty(word_list)
    word = choose_word(word_list)
    guessed_letters = []
    tries = 6
    score = 0
    start_time = time.time()

    print(f'Welcome to Hangman! You have {time_limit} seconds to guess the word.')

    while tries > 0:
        guessed_word = ''
        for letter in word:
            if letter.lower() in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += '_'

        print(f'Word: {guessed_word}')
        print(f'Tries left: {tries}')
        guess = input('Enter a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed that letter. Try again.')
        elif guess in word.lower():
            print('Correct guess!')
            guessed_letters.append(guess)
            score += 1
        else:
            print('Wrong guess!')
            tries -= 1

        if set(word.lower()) == set(guessed_letters):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print('Congratulations! You guessed the word.')
            print('The word was:', word)
            print('Time elapsed:', elapsed_time, 'seconds.')
            print('Your score:', score)
            return

        if time.time() - start_time > time_limit:
            print('Time limit exceeded. Game over.')
            print('Your score:', score)
            return

    print('You ran out of tries. The word was:', word)
    print('Your score:', score)

# Start the game
num_games = int(input('Enter the number of times you want to play: '))
time_limit = int(input('Enter the time limit (in seconds): '))

for game in range(num_games):
    print(f'\n----- Game {game+1} -----')
    word_list = get_word_list()
    play_hangman(time_limit, word_list)




  
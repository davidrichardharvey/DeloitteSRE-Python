import random
from hangman_words import word_list


def select_random_word():
    # return random.choice(word_list)
    return word_list[0]

# print(select_random_word())

# Where letters appear in a word
# Length of a word
# Take input
# Check if letter already been guessed

word = 'CODSWALLOP'

def find_letters_in_word(letter_guess, word):
    letter_positions = []
    for index, char in enumerate(word):
        if char == letter_guess:
            letter_positions.append(index)
    return letter_positions

board = '_' * len(word)
print(board)

def process_guess(letter, word, board):
    positions = find_letters_in_word(letter, word)
    for p in positions:
        board = board[:p] + letter + board[p+1:]
    return board

board = process_guess('L', word, board)
print(board)
board = process_guess('O', word, board)
print(board)
board = process_guess('X', word, board)
print(board)
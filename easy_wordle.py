# CSCI 1913
# 03/17/23
# Author: John Van Sloun

import random
import display_utility
from words import words
from wordle import check_word


def filter_word_list(words, clues):
    """

    Args:
        words: A list of valid wordle words.
        clues: A list of tuples that contain the current guesses and the subsequent clue given to each guess.

    Returns: a new list of words containing only words that could be the secret word.

    """

    potential_words = []

    if len(clues) == 0:
        return words.copy()

    for word in words:
        for i in range(len(clues)):
            if check_word(word, clues[i][0].lower()) != clues[i][1]:
                break
            elif i == (len(clues) - 1):
                potential_words.append(word)

    return potential_words


if __name__ == "__main__":

    secret_word = words[random.randint(0, len(words))]
    clues_list = []

    for i in range(6):
        guess = input("> ")
        while (guess not in words) or (len(guess) != 5):
            guess = input("> ")

        clues_list.append((guess, check_word(secret_word, guess)))

        for clue in clues_list:
            for j in range(len(clue[1])):
                if clue[1][j] == "green":
                    display_utility.green(clue[0][j].upper())
                elif clue[1][j] == "yellow":
                    display_utility.yellow(clue[0][j].upper())
                elif clue[1][j] == "grey":
                    display_utility.grey(clue[0][j].upper())

            print()

        possible_words = filter_word_list(words, clues_list)

        print(str(len(possible_words)) + " words possible:")

        if len(possible_words) >= 5:
            for m in range(5):
                print(possible_words[random.randint(0, len(possible_words) - 1)])
        else:
            for n in range(len(possible_words)):
                print(possible_words[n])

        if guess == secret_word:
            break

    print("Answer: " + secret_word.upper())

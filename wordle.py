# CSCI 1913
# 03/17/23
# Author: John Van Sloun
import random
from words import words
import display_utility

def find_num_repeats(word):
    """

    Args:
        word: A five letter string.

    Returns: A dictionary where the keys are the letters present in the word and the value is the number of times that
             letter appears in the word.

    """

    letter_count = {}

    for letter in word:
        if letter in letter_count.keys():
            letter_count[letter] = letter_count[letter] + 1
        else:
            letter_count[letter] = 1

    return letter_count

def has_repeats(word):
    """

    Args:
        word: A five letter string.

    Returns: A boolean value, true if the word contains repeats of letters and false otherwise.

    """
    dict = find_num_repeats(word)
    for i in dict.keys():
        if dict[i] > 1:
            return True

    return False

def no_repeats_yellow_and_grey(secret, guess, index):
    """

    Args:
        secret: 5-letter secret wordle word
        guess: 5-letter word guess from user
        index: The index of the letter of the guess currently being checked.

    Returns: returns yellow if the letter is present in the secret word but not at the index being checked and
             grey if the letter is not present in the secret word.

    """
    if (guess[index] in secret) and (guess[index] != secret[index]):
        return "yellow"
    else:
        return "grey"

def excess_repeats_yellow_and_grey(secret, guess, index, clues):
    """

    Args:
        secret: 5-letter secret wordle word
        guess: 5-letter word guess from user
        index: The index of the letter of the guess currently being checked.
        clues: A list of strings (green, yellow, grey, or an empty string) indicating the letter in the guess is
               in the same place as in the secret word, the letter at the index is not in the same place as in the
               secret but is in the secret word, the letter at the index is not in the secret word,
               or the nature of the letter is unknown.

    Returns: Yellow if the letter is present in the secret word but not in the right spot and is not an excess guess or
             grey if the letter is not in the secret word or is an excess guess.

    """
    num_times_accounted = 1

    for i in range(len(guess)):
        if (i < index) and (guess[i] == guess[index]) and (clues[i] == "green" or clues[i] == "yellow"):
            num_times_accounted = num_times_accounted + 1
        elif (i > index) and (guess[i] == guess[index]) and (clues[i] == "green"):
            num_times_accounted = num_times_accounted + 1

    if num_times_accounted <= find_num_repeats(secret)[guess[index]]:
        return "yellow"
    else:
        return "grey"


def check_word(secret, guess):
    """

    Args:
        secret: 5-letter secret wordle word
        guess: 5-letter word guess from user

    Returns: A length-5 list of strings which can be green indicating a correct guess of letter placement,
             yellow indicating the existence of the letter in the word but wrong placement,
             or grey indicating the letter not being present in the word.

    """

    clues = ["", "", "", "", ""]

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues[i] = "green"


    for j in range(len(guess)):
        if (clues[j] != "green") and (find_num_repeats(guess)[guess[j]] > 1) and (guess[j] in secret):
            clues[j] = excess_repeats_yellow_and_grey(secret, guess, j, clues)
        elif clues[j] != "green":
            clues[j] = no_repeats_yellow_and_grey(secret, guess, j)

    return clues


def known_word(clues_list):
    """

    Args:
        clues_list: A list of tuples that contain the current guesses and the subsequent clue given to each guess.

    Returns: A string indicating the letters that are known to be in the right position.
             Where the letters are not known is represented with a _.
             Where the letter is known is represented with the letter.

    """

    known_word_chars = ["_", "_", "_", "_", "_"]

    for i in range(len(clues_list)):
        for j in range(5):
            if clues_list[i][1][j] == "green":
                known_word_chars[j] = clues_list[i][0][j].upper()

    return known_word_chars

def yes_letters(clues_list):
    """

    Args:
        clues_list: A list of tuples that contain the current guesses and the subsequent clue given to each guess.

    Returns: A string containing letters that have been confirmed to be in the secret word
             regardless of whether they were in the right position.

    """
    yes_letters_set = set()

    for i in range(len(clues_list)):
        for j in range(5):
            if clues_list[i][1][j] == "green" or clues_list[i][1][j] == "yellow":
                yes_letters_set.add(clues_list[i][0][j])

    yes_letters_list = list(yes_letters_set)

    for k in range(len(yes_letters_list)):
        yes_letters_list[k] = yes_letters_list[k].upper()

    yes_letters_list.sort()

    return yes_letters_list

def no_letters(clues_list):
    """

    Args:
        clues_list: A list of tuples that contain the current guesses and the subsequent clue given to each guess.

    Returns: A string containing letters that have been guessed and are known to not be in the string.

    """
    yes_letters_list = yes_letters(clues_list)
    no_letters_set = set()

    for i in range(len(clues_list)):
        for j in range(5):
            if clues_list[i][1][j] == "grey" and (clues_list[i][0][j].upper() not in yes_letters_list):
                no_letters_set.add(clues_list[i][0][j])

    no_letters_list = list(no_letters_set)

    for k in range(len(no_letters_list)):
        no_letters_list[k] = no_letters_list[k].upper()

    no_letters_list.sort()

    return no_letters_list


if __name__ == "__main__":

    secret_word = words[random.randint(0, len(words)-1)]
    first_clue = check_word(secret_word, "")
    clues_list = []

    print("Known: _____")
    print("Green/Yellow Letters:")
    print("Grey Letters:")
    for i in range(6):
        guess = input("> ")
        while (guess not in words) or (len(guess) != 5):
            guess = input("> ")

        if guess == secret_word:
            break

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

        print()

        print("Known: " + "".join(known_word(clues_list)))
        print("Green/Yellow Letters: " + "".join(yes_letters(clues_list)))
        print("Grey Letters: " + "".join(no_letters(clues_list)))

    print(secret_word.upper())


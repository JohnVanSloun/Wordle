import words
import display_utility


def find_num_repeats(word):
    """

    Args:
        word: A five letter string.

    Returns: A set of the repeated letters found withing the word.

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
    if (guess[index] in secret) and (guess[index] != secret[index]):
        return "yellow"
    else:
        return "grey"

def excess_repeats_yellow_and_grey(secret, guess, index, clues):
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


def known_word(clues):
    """

    Args:
        clues: A list of tuples that contain the current guesses and the subsequent clue given to each guess.

    Returns: A string indicating the letters that are known to be in the right position.
             Where the letters are not known is represented with a _.
             Where the letter is known is represented with the letter.

    """
    pass


def no_letters(clues):
    """

    Args:
        clues: A list of tuples that contain the current guesses and the subsequent clue given to each guess.

    Returns: A string containing letters that have been guessed and are known to not be in the string.

    """
    pass


def yes_letters(clues):
    """

    Args:
        clues: A list of tuples that contain the current guesses and the subsequent clue given to each guess.

    Returns: A string containing letters that have been confirmed to be in the secret word
             regardless of whether they were in the right position.

    """
    pass


if __name__ == "__main__":
    pass

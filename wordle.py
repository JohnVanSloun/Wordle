import words
import display_utility


def has_repeats(word):
    """

    Args:
        word: A five letter string.

    Returns: A boolean value, true if the word contains repeasts of letters and false otherwise.

    """
    return len(find_repeats()) > 0

def find_repeats(word):
    """

    Args:
        word: A five letter string.

    Returns: A set of the repeated letters found withing the word.

    """

    repeats = set()
    letter_count = {}

    for letter in word:
        if letter in letter_count.keys():
            letter_count[letter] = letter_count[letter] + 1
            if letter_count[letter] > 1:
                repeats.add(letter)
        else:
            letter_count[letter] = 1

    return repeats


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

    if has_repeats(guess):
        # Using set difference to find words repeated in guess that are not repeated in secret
        not_repeated_in_secret = find_repeats(guess) - find_repeats(secret)
        pass
    else:
        pass


    pass


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

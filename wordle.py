import words
import display_utility


def check_word(secret, guess):
    """

    Args:
        secret: 5-letter secret wordle word
        guess: 5-letter word guess from user

    Returns: A length-5 list of strings which can be green indicating a correct guess of letter placement,
             yellow indicating the existence of the letter in the word but wrong placement,
             or grey indicating the letter not being present in the word.

    """
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

import words
import display_utility


def has_repeats(word):
    """

    Args:
        word: A five letter string.

    Returns: A boolean value, true if the word contains repeasts of letters and false otherwise.

    """
    return len(find_repeats(word)) > 0

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

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues[i] = "green"

    if has_repeats(guess):
        not_repeated_in_secret = find_repeats(guess) - find_repeats(secret)

        for j in range(len(guess)):
            if (guess[j] in not_repeated_in_secret) and (guess[j] in secret) and (clues[j] != "green"):
                if guess[j] not in secret[:j]:
                    clues[j] = "yellow"
                else:
                    clues[j] = "grey"
            else:
                if (guess[j] in secret) and (guess[j] != secret[j]):
                    clues[j] = "yellow"
                elif guess[j] not in secret:
                    clues[j] = "grey"
    else:
        for k in range(len(guess)):
            if (guess[k] in secret) and (guess[k] != secret[k]):
                clues[k] = "yellow"
            elif guess[k] not in secret:
                clues[k] = "grey"

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

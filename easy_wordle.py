import display_utility
import words
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
            if check_word(word.upper(), clues[i][0]) != clues[i][1]:
                break
            elif i == (len(clues) - 1):
                potential_words.append(word)

    return potential_words


if __name__ == "__main__":
    pass
# CSCI 1913
# 03/17/23
# Author: John Van Sloun

import easy_wordle
import wordle
from words import words

# find_repeats tests
#
# print(wordle.find_num_repeats("check"))
# print(wordle.find_num_repeats("teeth"))
# print(wordle.find_num_repeats("books"))
# print(wordle.find_num_repeats("gamer"))
#
# # has_repeats tests
#
# print(wordle.has_repeats("check"))
# print(wordle.has_repeats("teeth"))
# print(wordle.has_repeats("books"))
# print(wordle.has_repeats("gamer"))
#
# # no_repeats_yellow_and_grey tests
#
# print(wordle.no_repeats_yellow_and_grey("stork", "steam", 2))
#
# # excess_repeats_yellow_and_grey tests
#
# clues = ["green", "green", "green", "", ""]
# print(wordle.excess_repeats_yellow_and_grey("cooks", "cooko", 2, clues))
#
# # check_word tests
#
# print(wordle.check_word("chair", "check"))
# print(wordle.check_word("methe", "teeth"))
# print(wordle.check_word("chair", "books"))
# print(wordle.check_word("chair", "gamer"))
# print(wordle.check_word("cohoe", "cooks"))
# print(wordle.check_word("books", "cooko"))
# print(wordle.check_word("books", "tasch"))
# print(wordle.check_word("books", "ooooo"))

# known_word
# print(wordle.known_word([("books", ["green", "grey", "green", "green", "grey"]), ("brike", ["green", "green", "grey", "green", "green"])]))

# yes_letters
#broke
# print(wordle.yes_letters([("books", ["green", "grey", "green", "green", "grey"]), ("brike", ["green", "green", "grey", "green", "green"])]))

# no_letters
# print(wordle.no_letters([("books", ["green", "grey", "green", "green", "grey"]), ("brike", ["green", "green", "grey", "green", "green"])]))

# filtered_list
print(easy_wordle.filter_word_list(words, [("books", ["green", "grey", "green", "green", "grey"]), ("brike", ["green", "green", "grey", "green", "green"])]))

print(easy_wordle.filter_word_list(words, [("books", ["green", "green", "grey", "grey", "grey"])]))



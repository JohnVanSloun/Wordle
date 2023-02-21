import wordle

# find_repeats tests
#
# print(wordle.find_repeats("check"))
# print(wordle.find_repeats("teeth"))
# print(wordle.find_repeats("books"))
# print(wordle.find_repeats("gamer"))
#
# has_repeats tests
#
# print(wordle.has_repeats("check"))
# print(wordle.has_repeats("teeth"))
# print(wordle.has_repeats("books"))
# print(wordle.has_repeats("gamer"))

# check_word tests

print(wordle.check_word("chair", "check"))
print(wordle.check_word("methe", "teeth"))
print(wordle.check_word("chair", "books"))
print(wordle.check_word("chair", "gamer"))
print(wordle.check_word("cohoe", "cooks"))
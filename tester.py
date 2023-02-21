import wordle

# find_repeats tests

print(wordle.find_num_repeats("check"))
print(wordle.find_num_repeats("teeth"))
print(wordle.find_num_repeats("books"))
print(wordle.find_num_repeats("gamer"))

# has_repeats tests

print(wordle.has_repeats("check"))
print(wordle.has_repeats("teeth"))
print(wordle.has_repeats("books"))
print(wordle.has_repeats("gamer"))

# no_repeats_yellow_and_grey tests

print(wordle.no_repeats_yellow_and_grey("stork", "steam", 2))

# excess_repeats_yellow_and_grey tests

print(wordle.excess_repeats_yellow_and_grey("cooks", "cooko", 2))

# check_word tests

print(wordle.check_word("chair", "check"))
print(wordle.check_word("methe", "teeth"))
print(wordle.check_word("chair", "books"))
print(wordle.check_word("chair", "gamer"))
print(wordle.check_word("cohoe", "cooks"))
print(wordle.check_word("books", "cooko"))
print(wordle.check_word("books", "tasch"))
print(wordle.check_word("books", "ooooo"))

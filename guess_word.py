from collections import Counter

all_words = {}
test_counter = []

### File Pre-Processing
with open("words.txt", "r", encoding="utf-8") as file:
    contents = file.read()
    get_words = contents.split(',')[2:]
    get_words = [words.lower() for words in get_words]
    for i in range(len(get_words) - 1):
        if i % 2 == 0:
            test_counter.append(get_words[i])
            get_words[i] = get_words[i].replace('\n', '')
            all_words[get_words[i]] = get_words[i + 1]
    
    counts = Counter(test_counter)
    duplicates = [item for item, count in counts.items() if count > 1]
    assert len(duplicates) == 0, f"{len(duplicates)} duplicates detected."


def possible_words(word_length, num_spaces=0, num_before=None):
    possible_word_choices = []

    if num_spaces != 0:
        word_length += num_spaces
    
    for word in list(all_words.keys()):
        if num_spaces != 0:
            if " " in word and len(word) == word_length and word.index(" ") == num_before:
                possible_word_choices.append(word)
        else:
            if len(word) == word_length and " " not in word:
                possible_word_choices.append(word)
    
    return possible_word_choices

def specific_letters(some_words, letter_position):
    for lets in letter_position:
        for word in range(len(some_words) - 1, -1, -1):
            if some_words[word][lets[1] - 1] != lets[0]:
                some_words.pop(word)
            
    return some_words

def show_results(word_choices):
    total_words = len(word_choices)
    if total_words == 0:
        print(f"{total_words} possible word choices found. Please try again!")
    elif total_words == 1:
        print(f"{total_words} possible word choice, including...")

        for choice in word_choices:
            print(choice, end="; ")
    
        print()
    else:
        print(f"{total_words} possible word choice(s), including...")

        for choice in word_choices:
            print(choice, end="; ")
    
        print()

def main_function():
    try:
        guess_word = int(input("Enter word(s) length: "))
        with_space = str(input("Word(s) contains spaces? (Y/N) "))

        if with_space.upper().strip() == "Y":
            how_many_spaces = int(input("Enter total number of spaces in words: "))
            first_word = int(input("Enter the length of the FIRST word: "))
            your_words = possible_words(guess_word, how_many_spaces, first_word)
        else:
            your_words = possible_words(guess_word)
        
        more_letters = str(input("Any known letters? Press [ENTER] for yes; press any other key for no. "))
        known_places = []

        while more_letters == "":
            known_letter = str(input("Enter known letter: "))
            known_position = int(input("Enter known letter position: "))
            known_places.append((known_letter.lower().strip(), known_position))
            more_letters = input("Any more known letters? Press [ENTER] to continue; press any other key to exit. ")

        show_results(specific_letters(your_words, known_places))
    except:
        print("Invalid input! Please try again.")


main_function()
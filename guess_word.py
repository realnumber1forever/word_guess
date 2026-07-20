### Importing libraries
from collections import Counter # For duplicate checking

### Global variables across the program
all_words = {} # Keep track of all words
test_counter = [] # For duplicate words checking, just in case

### File Pre-Processing
with open("words.txt", "r", encoding="utf-8") as file:
    contents = file.read()
    get_words = contents.split(',')[2:] # Skip the first line
    get_words = [words.lower() for words in get_words]
    for i in range(len(get_words) - 1):
        if i % 2 == 0: # Add each word, along with its length together
            test_counter.append(get_words[i]) # Separately checking for duplicate words
            get_words[i] = get_words[i].replace('\n', '')
            all_words[get_words[i]] = get_words[i + 1]
    
    # Duplicate word checker
    counts = Counter(test_counter)
    duplicates = [item for item, count in counts.items() if count > 1]
    assert len(duplicates) == 0, f"{len(duplicates)} duplicates detected." # Will not run if any duplicates are found


### Get a list of all possible words, depending on `word_length`,
### `num_spaces`, and `num_before`
def possible_words(word_length, num_spaces=0, num_before=None):
    possible_word_choices = []

    if num_spaces != 0: # Adjust word length accordingly
        word_length += num_spaces
    
    for word in list(all_words.keys()):
        if num_spaces != 0:
            if " " in word and len(word) == word_length and word.index(" ") == num_before:
                possible_word_choices.append(word)
        else:
            if len(word) == word_length and " " not in word:
                possible_word_choices.append(word)
    
    return possible_word_choices

### Get a list of all possible words `some_words`, now taking into consideration
### certain characters at specific positions in `letter_position`
def specific_letters(some_words, letter_position):
    for lets in letter_position:
        for word in range(len(some_words) - 1, -1, -1): # Start backward
            if some_words[word][lets[1] - 1] != lets[0]:
                some_words.pop(word) # Remove if word does not work
            
    return some_words

### Display all possible words `word_choices` after past filtering
def show_results(word_choices):
    total_words = len(word_choices)

    if total_words == 0:
        print(f"{total_words} possible word choices found. Please try again!")
    elif total_words == 1:
        print(f"{total_words} possible word choice, including...")

        for choice in word_choices:
            print(choice, end="; ")
    
        print() # Formatting
    else:
        print(f"{total_words} possible word choice(s), including...")

        for choice in word_choices:
            print(choice, end="; ")
    
        print() # Formatting

### Where most of the interaction and processing occurs for the user
def main_function():
    try: # Just in case of invalid user inputs
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

        while more_letters == "": # Keep entering letters until user decides to stop
            known_letter = str(input("Enter known letter: "))
            known_position = int(input("Enter known letter position: "))
            known_places.append((known_letter.lower().strip(), known_position))
            more_letters = input("Any more known letters? Press [ENTER] to continue; press any other key to exit. ")

        show_results(specific_letters(your_words, known_places)) # Display final results!
    except: # Break out, if so
        print("Invalid input! Please try again.")


### Call the main function!
main_function()
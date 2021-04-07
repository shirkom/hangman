MAX_TRIES = 6  # define
HANGMAN_PHOTOS = {6: """
                    x-------x
                    |
                    |
                    |
                    |
                    |
                    """,
                  5: """
                    x-------x
                    |
                    |
                    |
                    |
                    |
                    """,
                  4: """
                    x-------x
                    |       |
                    |       0
                    |       |
                    |
                    |
                    """,
                  3: """
                    x-------x
                    |       |
                    |       0
                    |      /|
                    |
                    |
                    """,
                  2: """
                    x-------x
                    |       |
                    |       0
                    |      /|\\
                    |       
                    |
                    """,
                  1: """
                    x-------x
                    |       |
                    |       0
                    |      /|\\
                    |      /
                    |
                    """,
                  0: """
                    GAME OVER!
                    x-------x
                    |       |
                    |       0
                    |      /|\\
                    |      / \\
                    |
                    """}


def print_title():
    hang_man_ascii_art = r"""
  __   __ 
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |  
                     |___/"""
    print(hang_man_ascii_art)


def print_hangman(tries):
    print("You left", tries, "tries.")
    print(HANGMAN_PHOTOS[tries])


def is_first_time(letter_guessed, old_letters_guessed):
    if not letter_guessed:
        print("empty str not allowed\t")
        return False

    if letter_guessed.lower() in old_letters_guessed:
        print("X\t" + "->".join(old_letters_guessed))
        print("this letter already used.\t")
        return False

    print("X\t" + "->".join(old_letters_guessed))
    return True


def is_valid_input(letter_guessed):
    if len(letter_guessed) > 1:
        print("E1" if letter_guessed.isalpha() else "E3")
        return False

    if not letter_guessed.isalpha():
        print("E2")
        return False

    return True


def guess_letter(letters_guessed):
    letter_guessed = input("guess letter: ")
    while not is_valid_input(letter_guessed) or not is_first_time(letter_guessed, letters_guessed):
        letter_guessed = input("incorrect letter. please try again: ")

    print("your chose is: " + letter_guessed.lower())
    return letter_guessed.lower()


def is_in_word(secret_word, old_letters_guessed):
    return old_letters_guessed[-1] in secret_word.lower()


def is_win(hidden_word):
    return '_' not in hidden_word


def reveal_letters_in_hidden_word(secret_word, old_letters_guessed):
    hidden_word = ''
    for letter in secret_word:
        if letter.lower() in old_letters_guessed or letter.upper() in old_letters_guessed:
            hidden_word += letter
        else:
            hidden_word += '_'
    return hidden_word


def file_to_words(file_path):
    file = open(file_path, "r")
    all_file = file.read()
    words = []
    for word in all_file.split(' '):
        words.append(word)
    file.close()
    return words


def check_index_and_convert(index):
    while not index.isdigit():
        index = input("Please enter digit: ")
    index = int(index)
    if index < 0:
        return -1 * index
    if index == 0:
        return 1
    return index


def choose_word(file_path, index):
    index_after = check_index_and_convert(index)
    words_in_file = file_to_words(file_path)
    if int(index_after) > len(words_in_file):
        return words_in_file[-1]
    return words_in_file[index_after - 1]


def play():
    print_title()
    words_file_path = input("Enter path for words file: ")
    index = input("Enter the num of word you want to guess: ")
    secret_word = choose_word(words_file_path, index)
    elastic_word = len(secret_word) * '_'
    tries_left = MAX_TRIES

    letters_guessed = []
    while tries_left:
        letters_guessed.append(guess_letter(letters_guessed))

        if not is_in_word(secret_word, letters_guessed):
            print("Try again.\nThe hidden word: " + elastic_word)
            tries_left -= 1
        else:
            elastic_word = reveal_letters_in_hidden_word(secret_word, letters_guessed)
            print("Grate!\nThe hidden word: " + elastic_word)
            if is_win(elastic_word):
                print("YOU WON! :)")
                break
        print_hangman(tries_left)

    print("BAY BAY")


if __name__ == '__main__':
    play()

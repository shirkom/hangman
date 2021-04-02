MAX_TRIES = 6  # define


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


def hang_man(tries):
    print("You left", tries, "tries.")
    if tries == 6:
        print("""
                    x-------x
                    |
                    |
                    |
                    |
                    |
                    """)
    if tries == 5:
        print("""
                    x-------x
                    |       |
                    |       0
                    |
                    |
                    |
                    """)
    if tries == 4:
        print("""
                    x-------x
                    |       |
                    |       0
                    |       |
                    |
                    |
                    """)

    if tries == 3:
        print("""
                    x-------x
                    |       |
                    |       0
                    |      /|
                    |
                    |
                    """)
    if tries == 2:
        print("""
                    x-------x
                    |       |
                    |       0
                    |      /|\\
                    |       
                    |
                    """)

    if tries == 1:
        print("""
                    x-------x
                    |       |
                    |       0
                    |      /|\\
                    |      /
                    |
                    """)
    if tries == 0:
        print("""
                    GAME OVER!
                    x-------x
                    |       |
                    |       0
                    |      /|\\
                    |      / \\
                    |
                    """)


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


def play():
    print_title()
    secret_word = input("Enter word the players guess: ")
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
        hang_man(tries_left)

    print("BAY BAY")


if __name__ == '__main__':
    play()

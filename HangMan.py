#imports for the sound making
from playsound import playsound
import winsound
#import to get paths
import os

#6 states of the hangman-> in a dictionary
HANGMAN_PHOTOS = {0: "x-------x",
                  1: "x-------x\n|\n|\n|\n|\n|",
                  2: "x-------x\n|       |\n|       0\n|\n|\n|",
                  3: "x-------x\n|       |\n|       0\n|       |\n|\n|",
                  4: "\nx-------x\n|       |\n|       0\n|      /|\\\n|\n|",
                  5: "x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|",
                  6: "\nx-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|"}

# Colors from green to red that will be used with the hangman photos -> dictionary
COLORS = {
    0: "\033[38;5;46m",  # Bright green
    1: "\033[38;5;118m", # Light yellow-green
    2: "\033[38;5;154m", # Yellow
    3: "\033[38;5;208m", # Orange-red
    4: "\033[38;5;202m", # Red-orange
    5: "\033[38;5;196m"  # Bright red
}

#max number of wrong tries
MAX_TRIES = 6

def check_win(secret_word, old_letters_guessed):
    """
    this function checks if a player guessed the entire hidden word
    :param secret_word: the word the player needs to guess
    :type: string
    :param old_letters_guessed: the letters the player guessed befor
    :type:list of strings
    :return: weather or not the player guessed the entire word
    :rtype: boolean
    """
    #if all the letters in the secret word are in the old guesses list
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """
    this functions returns the word with the right guesses only and _ at the letters the player didn't guess yet
    :param secret_word: the secert word the player needs to guess
    :type: string
    :param old_letters_guessed: a list of letters the player guessed before
    :type: list of strings
    :return: a string that shows which letters of the word the player guessed and which not
    :rtype: string
    """

    new_str = ""
    #go theough each word in the secret word
    # and if a letter wasn't guessed ,add _ to the new_str and if it was add the letter to the new_str
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_str+=' ' + letter
        else:
            new_str+=' _'
    return new_str

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    this functions checks if the guess is valid. one english letter and the player didnt guess it befor
    :param letter_guessed: the new letter geuss
    :param old_letters_guessed: a list of letters the player already geussed
    :return: if the input wasn't geussed befor and is valid
    :rtype: boolean
    """
    return letter_guessed.lower() not in old_letters_guessed and is_valid_input(letter_guessed)

def is_valid_input(letter_guessed):
    """
    this function checks if the input is valid(one english letter)
    :param letter_guessed:
    :type: string
    :return: if the input is one english letter
    :rtype: boolean
    """
    #if the input is one letter return tru -> it's length is 1 and it's a letter
    length = len(letter_guessed)
    if length == 1:
        if letter_guessed.isalpha():
            return True
    return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    this function checks if a guess is valid and wasn't guessed befor and adds the new letter to the guess list
    :param letter_guessed:
    :type: string
    :param old_letters_guessed:
    :type: list of strings
    :return:if the guess is valid and was added to the list
    :rtype: boolean
    """
    #if the input is valid return true
    if check_valid_input(letter_guessed,old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    #if it's not valis show the list of old guesses to remind the player and return false
    else:
        print('X')
        print( '-> '.join(sorted(old_letters_guessed)[:]))
        return False

def choose_word(file_path, index):
    """
    this function opens a file of words and selects a word according to an index
    :param file_path: the path to the word file
    :type: string
    :param index: the index of the selected word
    :type: int
    :return: the selected word from the list of words in the file
    :rtype: string
    """
    with open(file_path, 'r') as file:
        words = file.read().split()
    return words[(index - 1) % len(words)]


def print_hangman(num_of_tries):
    """
    gets the state of tries and prints the right state hangman from a global dicionary
    :param num_of_tries: how many failed tries the player had
    :type: int
    :return: None
    :rtype: NoneType
    """
    #print hangman with color
    key = min(num_of_tries, len(COLORS) - 1)
    color = COLORS[key]
    print(f"{color}{HANGMAN_PHOTOS[num_of_tries]}\033[0m\n")



def print_start_game():
    """
    this function prints the open screen of the game hangman
    :return: None
    :rtype: NoneType
    """

    HANGMAN_ASCII_ART = """Welcome to the game
            _    _
           | |  | |
           | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
           |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
           | |  | | (_| | | | | (_| | | | | | | (_| | | | |
           |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __/ |
                               |___/"""
    print(HANGMAN_ASCII_ART)


def main():
    #print start game and play the start game sound
    print_start_game()
    winsound.PlaySound(r'C:\Users\yaeld\PycharmProjects\sigit\venv\HangMan\mixkit-bonus-extra-in-a-video-game-2064.wav',
                       winsound.SND_FILENAME)
    #get word file path and index and chose the secret word. keep asking for index and file path until the inptut is right.
    path_to_words_file = input("Enter the path to the words file: ")
    while not os.path.exists(path_to_words_file):
        print("File does not exist. Please enter a valid file path.")
        path_to_words_file = input("Enter the path to the words file: ")
    word_index = input("enter a number that will represent the index of the chosen word: ")
    while not word_index.lstrip('-').isdigit():
        word_index = input("you entered the wrong input... enter a number that will represent the index of the chosen word: ")

    #get the sercet word
    secret_word = choose_word(path_to_words_file, int(word_index))
    #initialization of old letters guessed and number of tries
    old_letter_guessed=[]
    number_of_tries = 0

    #show the first hangman photo
    print_hangman(number_of_tries)
    # show the hidden word befor game starts
    print(show_hidden_word(secret_word, old_letter_guessed))

    #the while loop game- loop while it's not a win and number of tries is still below the max number of tries
    while not check_win(secret_word, old_letter_guessed) and number_of_tries < MAX_TRIES:
        #get a geuss and check if it's valid
        user_guess = input("enter a guess (a single letter): ").lower()
        #if it's not valid continue to the next loop
        if not try_update_letter_guessed(user_guess, old_letter_guessed):
            #print what type of wrong input was enterd-> wrong type/ an old guess
            if(is_valid_input(user_guess)):
                print ("You already geussed this letter")
            else:
                print ("wrong input...")
            continue

        #it's a valid guess that wasn't guessed befor but it's wrong so lets show the hidden word
        # and increase the number of tries and show the hangman

        if user_guess.lower() not in secret_word:
            number_of_tries+=1
            print_hangman(number_of_tries)
        print(show_hidden_word(secret_word, old_letter_guessed))

    #if it's a win show win statement and play the win sound
    if check_win(secret_word, old_letter_guessed):
        print("\033[92mWIN!!")
        winsound.PlaySound(r'C:\Users\yaeld\PycharmProjects\sigit\venv\HangMan\mixkit-winning-an-extra-bonus-2060.wav',
                           winsound.SND_FILENAME)

    #it's not a win so show the lose statement, lose sound, and the headen word
    else:
        print("\033[91mLOSE :( \033[0m")
        print("the word was " + secret_word)
        winsound.PlaySound(r'C:\Users\yaeld\PycharmProjects\sigit\venv\HangMan\mixkit-long-game-over-notification-276.wav',
                           winsound.SND_FILENAME)

if __name__ == "__main__":
    main()
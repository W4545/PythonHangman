# File Name: hangman
# Date Started: 3/1/2017


import os
import sys
from random import randint

if os.name == 'posix':  # If the current operating system is linux
    clear_screen_command = 'tput reset'  # Sets the linux clear screen command
elif os.name == 'nt':  # If the current operating system is windows
    clear_screen_command = 'cls'  # Sets the windows clear screen command
else:
    sys.exit('Invalid Operating System')  # Otherwise exit the program


def game_start():  # Initiates the game by allowing the user to input a word or have the program select one
    os.system(clear_screen_command)  # Clears the screen
    while True:  # Loops the game_start code to ensure the user inputs proper responses
        choose = input("Would you like to enter a word or guess a random word? (Enter E to enter a word or R to "
                       "guess a random word): ")
        os.system(clear_screen_command)  # Clears the screen

        if choose.lower() == 'e':  # If the user wants to enter a word
            word = input("Enter a word to guess: ").lower()
            os.system(clear_screen_command)  # Clears the screen
            break  # Breaks out of the while loop

        elif choose.lower() == 'r':  # If the user wants the program to randomly select a word

            while True:  # Loops input statement to ensure user inputs an appropriate response
                try:  # If the user enters a response with letters in it, the code doesn't crash
                    level = int(input('What level of difficulty would you like? (Enter 1 for easy, 2 for medium, '
                                      'and 3 for hard): '))
                    if level != 1 and level != 2 and level != 3:  # If the user didn't enter a 1, 2, or a 3
                        raise ValueError  # Throws the same error to jump to the exception code
                    else:
                        break

                except ValueError:  # Excepts the error to prevent the code from crashing
                    os.system(clear_screen_command)  # Clears the screen
                    print("Please only enter a 1, 2, or a 3")
            os.system(clear_screen_command)  # Clears the screen

            if level == 1:  # If the user selected the easy word difficulty
                print("Easy selected")
                word_list = open("easy_list.txt", 'r').read()  # Load the easy word list
    # Source:
    # https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
            elif level == 2:  # If the user selected the medium word difficulty
                print("Medium Selected")
                word_list = open("medium_list.txt", 'r').read()  # Load the medium word list
    # Source:
    # https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-medium.txt
            else:  # Since all possible values are either a 1, 2, or a 3, the only left option is the hard difficulty
                print("Hard Selected")
                word_list = open("hard_list.txt", 'r').read()  # Load the hard word list
    # Source:
    # https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
            word_list = word_list.split("\n")  # Convert the string word_list to a list
            word = word_list[randint(0, len(word_list) - 1)]  # assign a random word from the list to the variable word
            break  # Break out of the while loop
        else:  # If the user entered an incorrect input
            print("Invalid Entry.")

    hidden_word = "_" * len(word)  # Generates the empty spaces for the word

    while True:  # Continues to loop until proper response is given
        os.system(clear_screen_command)  # Clears the screen
        random_letter = input(
            "Would you like to start with a guessed letter in the word? (enter Y for yes or N for no): ")

        if random_letter.lower() == "y":  # If the user wants to start with a random letter
            hidden_word = scanner(word, word[randint(0, len(word) - 1)], hidden_word)
            break  # Breaks out of while loop
        elif random_letter.lower() == 'n':  # If the user doesn't want a random letter
            break  # Breaks out of while loop
        else:
            print("Incorrect Entry")

    os.system(clear_screen_command)  # Clears the screen

    return word, hidden_word  # Returns the word and hidden word


def assembling(list_of_stuff):  # Inputs a list of letters and assembles them into a word
    assembled = ""
    for item in list_of_stuff:  # For each letter in the list
        item = item.replace(" ", "")  # Removes spaces left from splitting the original word during scanning
        assembled += item  # Appends the letter to the end of the assembled word
    return assembled


def display_man(number_of_limbs):  # Inputs the number of "limbs" the man has lost
    man = [" O\n", "/", "|", "\\\n", "/ ", "\\\n"]  # A list of the man cut into lines

    for i in range(number_of_limbs):  # Cycles through the list to print the designated number of limbs
        print(man[i], end="")
    print("")


def scanner(word, guess, hidden_word):  # Inputs the word, the letter guessed, and the current hidden word
    index = 0

    hidden_word = " ".join(hidden_word)  # Adds spaces between each letter
    new_hidden = hidden_word.split(" ")  # Splits the string into a list with each item in the list a letter

    for letter in word:  # Cycles through each letter in the list
        if letter == guess:  # If the letter equals the user's guess
            new_hidden[index] = guess  # Reveals the letter in the hidden word
        index += 1

    return assembling(new_hidden)  # Returns the hidden word as a string after being reassembled


def game(word, hidden_word):  # Inputs the word to guess and the hidden word
    os.system(clear_screen_command)  # Clears screen
    limbs_lost = 0
    guessed_letters = []
    while limbs_lost < 6:  # While the man is not completely hanged. If the man is completely hanged, the game will end.

        display_man(limbs_lost)  # Displays the man
        print("Remaining limbs:", 6 - limbs_lost)
        print("Guessed letters: ", end="")
        for letter in guessed_letters:  # Cycles through a list of the guessed letters and prints them
            print(letter, end=" ")
        print("")

        guess = input(hidden_word + "\n\nGuess a letter or the whole word(Enter quit to exit): ")
        os.system(clear_screen_command)  # Clears screen
        if len(guess) == 1:  # If the user entered a single letter
            guess = guess.lower()
            guessed_letters.append(guess)  # Adds the letter to the list of guessed letters
            value = scanner(word, guess, hidden_word)  # Scans the word and reveals the guessed letter

            if hidden_word == value:  # If the scanner didn't find the letter in the word
                limbs_lost += 1

            else:  # The user successfully found a letter
                print("Good Guess!!")
                hidden_word = value  # Updates the hidden word to include the guessed letter

        elif guess == "DEBUG_WORD":
            print(word)  # Shows the word

        elif guess == "DEBUG_LIMB":
            limbs_lost -= 1  # Decreases the limb

        elif guess == "DEBUG_HINT":
            hidden_word = scanner(word, word[randint(0, len(word) - 1)], hidden_word)  # Reveals a letter

        elif guess.lower() == 'quit':  # If the user typed "quit"
            sys.exit(0)  # Exits the program

        elif guess.lower() == word:  # If the user successfully guess the whole word
            print("GOOD JOB! You guessed it!")
            hidden_word = word  # Assigns the hidden word to the unhidden word

        else:  # The user attempted to guess the whole word but failed.
            print("Oops. Wrong Guess. You will gain two limbs")
            limbs_lost += 2
        print("")  # Prints empty line

        if hidden_word == word:  # If the user has guess the whole word
            break  # Break out of the game loop

    return limbs_lost


def main():
    while True:  # While the user wants to play the game

        word, hidden_word = game_start()  # Initiates user setup of the game and assigns the word and hidden word

        outcome = game(word, hidden_word)  # Starts the main game loop and returns the number of limbs hanged
        os.system(clear_screen_command)  # Clears the screen

        if outcome >= 6:  # If the user completely hanged the man
            print("You Lose!\nThe word was", word)
        else:  # If the user didn't hang the man, they guessed the complete word
            print("You win!!!!!\nYou successfully guessed the word", word, "!!!!")

        while True:  # Ensures correct response to question
            repeat = input("Play again? (Y for yes, N for no): ")
            os.system(clear_screen_command)  # Clears the screen
            if repeat.lower() == "n":  # If the user doesn't want to continue playing
                sys.exit(0)  # Exits the program
            elif repeat.lower() == "y":  # If the user wants to keep playing
                break  # Breaks out of while loop
            else:
                print("Incorrect Entry")

main()

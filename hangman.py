# File Name: hangman
# Date Started: 3/1/2017
# Icon made by Freepik from www.flaticon.com

import os
import sys
from random import randint

if os.name == 'posix':  # If the current operating system is linux
    clear_screen_command = 'tput reset'  # Sets the linux clear screen command
elif os.name == 'nt':  # If the current operating system is windows
    clear_screen_command = 'cls'  # Sets the windows clear screen command
else:
    sys.exit('Invalid Operating System')  # Otherwise exit the program

#  User: ashes999
if hasattr(sys, '_MEIPASS'):  # If the code is running from a .exe file
    os.chdir(sys._MEIPASS)  # Changes the active directory to the temporary directory created by the .exe file
#  Source: http://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile


def game_start():  # Initiates the game by allowing the user to input a word or have the program select one
    os.system(clear_screen_command)  # Clears the screen
    while True:  # Loops the game_start code to ensure the user inputs proper responses
        choose = input("Would you like to enter a word or guess a random word? (Enter E to enter a word or R to "
                       "guess a random word): ")
        os.system(clear_screen_command)  # Clears the screen

        if choose.lower() == 'e':  # If the user wants to enter a word
            word = input("Enter a word to guess: ").lower()
            os.system(clear_screen_command)  # Clears the screen

        elif choose.lower() == 'r':  # If the user wants the program to randomly select a word
            os.system(clear_screen_command)  # Clears the screen
            while True:  # Loops input statement to ensure user inputs an appropriate response
                level = input('What level of difficulty would you like? (Enter 1 for normal and 2 for hard): ')
                os.system(clear_screen_command)  # Clears the screen
                if level == '1':  # If the user didn't enter a 1
                    print("Normal selected")
                    word_list = open("src\medium_list.txt", 'r').read()  # Load the normal word list
        # Source:
        # https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-medium.txt
                elif level == '2':  # If the user entered a 2
                    print("Hard Selected")
                    word_list = open("src\hard_list.txt", 'r').read()  # Load the hard word list
        # Source:
        # https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-long.txt
                else:
                    print("Please only enter a 1 or a 2")
                    continue  # Restarts while loop
                break  # break out of while loop
            word_list = word_list.split("\n")  # Convert the string word_list to a list
            word = word_list[randint(0, len(word_list) - 1)]  # assign a random word from the list to the variable word
        else:  # If the user entered an incorrect input
            os.system(clear_screen_command)  # Clears the screen
            print("Invalid Entry.")
            continue  # Restarts while loop
        break

    hidden_word = "_" * len(word)  # Generates the empty spaces for the word

    while True:  # Continues to loop until proper response is given
        random_letter = input(
            "Would you like to start with a guessed letter in the word? (enter Y for yes or N for no): ")

        if random_letter.lower() == "y":  # If the user wants to start with a random letter
            guessed_letter = word[randint(0, len(word) - 1)]
            hidden_word = scanner(word, guessed_letter, hidden_word)
        elif random_letter.lower() == 'n':  # If the user doesn't want a random letter
            guessed_letter = ''  # Ensures a letter doesn't get added to the guessed letters list
        else:
            os.system(clear_screen_command)  # Clears the screen
            print("Incorrect Entry")
            continue  # Restarts while loop
        break

    os.system(clear_screen_command)  # Clears the screen

    return word, hidden_word, guessed_letter  # Returns the word, the hidden word, and the guessed letter


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


def game(word, hidden_word, revealed_letter):  # Inputs the word to guess, the hidden word, and the revealed letter
    os.system(clear_screen_command)  # Clears screen
    limbs_lost = 0
    guessed_letters = []
    guessed_letters += revealed_letter
    while limbs_lost < 6:  # While the

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

        elif guess == "DEBUG_WORD" or guess == '001':
            print(word)  # Shows the word

        elif guess == "DEBUG_LIMB" or guess == '002':
            limbs_lost -= 1  # Decreases the limbs

        elif guess == "":  # If the user accidentally hit enter
            continue

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

        word, hidden_word, revealed_letter = game_start()
        # Initiates user setup of the game and assigns the word, hidden word, and the initial hidden letter

        outcome = game(word, hidden_word, revealed_letter)
        # Starts the main game loop and returns the number of limbs hanged

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

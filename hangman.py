# File Name: hangman
# Programmer: Jack Young
# Date Started: 3/1/2017


import os  # Used to clear the command prompt
import sys  # Used to properly exit the program
from random import randint  # Used to randomly select a word from the lists


def game_start():  # Initiates the game by allowing the user to input a word or have the program select one
    while True:  # Loops the game_start code to ensure the user inputs proper responses
        choose = input("Would you like to enter a word or guess a random word? (Enter E to enter a word or R to "
                       "guess a random word): ")
        os.system('cls')  # Clears the screen

        if choose.lower() == 'e':  # If the user wants to enter a word
            word = input("Enter a word to guess: ").lower()
            break  # Breaks out of the while loop

        elif choose.lower() == 'r':  # If the user wants the program to randomly select a word

            while True:  # Loops input statement to ensure user inputs an appropriate response
                try:  # If the user enters a response with letters in it, the code doesn't crash
                    level = int(input('What level of difficulty would you like? (Enter 1 for easy, 2 for medium, '
                                      'and 3 for hard: '))
                    if level != 1 and level != 2 and level != 3:  # If the user didn't enter a 1, 2, or a 3
                        raise ValueError  # Throws the same error to jump to the exception code
                    else:
                        break

                except ValueError:  # Excepts the error to prevent the code from crashing
                    os.system('cls')  # Clears the screen
                    print("Please only enter a 1, 2, or a 3")
            os.system('cls')  # Clears the screen

            if level == 1:  # If the user selected the easy word difficulty
                print("Easy selected")
                word_list = open("easy_list.txt", 'r').read()  # Load the easy word list

            elif level == 2:  # If the user selected the medium word difficulty
                print("Medium Selected")
                word_list = open("medium_list.txt", 'r').read()  # Load the medium word list

            else:  # Since all possible values are either a 1, 2, or a 3, the only left option is the hard difficulty
                print("Hard Selected")
                word_list = open("hard_list.txt", 'r').read()  # Load the hard word list

            word_list = word_list.split("\n")  # Convert the string word_list to a list
            word = word_list[randint(0, len(word_list) - 1)]  # assign a random word from the list to the variable word
            break  # Break out of the while loop
        else:  # If the user entered an incorrect input
            print("Invalid Entry.")
    os.system('cls')  # Clears the screen
    return word  # Returns the word


def assembling(list_of_stuff):
    assembled = ""
    for item in list_of_stuff:
        item = item.replace(" ", "")
        assembled += item
    return assembled


def display_man(number_of_limbs):
    man = [" O\n", "/", "|", "\\\n", "/ ", "\\\n"]
    index = 0
    for i in range(number_of_limbs):
        if index <= number_of_limbs:
            print(man[index], end="")
        index += 1
    print("")


def scanner(word, guess, hidden_word):
    index = 0

    hidden_word = " ".join(hidden_word)
    new_hidden = hidden_word.split(" ")

    for letter in word:
        if letter == guess:
            new_hidden[index] = guess
        index += 1

    return assembling(new_hidden)


def game(word, hidden_word):
    os.system('cls')
    limbs_lost = 0
    guessed_letters = []
    while limbs_lost < 6:

        display_man(limbs_lost)
        print("Remaining limbs:", 6 - limbs_lost)
        print("Guessed letters: ", end="")
        for letter in guessed_letters:
            print(letter, end=" ")
        print("")

        guess = input(hidden_word + "\n\nGuess a letter or the whole word(Enter quit to exit): ")
        if len(guess) == 1:
            guess = guess.lower()
            guessed_letters.append(guess)
            value = scanner(word, guess, hidden_word)

            if hidden_word == value:
                os.system("cls")
                limbs_lost += 1

            else:
                os.system("cls")
                print("Good Guess!!")
                hidden_word = value

        elif guess.lower() == 'quit':
            sys.exit(0)
        elif guess.lower() == word:
            os.system("cls")
            print("GOOD JOB! You guessed it!")
            hidden_word = word
        else:
            os.system("cls")
            print("Oops. Wrong Guess. You will gain two limbs")
            limbs_lost += 2
        print("")

        if hidden_word == word:
            break

    return limbs_lost


def main():
    while True:
        word = game_start()
        hidden_word = "_" * len(word)

        while True:
            random_letter = input(
                "Would you like to start with a guessed letter in the word? (enter Y for yes or N for no): ")

            if random_letter.lower() == "y":
                hidden_word = scanner(word, word[randint(0, len(word) - 1)], hidden_word)
                break
            elif random_letter.lower() == 'n':
                break
            else:
                os.system('cls')
                print("Incorrect Entry")

        outcome = game(word, hidden_word)
        os.system('cls')

        if outcome >= 6:
            print("You Lose!\nThe word was", word)
        else:
            print("You win!!!!!")

        while True:
            repeat = input("Play again? (Y for yes, N for no): ")
            if repeat.lower() == "n":
                sys.exit(0)
            elif repeat.lower() == "y":
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Incorrect Entry")

main()

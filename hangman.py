# File Name: hangman
# Programmer: Jack Young
# Date Started: 3/1/2017


import os
import sys
from random import randint


def game_start():
    word = ''
    level = 1
    while True:
        choose = input("Would you like to enter a word or guess a random word? (Enter E to enter a word or R to "
                       "guess a random word): ")

        if choose.lower() == 'e':
            word = input("Enter a word to guess: ")
            word = word.lower()
            break
        elif choose.lower() == 'r':
            while True:
                try:
                    level = int(input('What level of difficulty would you like? (Enter 1 for easy, 2 for medium, '
                                      'and 3 for hard: '))
                    if level != 1 and level != 2 and level != 3:
                        raise ValueError
                    break
                except ValueError:
                    print("Please only enter a 1, 2, or a 3")
            if level == 1:
                print("Easy selected")
                word_list = open("easy_list.txt", 'r').read()
            elif level == 2:
                print("Medium Selected")
                word_list = open("medium_list.txt", 'r').read()
            else:
                print("Hard Selected")
                word_list = open("hard_list.txt", 'r').read()

            word_list = word_list.split("\n")
            word = word_list[randint(0, len(word_list) - 1)]
            break
        else:
            print("Invalid Entry.")
    return word


def assembling(list_of_stuff):
    assembled = ""
    for item in list_of_stuff:
        item = item.replace(" ", "")
        assembled += item
    return assembled


def display_man(number_of_limbs_lost):
    man = [" O\n", "/", "|", "\\\n", "/ ", "\\\n"]
    index = 0
    for i in range(number_of_limbs_lost):
        if index <= number_of_limbs_lost:
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
    limbs_lost = 0
    guessed_letters = []
    while limbs_lost < 6:

        guess = input(hidden_word + "\n\nGuess a letter or the whole word(Enter quit to exit): ")
        if len(guess) == 1:
            guess = guess.lower()
            guessed_letters.append(guess)
            value = scanner(word, guess, hidden_word)

            if hidden_word == value:
                os.system("cls")
                limbs_lost += 1
                display_man(limbs_lost)
                print("Remaining limbs:", 6 - limbs_lost)
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
            display_man(limbs_lost)
        print("")

        if hidden_word == word:
            break

        print("Guessed letters: ", end="")
        for letter in guessed_letters:
            print(letter, end=" ")
        print("")
    return limbs_lost


def main():
    while True:
        word = game_start()
        hidden_word = "_" * len(word)

        random_letter = input(
            "Would you like to start with a guessed letter in the word? (enter Y for yes or N for no): ")
        if random_letter.lower() == "y":
            hidden_word = scanner(word, word[randint(0, len(word) - 1)], hidden_word)

        os.system("cls")
        outcome = game(word, hidden_word)

        if outcome == 6:
            print("You Lose!\nThe word was", word)
        else:
            print("You win!!!!!")

        repeat = input("Play again? (Y for yes, N for no): ")
        if repeat.lower() == "n":
            break
        elif repeat != "y":
            sys.exit(2)


main()

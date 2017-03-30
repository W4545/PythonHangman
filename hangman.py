# File Name: hangman
# Programmer: Jack Young
# Date Started: 3/1/2017


import os
import sys
from random import randint


def game_start():
    level = ''
    choose = input("Would you like to enter a word or guess a random word? (Enter E to enter a word or R to guess a "
                   "random word): ")
    if choose.lower() == 'e':
        word = input("Enter a word to guess: ")
        word = word.lower()
    else:
        while True:
            try:
                level = int(input('What level of difficulty would you like? (Enter 1 for easy, 2 for medium, '
                                  'and 3 for hard: '))
                if level != 1 and level != 2 and level != 3:
                    raise ValueError
                break
            except ValueError:
                print("please only enter a 1, 2, or a 3")
        if level == 1:
            print("Easy selected")
            word_list = open("easy_list.txt", 'r').read()
        elif level == 2:
            word_list = open("medium_list.txt", 'r').read()
        else:
            word_list = open("hard_list.txt", 'r').read()

        word_list = word_list.split("\n")
        word = word_list[randint(0, len(word_list) - 1)]
    return word


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
    limbs = 0
    guessed_letters = []
    while limbs < 6:
        guess = input(hidden_word + "\n\nGuess a letter: ")
        print("")
        guess = guess.lower()
        guessed_letters.append(guess)
        value = scanner(word, guess, hidden_word)

        if hidden_word == value:
            limbs += 1
            display_man(limbs)
            print("Remaining Limbs:", 6-limbs)
        else:
            print("Good Guess!!")
            hidden_word = value

        if hidden_word == word:
            break

        print("Guessed letters: ", end="")
        for letter in guessed_letters:
            print(letter, end=" ")
        print("")
    return limbs


def main():
    while True:
        word = game_start()
        hidden_word = "_" * len(word)
        os.system("cls")

        random_letter = input(
            "Would you like to start with a guessed letter in the word? (enter Y for yes or N for no): ")

        if random_letter.lower() == "y":
            letter_index = randint(0, len(word) - 1)
            value = scanner(word, word[letter_index], hidden_word)
            hidden_word = value

        outcome = game(word, hidden_word)

        if outcome == 6:
            print("You Lose!\nThe word was", word)
        else:
            print("You win!!!!!")

        repeat = input("Play again? (Y for yes, N for no): ")
        repeat.lower()
        if repeat == "n":
            break
        elif repeat != "y" and repeat != "n":
            sys.exit(2)


main()

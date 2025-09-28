#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    if letter in word:
        return True
    else:
        return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    if spot < len(word) and word[spot] == letter:
        return True
    else:
        return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    gradedGuess = ''
    #enumerate is my favorite function in the world.
    #if I didn't know enumerate, I'd probably use a pointer var based on length of the word.
    #but enumerate makes all that not needed
    for i, letter in enumerate(myGuess):
        if inSpot(letter, word, i):
            gradedGuess += letter.upper()
        elif inWord(letter, word):
            gradedGuess += letter.lower()
        else:
            gradedGuess += "*"
    return gradedGuess

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    #print(todayWord)
    #no cheating

    #User should get 6 guesses to guess
    for guess in range(6):
    #Ask user for their guess
        while True:
            user_guess = input("Guess a 5 letter word: ")
            if len(user_guess) < 5 or len(user_guess) > 5:
                print(f"{user_guess} isn't a 5 letter word. No guess consumed.")
                continue
            if user_guess in wordList:
                break
            else:
                print(f"Word {user_guess} is not in word list. Guess consumed.")
                break

    #Give feedback using on their word:
        if user_guess == todayWord:
            print("You guessed the word!")
        else:
            print(rateGuess(user_guess, todayWord))
    print(f"You lost! The word was {todayWord}")





if __name__ == '__main__':
  main()

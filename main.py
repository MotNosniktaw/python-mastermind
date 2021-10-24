import random
import re

guesses = []
passcode = ""
guessesLeft = 10


def generatePasscode():
    output = ""
    for x in range(4):
        output += str(random.randint(1, 6))
    return output


def checkGuess(guess, passcode):
    fullMatchCount = ""
    partialMatchCount = ""
    noMatchCount = ""

    for idx, val in enumerate(guess):
        if passcode[idx] == val:
            fullMatchCount += "Z"
        elif val in passcode:
            partialMatchCount += "Y"
        else:
            noMatchCount += "X"

    return fullMatchCount + partialMatchCount + noMatchCount


def takeGuessInput():
    output = input()
    inputRegex = r"^[1-6]{4}$"

    if len(re.findall(inputRegex, output)) == 0:
        print("That was not a valid guess. Try again:")
        return takeGuessInput()
    else:
        return output


while True:
    if len(guesses) == 0:
        print("Welcome to Mastermind.")
        print("The rules be simple. You have 10 attempts to guess the password.")
        print("The passcode is 4 digits (1-6). I will tell you whether you got any exact or near matches.")
        print("")

        passcode = generatePasscode()
        print("Give me your first guess:")
    else:
        print("")
        print("Your remaining guesses: " + str(guessesLeft))
        print("Your previous guesses")
        for guess in guesses:
            print(guess + " - " + checkGuess(guess, passcode))
        print()
        print("Give me your next guess:")

    guessInput = takeGuessInput()
    if guessInput == passcode:
        print("Huzzah")
        break
    elif guessInput == "quit":
        print("Sad to see you go. Thanks for playing.")
        break
    else:
        guesses.append(guessInput)
        guessesLeft -= 1
        print("That was not the correct passcode.")

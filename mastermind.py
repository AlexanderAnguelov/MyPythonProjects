import re
import random
from collections import Counter


def compare(num1, num2):
    bulls = 0
    cows = 0
    list = []
    if num1[0] == num2[0]:
        bulls += 1
    if num1[1] == num2[1]:
        bulls += 1
    if num1[2] == num2[2]:
        bulls += 1
    if num1[3] == num2[3]:
        bulls += 1
    for digit in num1:
        if digit in list:
            pass
        elif num2.count(digit) > 0:
            cows += min(num1.count(digit), num2.count(digit))
        list += [digit]
    cows -= bulls
    return bulls, cows


GAME_CHOICE = input("Type 1 for computer to guess your number or type 2 for you to guess computer's number:\n")
if GAME_CHOICE == "1":
    PLAYER_CODE = input("Enter your secret 4 digit code: ")
    if re.match("^[0-9]{4}$", PLAYER_CODE):
        ALL_CODES = []
        # Creating list with all possible 10000 codes.
        for digit1 in range(0, 10):
            for digit2 in range(0, 10):
                for digit3 in range(0, 10):
                    for digit4 in range(0, 10):
                        ALL_CODES.append(str(digit1) + str(digit2) + str(digit3) + str(digit4))
        GUESS = "".join(map(str, random.sample(range(10), 4)))
        # The first guess random number with 4 different digits.
        REMAINING_CODES = ALL_CODES
        while True:
            print("Computer's guess is:", GUESS)
            BULLS = int(input("Number of 'bulls' in the guess is: "))
            if BULLS == 4:
                # If computer gets 4 bulls the game is over.
                print("Game over!")
                break
            COWS = int(input("Number of 'cows' in the guess is: "))
            FEEDBACK = BULLS, COWS
            REMAINING_CODES = [code for code in REMAINING_CODES if compare(GUESS, code) == FEEDBACK]
            # Only valid codes remain in this list given the user feedback.
            NextGuessFunction = lambda x: max(Counter(compare(x, code) for code in REMAINING_CODES).values())
            # Function compares all remaining codes and scores them based on bulls+cows, takes the max value.
            if len(REMAINING_CODES) == 1:
                # If there is only one element in the list, this is the one we are looking for
                GUESS = REMAINING_CODES[0]
            else:
                GUESS = min(REMAINING_CODES, key=NextGuessFunction)
            # Otherwise we take the minimum based on the function of all remaining codes left.
    else:
        print("Wrong code!")
elif GAME_CHOICE == "2":
    SECRET_CODE = str(random.randint(0, 9999))
    while len(SECRET_CODE) != 4:
        SECRET_CODE = "0" + SECRET_CODE

    while True:
        USER_CODE = input("Enter 4 digit code guess or type 'stop' to give up:\n")
        if USER_CODE == "stop":
            print("The code was: ", SECRET_CODE)
            break
        elif re.match("^[0-9]{4}$", USER_CODE):
            print("You guessed", USER_CODE, ": (Bulls, Cows) - ", compare(USER_CODE, SECRET_CODE))
        else:
            print("Wrong code!")
        if SECRET_CODE == USER_CODE:
            print("You guessed the code!")
            break
else:
    print("Error!")

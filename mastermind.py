import re
import random
from collections import Counter


def compare(num1, num2):
    bulls_count = 0
    cows_count = 0
    list = []
    if num1[0] == num2[0]:
        bulls_count += 1
    if num1[1] == num2[1]:
        bulls_count += 1
    if num1[2] == num2[2]:
        bulls_count += 1
    if num1[3] == num2[3]:
        bulls_count += 1
    for digit in num1:
        if digit in list:
            pass
        elif num2.count(digit) > 0:
            cows_count += min(num1.count(digit), num2.count(digit))
        list += [digit]
    cows_count -= bulls_count
    return bulls_count, cows_count


game_choice = input("Type 1 for computer to guess your number or type 2 for you to guess computer's number:\n")
if game_choice == "1":
    player_code = input("Enter your secret 4 digit code: ")
    if re.match("^[0-9]{4}$", player_code):
        all_codes = []
        # Creating list with all possible 10000 codes.
        for digit1 in range(0, 10):
            for digit2 in range(0, 10):
                for digit3 in range(0, 10):
                    for digit4 in range(0, 10):
                        all_codes.append(str(digit1) + str(digit2) + str(digit3) + str(digit4))
        guess = "".join(map(str, random.sample(range(10), 4)))
        # The first guess random number with 4 different digits.
        remaining_codes = all_codes
        while True:
            print("Computer's guess is:", guess)
            bulls = int(input("Number of 'bulls' in the guess is: "))
            if bulls == 4:
                # If computer gets 4 bulls the game is over.
                print("Game over!")
                break
            cows = int(input("Number of 'cows' in the guess is: "))
            feedback = bulls, cows
            remaining_codes = [code for code in remaining_codes if compare(guess, code) == feedback]
            # Only valid codes remain in this list given the user feedback.
            NextGuessFunction = lambda x: max(Counter(compare(x, code) for code in remaining_codes).values())
            # Function compares all remaining codes and scores them based on bulls+cows, takes the max value.
            if len(remaining_codes) == 1:
                # If there is only one element in the list, this is the one we are looking for
                guess = remaining_codes[0]
            else:
                guess = min(remaining_codes, key=NextGuessFunction)
            # Otherwise we take the minimum based on the function of all remaining codes left.
    else:
        print("Wrong code!")
elif game_choice == "2":
    secret_code = str(random.randint(0, 9999))
    while len(secret_code) != 4:
        secret_code = "0" + secret_code

    while True:
        user_code = input("Enter 4 digit code guess or type 'stop' to give up:\n")
        if user_code == "stop":
            print("The code was: ", secret_code)
            break
        elif re.match("^[0-9]{4}$", user_code):
            print("You guessed", user_code, ": (Bulls, Cows) - ", compare(user_code, secret_code))
        else:
            print("Wrong code!")
        if secret_code == user_code:
            print("You guessed the code!")
            break
else:
    print("Error!")

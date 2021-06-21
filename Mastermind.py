# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
import random


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


SECRET_CODE = str(random.randint(0, 9999))
while len(SECRET_CODE) != 4:
    SECRET_CODE = "0" + SECRET_CODE
while True:
    USER_CODE = input("Enter 4 digit code guess:\n")
    if re.match("^[0-9]{4}$", USER_CODE):
        print("You guessed (Bulls, Cows) - ", compare(USER_CODE, SECRET_CODE))
    else:
        print("Wrong code!")
    if SECRET_CODE == USER_CODE:
        print("You guessed the code!")
        break

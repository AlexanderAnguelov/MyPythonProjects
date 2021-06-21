# MyPythonProjects

##What is this game:
Mastermind/Bulls and Cows
The computer randomly picks a 4-digit number. The human player tries to guess the number according to the - [game rules](https://en.wikipedia.org/wiki/Mastermind_(board_game)). 
###How to play the game:
Download and run the mastermind.py file.
###How does the code work:
It checks if the user input is correct (4-digit number) and then compares the input with the computer's randomly generated 4-digit code.
The compare function first finds out how many "bulls" have been guessed, then finds the count of the correct digit guesses and extracts the "bulls" from that to find the "cows".
The game continues untill the player guesses the number.

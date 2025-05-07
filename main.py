# IMPORT THE RANDOM MODULE
from random import randint
# WELCOME THE USER AND DISPLAY INSTRUCTIONS
print("Welcome to the Number Guessing Game!")
print("In this game, you have to try to guess the number I'm thinking of from 1-100.")

# CREATE A VARIABLE TO STORE THE RANDOM NUMBER FOR THE USER TO GUESS
number_to_guess = randint(1,100)
print(number_to_guess)

# CREATE CONSTANTS TO STORE THE NUMBER OF ATTEMPTS THE USER STARTS WITH, DEPENDENT ON THE DIFFICULTY
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5

# CREATE A VARIABLE TO STORE THE GAME'S LEVEL
game_level = input("Choose your difficulty level. Type 'easy' or 'hard': ").lower()


# CREATE A FUNCTION FOR USER TO CHOOSE A DIFFICULTY LEVEL
def choose_difficulty(choice):
    if choice == "q":
        return
    elif choice == "":
        print("That isn't a valid choice. Enter either 'easy' or 'hard' to continue.")
    elif choice == "easy":
        print(f"You chose easy mode. You have {EASY_MODE_ATTEMPTS} attempts to guess the number, good luck!")
        return EASY_MODE_ATTEMPTS
    elif choice == "hard":
        print(f"You chose hard mode. You have {HARD_MODE_ATTEMPTS} attempts to guess the number, good luck!")
        return HARD_MODE_ATTEMPTS
    
# CREATE A VARIABLE TO STORE THE NUMBER OF GUESSES THE USER HAS LEFT   
num_of_guesses_left = choose_difficulty(game_level)





from random import randint

print("Welcome to the Number Guessing Game!")
print("In this game, you have to try to guess the number I'm thinking of from 1-100.")

EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5
INVALID_CHOICE_MSG = "That isn't a valid choice. Enter either 'easy' or 'hard' to continue."

number_to_guess = randint(1,100)
print(number_to_guess)

difficulty_level_or_quit = input("Choose your difficulty level. Type 'easy' or 'hard' or 'q' to quit: ").lower()


def choose_difficulty(choice):
    if choice == "easy":
        print(f"You chose easy mode. You have {EASY_MODE_ATTEMPTS} attempts to guess the number, good luck!")
        return EASY_MODE_ATTEMPTS
    elif choice == "hard":
        print(f"You chose hard mode. You have {HARD_MODE_ATTEMPTS} attempts to guess the number, good luck!")
        return HARD_MODE_ATTEMPTS
    elif choice == "q":
        print("You chose to quit, goodbye!")
        return "quit"
    elif choice == "":
        print(INVALID_CHOICE_MSG)
        return INVALID_CHOICE_MSG
    else: 
        print(INVALID_CHOICE_MSG)
        return INVALID_CHOICE_MSG
    
    
# CREATE A VARIABLE TO STORE THE NUMBER OF GUESSES THE USER HAS LEFT   
num_of_guesses_left = choose_difficulty(difficulty_level_or_quit)

# CREATE A FUNCTION FOR USER TO CHOOSE A DIFFICULTY LEVEL

    









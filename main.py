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
    """Returns either the number of attempts the user has
    or it quits the game or returns an invalid choice message"""

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
    
    
num_of_guesses_left = choose_difficulty(difficulty_level_or_quit)


def check_answer(user_guess, answer):
    """Checks the user's guess and returns updated guesses and result status"""
    
    global num_of_guesses_left
    game_over = "GAME OVER."

    if user_guess > answer:
        num_of_guesses_left -= 1
        print(f"Your answer, {user_guess}, was too high, try again.")
        print(f"You have {num_of_guesses_left} guesses left.")
        if num_of_guesses_left == 0:
            print(game_over)
    elif user_guess < answer:
        num_of_guesses_left -= 1
        print(f"Your answer, {user_guess}, was too low, try again.")
        print(f"You have {num_of_guesses_left} guesses left.")
        if num_of_guesses_left == 0:
            print(game_over)
    else:
        print(f"Your answer, {user_guess}, was CORRECT! YOU WIN!")
        return True

while num_of_guesses_left > 0:
    user_guess = int(input("What's the number I'm thinking of?: "))
    compared_guess_to_answer = check_answer(user_guess, number_to_guess)
    
    if compared_guess_to_answer != True:
        continue
    else:
        break
 
        
  






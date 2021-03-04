import random

random_num = random.randint(1, 50)

def play_again():
    again = input("Would you like to play again. Type 'y' for yes or 'n' for no:")
    if again == 'y':
        guessing_game()
    else: 
        print("Goodbye.")

def guessing_game():
    attempts = 0
    guess = int(input("The number is between 1 and 50. You have 10 guesses. Guess a number: "))
    should_continue = True
    while should_continue:
        if guess != random_num:
            attempts += 1
            print(f"Try Again. {10 - attempts} attampts left.")
            guess = int(input("Guess again: "))
            if attempts == 3:
                print(f"Hint! The number is near {random_num - 5}.")
            elif attempts == 6:
                print(f"Final Hint! The number is near {random_num + 2}")
            elif attempts == 10:
                should_continue = False
                print(f"No more attempts! The number was {random_num}.")
                play_again()
        elif guess == random_num:
            should_continue = False
            attempts += 1
            print(f"You guessed the number in {attempts} attempts!")
            play_again()

guessing_game()


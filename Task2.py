#Program by Muhammad Talal Tahir

import random

def Talal_guess_game():
    """
    Number guessing game function.
    The computer selects a number between 1 and 50.
    User has 5 guesses to find it.
    Gives hints and shows score.
    """
    num = random.randint(1, 50)
    guesses = 0

    for i in range(1, 6):
        print("Enter your guess no.", i)
        try:
            guess = int(input())
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        guesses += 1

        if guess == num:
            print("Your guess is correct")
            break
        elif guess > num:
            print("Your guess is high")
        elif guess < num:
            print("Your guess is low")

    if guess == num:
        print("**********CONGRATULATIONS**********")

    print("The number was", num)
    print("You used", guesses, "guesses.")

# Main loop
while True:
    Talal_guess_game()
    again = input("Do you want to play again? (y/n): ")
    if again.lower() != 'y':
        print("Thank you for playing!")
        break

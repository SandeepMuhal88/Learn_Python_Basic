# Game instructions
print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
import random
number_to_guess = random.randint(1, 100)

print("I have selected a number between 1 and 100. Can you guess it?")

print("Instructions:")
print("1. If you want to exit the game, type 'exit'.")
print("2. If you want a hint, type 'hint'.")
print("3. Otherwise, enter your guess as a number.")

while True:
    #get user input
    user_input =input("Enter your guess :")
    if user_input.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    elif user_input.lower() == 'hint':
        if number_to_guess % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
    else:
        try:
            user_guess = int(user_input)
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the number!")
                break
        except ValueError:
            print("Invalid input. Please enter a number, 'hint', or 'exit'.")


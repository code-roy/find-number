# using random module in python we can creat mini project.

# We can use the Python's built-in random module to generate a random number.
import random

# now we set the Range and it help to Generate the Secret Number
lower_bound = 1
upper_bound = 100
secret_number = random.randint(lower_bound, upper_bound)

#for tracking the player atempt 
attempts = 0


print(f"Guess the number between {lower_bound} and {upper_bound}!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < lower_bound or guess > upper_bound:
            print(f"Please enter a number between {lower_bound} and {upper_bound}.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

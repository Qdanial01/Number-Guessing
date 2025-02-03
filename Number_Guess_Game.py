import random

# Set up range
lowest_number = 1
highest_number = 10
max_attempts = 10

# Generate random number
secret_number = random.randint(lowest_number, highest_number)

# User input
def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lowest_number} and {highest_number}: "))
            if lowest_number <= guess <= highest_number:
                return guess
            else:
                print("Invalid input. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Compare random number and user's number
def play_game():
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        if guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        # Provide a hint on the last attempt
        if attempts == max_attempts - 1:
            hint = abs(secret_number - guess)
            print(f"Hint: The secret number is within {hint} of your guess.")

    print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")

# Start the game
play_game()
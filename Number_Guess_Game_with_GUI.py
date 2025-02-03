# import tkinter for the GUI 
import tkinter as tk
from tkinter import messagebox
import random

# Set up range
lowest_number = 1
highest_number = 10
max_attempts = 10

# Generate random number within range set
# Set attempt count to 0
secret_number = random.randint(lowest_number, highest_number)
attempts = 0

# User input
def check_guess():
    global attempts, secret_number
    try:
        # Takes user's input and turns it into INT
        user_guess = int(entry_guess.get())
        # Checks if number input is valid or within preset range
        if not (lowest_number <= user_guess <= highest_number):
            messagebox.showerror(f"Invalid Number, Please enter a number between {lowest_number} and {highest_number}.")
            return
        
        # Tracks attempts made
        attempts += 1
        if user_guess == secret_number:
            messagebox.showinfo("Congratulations!", f"You guessed the secret number {secret_number} in {attempts} attempts")
            reset_game()
        elif user_guess < secret_number:
            label_result.config(text="Too low! Try again.")
        else:
            label_result.config(text="Too high! Try again.")

        # Provide hint on last attempt
        # Not hardcoded to 9 so that if max attempts were to change there is no need to change this code
        if attempts == max_attempts - 1:
            hint = abs(secret_number - user_guess)
            label_hint.config(text=f"Hint: The secret number is within {hint} of your guess.")

        # Game over message once max number of attempts is reached.
        if attempts == max_attempts:
            messagebox.showinfo("Game Over", f"You've used up all {max_attempts} attempts. The number was {secret_number}.")
            reset_game()

    # If valid number if not keyed in
    except ValueError:
        messagebox.showerror("Please enter a valid number.")
    
#Define reset game to reset the secret number, attempt count, and user input fields
def reset_game():
    global secret_number, attempts
    secret_number = random.randint(lowest_number, highest_number)
    attempts = 0
    entry_guess.delete(0, tk.END)
    label_result.config(text="")
    label_hint.config(text="")

#Set up GUI window
window = tk.Tk()
window.title("Number Guesser Game")
window.geometry("300x300")

label_title = tk.Label(window, text="Guess the Number!", font=("Arial", 16))
label_title.pack(pady=10)

label_instruction = tk.Label(window, text=f"Enter a number between {lowest_number} and {highest_number}:")
label_instruction.pack(pady=5)

entry_guess = tk.Entry(window, width=10)
entry_guess.pack(pady=5)

# Button will have check to call the check_guess function
button_check = tk.Button(window, text="Check", command=check_guess)
button_check.pack(pady=5)

label_result = tk.Label(window, text="", font=("Arial", 12))
label_result.pack(pady=5)

label_hint = tk.Label(window, text="", font=("Arial", 10), fg="blue")
label_hint.pack(pady=5)

# Reset game button which uses the reset game function: see line 53 -> 59
button_reset = tk.Button(window, text="Reset Game", command=reset_game)
button_reset.pack(pady=5)

window.mainloop()
        

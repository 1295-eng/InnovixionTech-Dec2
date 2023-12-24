import random

def number_guessing_game():
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    
    max_attempts = 10
    attempts = 0
    
    print(f"Welcome to the Number Guessing Game! Guess a number between {lower_limit} and {upper_limit}")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
    
    if guess != secret_number:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

number_guessing_game()

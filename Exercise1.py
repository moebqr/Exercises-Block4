import random

# Set random seed
random.seed()

# Generate random number between 1 and 100
hidden_number = random.randint(1, 100)

while True:
    # Get user's guess
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer!")
        continue
        
    # Check if guess is correct
    if guess == hidden_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < hidden_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

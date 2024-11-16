# Set random seed
set.seed(NULL)

# Generate random number between 1 and 100
hidden_number <- sample(1:100, 1)

# Start guessing game loop
while(TRUE) {
  # Get user's guess
  guess <- tryCatch({
    as.numeric(readline("Guess a number between 1 and 100: "))
  }, warning = function(w) {
    return(NA)
  })
  
  # Validate input
  if(is.na(guess)) {
    print("Please enter a valid number!")
    next
  }
  
  # Check if guess is correct
  if(guess == hidden_number) {
    print("Congratulations! You guessed the number!")
    break
  } else if(guess < hidden_number) {
    print("Too low! Try again.")
  } else {
    print("Too high! Try again.")
  }
}

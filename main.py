import random # Imports random valid number from dataset

print("====================================")
print("  Welcome to Guess the Number!")
print("====================================")

import random # Imports random valid number from dataset
playing = True # Shows user is actively playing
best_score = None # sets no default score
while playing:
    number = random.randint(1, 100) #shows parameters of the game
    attempts = 1 # Shows how many attempts are added after each attempt
    max_attempts = 10 # Max attempts for the game
    
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")
 # Outlines the rules of the game
  
    if best_score is not None:
        print(f"Current High Score: {best_score} attempt(s)")
    print("------------------------------------")
# Will print the highest score if the user has previously played
  
 # --- Input Validation for First Guess ---
    valid_guess = False
    while not valid_guess:
        try:
            guess = int(input("Please enter your guess: "))
            valid_guess = True
        except ValueError:
            print("Invalid input! Please enter a whole number.")
# Only allows valid numerials to be entered

 # --- Main Game Loop ---
    while guess != number and attempts < max_attempts:
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
# Output is decided based on the users guess and is printed
        
        remaining = max_attempts - attempts
        print(f"Attempts left: {remaining}")
# Highlights to the user how many guesses they have had
        
# Validate each subsequent guess
        valid_guess = False
        while not valid_guess:
            try:
                guess = int(input("\nTry again: "))
                valid_guess = True
            except ValueError:
                print("Invalid input! Please enter a whole number.")
 # Reiterates that the guess needs to be a whole numerical value
        attempts += 1 #adds +1 to attempt value after a guess

 # --- Round Outcome & High Score ---
    print("------------------------------------")
    if guess == number:
        print(f"Wooo! You guessed it in {attempts} attempt(s)!")
 # Prints a congratulations message and highlights the amount of attempts taken, if the number if successfully guessed.
        
 # Update high score if it's the first win or a new record
        if best_score is None or attempts < best_score:
            best_score = attempts
            print("🎉 New High Score! 🎉")
# Updates the users highests score where appropriate
  
    else:
        print(f"Game Over! You ran out of attempts.")
        print(f"The secret number was {number}.")
 # If the user runs out of attempts and is unsuccessful then the user is shown this message, and the secret number is revealed.

 # --- Play Again Prompt ---
    again = input("\nWould you like to play again? (y/n): ").strip().lower()
    if again != 'y':
        playing = False
        print("Thanks for playing! Goodbye!")
  # Gives the user the choice to play again or not. If they decide not to then the game is ended and they are shown a goodbye message

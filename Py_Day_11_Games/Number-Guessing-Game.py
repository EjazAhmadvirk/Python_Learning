import random
# Number Guessing Game      
number_to_guess = random.randint(1, 100)
attempts = 0
# Print welcome message and instructions
print("Guess the number between 1 and 100!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
# Number Guessing Game

# --- Part 1: Countdown Timer ---
start = int(input("Enter starting number for countdown: "))

while start >= 0:
    print(start)
    start -= 1

print("Blast off!")

print()  # spacer

# --- Part 2: Simple Guessing Game ---
secret_number = 67
max_attempts = 5   
attempts = 0

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < secret_number:
        print(f"{guess} is Too low! Try again.\n")
    elif guess > secret_number:
        print(f"{guess} is Too high! Try again.\n")
    else:
        print("Congratulations! You guessed it!")
        break
else:
    print(f"Sorry, you ran out of attempts. The secret number was {secret_number}.")
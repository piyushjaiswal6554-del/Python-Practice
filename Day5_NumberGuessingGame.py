import random

number = random.randint(1, 100)
attempts = 0
while True:
    attempts += 1
    guess = int(input("Guess the number (1-100): "))

    if guess == number:
        print("Correct! You guessed it!")
        print("Attempts:",attempts)
        break
    elif guess > number:
        print(" Too high! Try again.")
    else:
        print("Too low! Try again.")
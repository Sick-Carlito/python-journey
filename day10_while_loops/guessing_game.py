# Day 10 - Number Guessing Game

import random

secret = random.randint(1, 10)
guess = 0
tries = 0

print("🎯 Guess the secret number between 1 and 10!")

while guess != secret:
    guess = int(input("Your guess: "))
    tries += 1

    if guess < secret:
        print("Too low! 📉")
    elif guess > secret:
        print("Too high! 📈")
    else:
        print(f"🎉 Correct! You guessed it in {tries} tries.")


# infinite chatbot loop


# Day 10 - Infinite Chatbot

print("CarlBot is here! Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("CarlBot: Goodbye 👋")
        break
    else:
        print("CarlBot: I heard you say:", user)

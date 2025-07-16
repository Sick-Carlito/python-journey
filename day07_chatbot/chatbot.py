# Day 7 - Simple Chatbot Project

print("🤖 Hi there! I'm CarlBot. Let's chat!")

name = input("What's your name? ").title()
print(f"Nice to meet you, {name}!")

age = int(input("How old are you? "))
print(f"Wow, {age} years old? That's awesome!")

# Respond differently based on age
if age < 13:
    print("You're a cool kid!")
elif age < 20:
    print("Teen life is fun, right?")
else:
    print("Adulthood can be wild 😄")

# Ask about favorite things
food = input("What's your favorite food? ")
color = input("What's your favorite color? ")
animal = input("If you were an animal, what would you be? ")

# Final response
print(f"\nOkay, let me see... You love {food}, your favorite color is {color}, and you'd be a {animal}!")
print("You're awesome, " + name + "! Thanks for chatting 💬")

# Goodbye message
goodbyes = ["Bye!", "See you!", "Talk later!", "Peace out!"]
import random
print(random.choice(goodbyes))


# Day 5 - Sentence Maker

color = input("Enter a color: ")
food = input("Enter your favorite food: ")
animal = input("Enter an animal: ")
city = input("Enter a city: ")

sentence = f"In {city.title()}, I saw a {color.lower()} {animal.lower()} eating {food.lower()}!"
print("\nYour custom sentence:")
print(sentence)


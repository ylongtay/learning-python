# === Python Crash Course 3rd ed - Chapter 4 Exercise 1 ===

# Ex 4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
domino_pizzas = ["simply cheese", "classified chicken", "hawaiian paradise"]
for pizza in domino_pizzas:
    print(pizza)
    print(f"{pizza.title()} is one of my favorite pizza of Domino's\n")
print("I really like Domino's Pizza!\n")

# Ex 4-2. Animals: Create a list of 3 animals that have common characteristic.
# Use for loop to print out name of each animal
animals = ["whale", "dolphin", "narwhal"]
for animal in animals:
    print(f"I will love to see a {animal} when cruising in the sea.")
print("To be able to see these sea mammals live is a dream come true!")
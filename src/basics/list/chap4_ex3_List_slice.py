# === Python Crash Course 3rd ed - Chapter 4 Exercise 2 ===

# Ex 4-10: Slices: Using one created program in this chapter
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# Task 1: Use a slice to print the first three items from that program’s list
print(f"""The first three items in the list are:
{cubes[0:3]}""")

# Task 2: Use a slice to print three items from the middle of the list
print(len(cubes))
print(f"""Three items from the middle of the list are:
{cubes[4:7]}""")

# Task 3: Use a slice to print three items from the middle of the list
print(f"""The last three items in the list are:
{cubes[-3:]}""")

# Ex 4-11: My Pizzas, Your Pizzas: Start with your program from Exercise 4-1.
# Make a copy of the list of pizzas, and call it friend_pizzas.
domino_pizzas = ["simply cheese", "classified chicken", "hawaiian paradise"]
for pizza in domino_pizzas:
    print(pizza)
    print(f"{pizza.title()} is one of my favorite pizza of Domino's\n")
print("I really like Domino's Pizza!\n")
friend_pizzas = domino_pizzas[:]

# Task 1: Add a new pizza to the original list.
domino_pizzas.append("chilli chicken")
# Task 2: Add a different pizza to the list friend_pizzas.
friend_pizzas.append("classic pepperoni")
# Task 3: Prove that you have two separate lists. Use for loop to print pizza from the two lists
print("My favorite pizzas are:")
for pizza in domino_pizzas:
    print(f"{pizza.title()}")
print("\nMy friend's favorite pizzas are:")
for f_pizza in friend_pizzas:
    print(f"{f_pizza.title()}")

# Ex 4-12: More Loops: Write two for loops to print each list of foods
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nHere is a list of my favorite foods:")
for food in my_foods:
    print(food.title())
print("\nHere is a list of my friend's favorite foods:")
for f_food in friend_foods:
    print(f_food.title())
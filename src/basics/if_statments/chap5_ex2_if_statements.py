# === Python Crash Course 3rd ed - Chapter 5 Exercise 2 ===

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# Write code that passes.
alien_color = "green"
if alien_color == "green":
  print("You earned 5 points")
# Write code that fails.
alien_color = "red"
if alien_color == "green":
  print("You earned 5 points")
# No output as conditional test fail

# 5-4. Alien Colors #2: Choose another color for an alien and write an if-else chain.
# Write code that runs the if block
alien_color = "green"
if alien_color == "green":
  print("You earned 5 points")
else:
  print("You earned 10 points")
# Write another code that runs the else block.
alien_color = "red"
if alien_color == "green":
  print("You earned 5 points")
else:
  print("You earned 10 points")

# 5-5. Alien Colors #3: Turn if-else chain into if-elif-else with 3 alien colors.
# Uncomment each alien_color to test the if statements
# alien_color = "green"
# alien_color = "yellow"
alien_color = "red"
if alien_color == "green":
  print("You earned 5 points")
elif alien_color == "yellow":
  print("You earned 10 points")
elif alien_color == "red":
  print("You earned 15 points")

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life.
# Set a value for the variable age
age = 38
if age < 2:
  life_stage = "baby"
elif age < 4:
  life_stage = "toddler"
elif age < 13:
  life_stage = "kid"
elif age < 20:
  life_stage = "teenager"
elif age < 65:
  life_stage = "adult"
elif age >= 66:
  life_stage = "elderly"
print(f"I am a/an {life_stage}")

# Ex 5-7. Favorite Fruit: Make a list of your favorite fruits and write a series of independent 
# if statements that check for certain fruits in your list.
fav_fruits = ["grapes", "mango", "durian"]

# Write five if statements. Each check for a certain kind of fruit in the list. 
# When passes if block should print a statement.
if "grapes" in fav_fruits:
  print("Yes, grapes is one of my favorite!")
if "mango" in fav_fruits:
  print("Yes, mango is one of my favorite!")
if "durian" in fav_fruits:
  print("Yes, durian is one of my favorite!")
if "cherries" in fav_fruits:
  print("Yes, cherries is one of my favorite!")
if "watermelon" in fav_fruits:
  print("Yes, watermelon is one of my favorite!")
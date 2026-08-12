# === Python Crash Course 3rd ed - Chapter 4 Exercise 4 ===

# Ex 4-13. Buffet: A buffet-style restaurant offers only five basic foods. 
# Create a Tuple to store them.
buffet_menu = ("fried rice", "samosa", "curry chicken", "kang kong", "eclairs")

# Task 1: Use a for loop to print each food the restaurant offers.
print("Buffet Menu:")
for food in buffet_menu:
  print(f"{food.title()}")

# Task 2: Try to modify one of the items and check Python for error
# buffet_menu[0] = "fried beehoon" 

# Task 3: Restaurant changes its menu and replaced two of the foods. 
# Rewrite the tuple and use for loop to print each food in the revised menu.
buffet_menu = ("fried beehoon", "spring roll", "curry chicken", "kang kong", "eclairs")
print("\nRevised Buffet Menu:")
for items in buffet_menu:
  print(f"{items.title()}")
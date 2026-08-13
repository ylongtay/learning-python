# === Python Crash Course 3rd ed - Chapter 5 Exercise 1 ===

# Ex 5-1. Conditional Tests: Write a series of conditional tests. 
# Print a statement describing each test and prediction for the results.
# Ex 5-2. More Conditional Tests: Have at least one True and one False result for each of the test:
# - Test using equality and inequality with strings
# - Test using lower() method
# - Numerical test using various operators
# - Test using keyword 'and' and 'or'
# - Check for item in a list using 'in' keyword
# - Check for item not in a list using 'not in' keyword

username = "anonymous"
print("Is username != 'anonymous'? I predict False.")
print(username != "anonymous")
print("\nIs username == 'anonymous'? I predict True.")
print(username == 'anonymous')

username = "John"
print("\nIs username == 'john'? I predict False.")
print(username == 'john')
print("\nIs username.lower() == 'john'? I predict True.")
print(username.lower() == 'john')

height_0 = 163
height_1 = 119
print("\nIs both height >= 120? I predict False.")
print(height_0 >= 120 and height_1 >= 120)
print("\nIs either of the height >= 120? I predict True.")
print( height_0 >= 120 or height_1 >= 120)
print("\nIs both of height > 110? I predict True.")
print(height_0 > 110 and height_1 > 110)
print("\nIs either of the height >= 170? I predict False.")
print( height_0 >= 170 or height_1 >= 170)

prawn_aglio = ["pasta", "prawn", 'chilli']
ingredient_A = "prawn"
ingredient_B = "rice"
print(f"\nIngredient A is {ingredient_A.title()}")
print(f"Ingredient B is {ingredient_B.title()}")
if ingredient_A in prawn_aglio:
  print("\nIs ingredient_A in prawn aglio? I predict True.")
  print(ingredient_A in prawn_aglio)
  print("Is ingredient_A not in prawn aglio? I predict False.")
  print(ingredient_A not in prawn_aglio)
if ingredient_B not in prawn_aglio:
  print("\nIs ingredient_B not in prawn aglio? I predict True.")
  print(ingredient_B not in prawn_aglio)
  print("Is ingredient_B in prawn aglio? I predict False.")
  print(ingredient_B in prawn_aglio)





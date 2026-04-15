# Exercise 2: Case Manipulation with f-strings

# Task: Use a variable to represent a person's name in all lowercase letters 
# (e.g., user_name = "eric matthes").
# Then, use an f-string to print the person's name in title case,
# Every word capitalized, using the .title() method within the braces.
# Example Output: "Hello, Eric Matthes!"

user_name = "eric matthes"
greeting = f"Hello, {user_name.title()}!"
print(greeting)
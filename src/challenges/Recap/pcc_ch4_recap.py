## Chapter 4 Recap exercise: Numerical Cruncher & Comprehensions

# Create a list with odd numbers from 1 to 29
list_odd = list(range(1, 29, 2))
print(list_odd)

# Print max, min and sum of the list
print(min(list_odd))
print(max(list_odd))
print(sum(list_odd))

# Using a list comprehension, create a list called cubes containing the cubes (n**3) of all multiples of 3 between 3 and 30 inclusive.
cubes_3 = [n**3 for n in range(3,31,3)]
print(cubes_3)
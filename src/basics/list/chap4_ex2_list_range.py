# === Python Crash Course 3rd ed - Chapter 4 Exercise 2 ===

# Ex 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

### Note: Off-by-one behavior in programming apply to range() method
for value in range(1, 21):
  print(value)

# Ex 4-4. One Million: Make a list of the numbers from one to one million.
# Use a for loop to print the numbers.
a_million_list = list(range(1, 1_000_001))
# print(a_million_list)

# Ex 4-5. Summing a Million: Use min() and max() to check list starts at 1 and ends at 1,000,000.
print(min(a_million_list))
print(max(a_million_list))
print(sum(a_million_list))

# Ex 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use for loop to print each number
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
  print(odd_number)

# Ex 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
# Use a for loop to print the numbers in your list.
multiples_3 = list(range(3, 31, 3))
for multiple_of_3 in multiples_3:
  print(multiple_of_3)

# Ex 4-8. Cubes: Make a list of the first 10 cubes. 
# Use a for loop to print out the value of each cube.
cubes = []
for value in range(1, 11):
  cubes.append(value**3)
for cube in cubes:
  print(cube)

# Ex 4-9. Try using list comprehension to generate first 10 cubes
cubes = [value**3 for value in range(1, 11)]
print(cubes)
for cube in cubes:
  print(cube)
## Python Crash Course 3rd ed - Ex 1

# Ex 3-1. Names: Store the names of a few of your friends in a list called names
names = ['calvin', 'zac', 'jr', 'faith', 'michelle', 'raf']
print(names[0], names[1], names[2], names[3], names[4], names[5])
print(names[-1], names[-2], names[-3], names[-4], names[-5], names[-6])

# Ex 3-2. Greetings: Use list in Ex 3-1. Print a message to each person
print(f"Hello {names[0].title()}, how have you been doing?")
print(f"Hello {names[1].title()}, how have you been doing?")
print(f"Hello {names[2].title()}, how have you been doing?")
print(f"Hello {names[-3].title()}, how have you been doing?")
print(f"Hello {names[-2].title()}, how have you been doing?")
print(f"Hello {names[-1].title()}, how have you been doing?")

# Ex 3-3. Your Own List: Make a list my favorite mode of transportation and print statements with them
transport_modes = ['bicycle', 'car', 'plane', 'bus']
message = f'''I like to use {transport_modes[0]} and explore the parks with my wife.
To own a {transport_modes[1]} is my 40s dream. Taking {transport_modes[2]} to travel twice a year helps me recharge.
The most efficient way for me to get to work is by {transport_modes[-1]}.'''
print(f"\n{message}")

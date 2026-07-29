## Python Crash Course 3rd ed - Exercises 2"

# Ex 2-3. Personal Message
fullname = "Tay Yong Long"
message = f"Hello {fullname}, would you like to learn some python today?"
print(message)

# Ex 2-4. Name cases - Print names using different strings methods
given_name = "Yong Long"
surname = "Tay"
fullname = f"{surname} {given_name}"

# Print name in lowercase
print(fullname.lower())

# Print name in uppercase
print(fullname.upper())

# Print name in title 
print(fullname.title())

# Ex 2-5 & 2-6 Famous Quote: Print the quote and the name of its author. Quote in " quotation marks
quote = "With great power comes great responsibility."
author = "Stan Lee"
print(f'{author} once said, "{quote}"')

# Ex 2-7 Stripping Names: Print name in variable with whitespace, 
# add \t tab and \n Newline at least once
# Print name once showing whitespace around the name then print name 
# with stripping functions: lstrip(), rstrip(), strip()
fullname2 = " Yong Long "
print(fullname2)
print(f"\t{fullname2}")
print(f"\n{fullname2}")
print(f"{fullname2.lstrip()}")
print(f"\n{fullname2}")
print(f"{fullname2.rstrip()}")
print(f"\n{fullname2}")
print(f"{fullname2.strip()}")

# Ex 2-8 Use removesuffix() method to display filename without extension
filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))

### Notes for removeprefix in lesson ###
supplementary_url = "https://ehmatthes.github.io/pcc_3e"
simple_url = supplementary_url.removeprefix('https://')
print(simple_url)
### ============ End =============== ###
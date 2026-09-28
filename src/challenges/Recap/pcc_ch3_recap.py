## Chapter 3 Recap exercise: Dynamic Guest List Manager

guest = ["faith", "jr", "mich", "raf"]

#Replace Guest at index 1
guest[1] = "wifey"

# Expand more guest using insert() and append() methods
guest.insert(1, "john")
guest.append("shirley")

# Print the list temporarily in alphabetical order
# without mutating the original list
guest_sorted = sorted(guest)
print(guest_sorted)
print(guest)

# Venue shrink remove guest using pop()
rejected_guest1 = guest.pop()
rejected_guest2 = guest.pop()
print(f'Sorry {rejected_guest1}, venue size limited, I will invite you next time')
print(f'Sorry {rejected_guest2}, venue size limited, I will invite you next time')

# Sort remaining two guest permanently
print(guest.sort(reverse=True)) # INCORRECT
# Reason: The code print(guest.sort(reverse=True)) outputs None 
# because the sort() method modifies the list in place and returns None.
# Correction below
guest.sort(reverse=True)
print(guest)

# Wrong if use 'del guest' as whole list will be deleted
del guest[:]
print(guest)
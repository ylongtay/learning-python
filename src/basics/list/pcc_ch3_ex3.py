### Python Crash Course 3rd ed - Chapter 3 Exercise 3

## Ex 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

# Task: Store location in a list not in alphabetical order
bucket_list = ["Switzerland", "Iceland", "Norway", "Finland", "New Zealand"]
# Print list in its original order
print(bucket_list)

# Use sorted() to print your list in alphabetical order without modifying theactual list.
# Print and show that your list is still in its original
print("\nMy travel bucket list sorted:") 
print(sorted(bucket_list))
print("My original travel bucket list:") 
print(bucket_list)

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list
reverse_list = sorted(bucket_list , reverse=True)
print("\nMy travel bucket list sorted in reverse alphabetical order:") 
print(reverse_list)
print("My original travel bucket list:") 
print(bucket_list)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
bucket_list.reverse()
print("\nMy original travel bucket list in reverse order:") 
print(bucket_list)
# Use reverse() again to revert back the order of your list.
bucket_list.reverse()
print("My original travel bucket list:") 
print(bucket_list)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list with order changed.
bucket_list.sort()
print("\nMy sorted travel bucket list:")
print(bucket_list) 
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
bucket_list.sort(reverse=True)
print("\nMy sorted travel bucket list in reverse order:")
print(bucket_list)
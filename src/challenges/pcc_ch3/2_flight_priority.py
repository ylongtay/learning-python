# Challenge 2: Flight passenger priority manifest
# Scenario: An airline needs to generate an alphabetical passenger list for gate agents, 
# while keeping track of who registered first and last.

# Task 1: Create a list of passengers in order of arrival
# Task 2: Access and store the first passenger to arrive using positive indexing and negative indexing for last passenger
arrival_list = ["Charles", "Alice", "Eve", "Bob", "Daniel"]
first_passenger = arrival_list[0]
last_passenger = arrival_list[-1]

# Task 3: Use sorted() to print a temporary, alphabetically sorted list of passengers without changing order of the original.
# Task 4: Print the original list to prove its not change
temp_alpha_sorted = sorted(arrival_list)
check_original = f"{arrival_list}"

# [ERROR] check_original = arrival_list :: resulted to reverse alphabetical due to .sort(reverse=True)

# Task 5: Use sort() to permanently sort the list in reverse alphabetical order
# Task 6: Print the permanently sorted list
arrival_list.sort(reverse=True)

# [ERROR] final_boarding_order = arrival_list.sort(reverse=True) :: will result to 'None' in the f-string
# Because sort() method modifies the original list directly "in-place" and returns None

manifest_summary = f''' === FLIGHT BOARDING MANIFEST ===
First Arrived: {first_passenger}
Last Arrived: {last_passenger}

Alphabetical (Temporary): {temp_alpha_sorted}
Original List Intact: {check_original}

Final Boarding Order (Reverse Alphabetical): {arrival_list}'''

print(manifest_summary)
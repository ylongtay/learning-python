# Challenge 3: Concert VIP Access & Cancellation Handler
# Scenario: A VIP concert booking system is managing a exclusive guest list. 
# Venue capacity changes, requiring quick updates to the guest list.

# Task 1: Create a VIP list.
# Task 2: Print a personalized message to the 3rd person on the list to inform him/her that they been upgraded to front row.
vips = ["Taylor", "Drake", "Beyonce", "Ed"]
upgrade_notice = f"{vips[2]}, you have been upgraded to front row!"

# Task 3: Venue shrinks capacity, only 2 people can fit.
# Task 4: Print a regret message to cancelled_guest using an f-string.
del vips[1]
cancelled_guest = vips.pop()
cancelled_notice = f"Sorry {cancelled_guest}, your VIP ticket was cancelled due to capacity limits."

# Task 5: Reverse the order of the remaining guest.
# Task 6: Print the final vip list and the final count of guests using len().
vips.reverse()
system_message = f'''=== VIP ACCESS SYSTEM ===
Special Upgrade: {upgrade_notice}
Regret Notice: {cancelled_notice}

Final Guest List (Reverse): {vips}
Total Guests Confirmed: {len(vips)}'''
print(system_message)
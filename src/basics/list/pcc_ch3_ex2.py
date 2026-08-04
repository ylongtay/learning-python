## Python Crash Course 3rd ed - Chapter 3 Exercise 2

# Ex 3-4. Guest List: Make a list that includes at least three people to invite for dinner.
# Use list to print a message to each person, inviting them to dinner.
invitation_list = ["john", "zac"]
invitation_list.append("calvin")
print(invitation_list)
message = f'''
========================= Housewarming invitation =========================
The following {len(invitation_list)} guests:
Hello {invitation_list[0].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[1].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[2].title()}, we will like to invite to our new humble home on 26 Aug 2026.'''
print(message)

# Ex 3-5. One of your guests can’t make it for  the dinner, so you need to send out a new set of invitations.
print(f"{invitation_list[2].title()} rejected. Reason: Sorry, cannot make it for the dinner\n")

invitation_list[2] = "shirley"
print(invitation_list)
new_message =  f'''
========================= Housewarming invitation =========================
The following {len(invitation_list)} guests:
Hello {invitation_list[0].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[1].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[2].title()}, we will like to invite to our new humble home on 26 Aug 2026.'''
print(new_message)

# Ex 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
news_update = "\nHi Everyone, I have brought a new dining table that can host more of you!"
print(news_update)

invitation_list.insert(0, "jr")
invitation_list.insert(2, "faith")
invitation_list.append("jac")

updated_message = new_message =  f'''
========================= Housewarming invitation =========================
The following {len(invitation_list)} guests:
Hello {invitation_list[0].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[1].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[2].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[-3].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[-2].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[-1].title()}, we will like to invite to our new humble home on 26 Aug 2026.'''
print(updated_message)

# Ex 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and now you have space for only two guests 
news_update = "\nSorry all invitee, our new table cannot arrive on time. We only have space for two."
print(news_update)

popped_guest = invitation_list.pop()
cancel_message = f'Sorry {popped_guest}  we have limited space and cannot invite you for this event. We will arrange and invite you again'
print(cancel_message)

popped_guest = invitation_list.pop()
cancel_message = f'Sorry {popped_guest}  we have limited space and cannot invite you for this event. We will arrange and invite you again'
print(cancel_message)

popped_guest = invitation_list.pop()
cancel_message = f'Sorry {popped_guest}  we have limited space and cannot invite you for this event. We will arrange and invite you again'
print(cancel_message)

popped_guest = invitation_list.pop()
cancel_message = f'Sorry {popped_guest}  we have limited space and cannot invite you for this event. We will arrange and invite you again'
print(cancel_message)

updated_message = new_message =  f'''
========================= Housewarming invitation =========================
The following {len(invitation_list)} guests:
Hello {invitation_list[0].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[1].title()}, we will like to invite to our new humble home on 26 Aug 2026.
'''
print(updated_message)

# Task: Use del and .remove() to remove the last two names from your list, so you have an empty list. 
# Print list to check list is empty. 
print(invitation_list)
del invitation_list[0]
invitation_list.remove('john')
## Ex 3-11. Intentional Error: IndexError will occur when try to del after remove() method
# As the index we trying to delete is already empty
# del invitation_list[1]
print(invitation_list)

# Ex 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 to 3-7.
# Use len() to print a message indicating the number of people you’re inviting to dinner.
# Added answer at line 10, 23, 40, 72.
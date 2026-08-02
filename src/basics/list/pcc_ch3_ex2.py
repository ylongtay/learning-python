## Python Crash Course 3rd ed - Chapter 3 Exercise 2

# Ex 3-4. Guest List: Make a list that includes at least three people to invite for dinner.
# Use list to print a message to each person, inviting them to dinner.
invitation_list = ["john", "zac"]
invitation_list.append("calvin")
print(invitation_list)
message = f'''\n============= Housewarming invitation =============
Hello {invitation_list[0].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[1].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[2].title()}, we will like to invite to our new humble home on 26 Aug 2026.
'''
print(message)

# Ex 3-5. One of your guests can’t make it for  the dinner, so you need to send out a new set of invitations.
print(f"{invitation_list[2].title()} rejected. Reason: Sorry, cannot make it for the dinner")
invitation_list[2] = "shirley"
print(invitation_list)
new_message =  f'''\n============= Housewarming invitation =============
Hello {invitation_list[0].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[1].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[2].title()}, we will like to invite to our new humble home on 26 Aug 2026.
'''
print(new_message)

# Ex 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
news_update = "Hi Everyone, I have brought a new dining table that can host more of you!"
print(news_update)

invitation_list.insert(0, "jr")
invitation_list.insert(2, "faith")
invitation_list.append("jac")

updated_message = new_message =  f'''\n============= Housewarming invitation =============
Hello {invitation_list[0].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[1].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[2].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[-3].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[-2].title()}, we will like to invite to our new humble home on 26 Aug 2026.
Hello {invitation_list[-1].title()}, we will like to invite to our new humble home on 26 Aug 2026.
'''
print(updated_message)
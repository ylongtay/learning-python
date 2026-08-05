# Challenge 1: E-Commerce shopping cart manager

# Scenario: To manage an online shopping cart system. 
# A customer starts with a few items, adds a new one, changes their mind about a product, and then checks out the last added item.

# Task 1: Initialize a list named cart with four items: "laptop", "mouse", "keyboard", and "monitor".
# Task 2: Customer decides to replace "mouse" with "trackpad" using index assignment.

cart = ["laptop", "mouse", "keyboard", "monitor"]
cart[1] = "trackpad"
# print(cart)

# Task 3: Customer adds "headphones" to the end of the list using .append().
# Task 4: Customer wants to place a priority item "webcam" at the front (index 0) of the cart using .insert().

cart.append("headphones")
cart.insert(0, "webcam")
# print(cart)

# Task 5: Customer changes their mind about buying "keyboard". Remove it using .remove().
# Task 6: Customer decides to buy the last item added right now! Remove and store the last item using 
# .pop() into a variable called purchased_item.
# Task 7: Print a summary using f-strings showing:
# - The item that was just purchased.
# - The remaining items in the cart.
# - The total count of remaining items using len().

cart.remove("keyboard")
purchased_item = cart.pop()
purchased_summary = f"""=== CART UPDATE ===
Item Purchased: {purchased_item}
Current Cart: {cart}
Total Items Left: {len(cart)}"""
print(purchased_summary)

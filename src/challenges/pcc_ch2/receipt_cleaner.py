# Challenge 1: The E-Commerce Receipt & Cleaner

# Scenario: You are building a backend script for a retail store. 
# The system received raw customer input with messy spacing and capitalization, 
# alongside an internal product URL.

customer_name_entered = "   jAnE dOe   "
product_url = "https://mystore.com/products/bluetooth_headsets"
item_price = 79.99
quantity = 3

# Task 1: Clean up the customer's name by stripping and change to title case
customer_name_clean = customer_name_entered.lower().title().strip()

# Task 2: Extract the clean product name from the URL by removing prefix
product_name = product_url.removeprefix("https://mystore.com/products/")

# Task 3: Calculate the total cost before tax and with a 9 % GST included
subtotal = item_price * quantity
total_cost = subtotal * 1.09

# Task 4: Print a formatted receipt
print(f"=== OFFICIAL RECEIPT === \nCustomer:\t{customer_name_clean}\nItems:\t{product_name}\nQuantity:\t{quantity}\nSubtotal:\t{subtotal}\nTotal (incl.GST):\t{total_cost}")

# update to optimize code for task 4
# Tip 1: use (''') instead of (\n) make code display better 
# Tip 2: use :.2f in float value to display in 2 decimal place

receipt = f'''\n=== OFFICIAL RECEIPT === 
Customer:\t{customer_name_clean}
Items:\t{product_name}
Quantity:\t{quantity}
Subtotal:\t{subtotal:.2f}
Total (incl.GST):\t{total_cost:.2f}'''
print(receipt)

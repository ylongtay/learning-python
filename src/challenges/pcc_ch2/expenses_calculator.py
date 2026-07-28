# Challenge 2: Road Trip Expense & Fuel Calculator

# Scenario: Calculates estimated gallons and fuel cost for a road trip.

# Task 1: Define constants in ALL_CAPS for fuel efficiency
MILES_PER_GALLON = 28.5
GAS_PRICE_PER_GALLON = 3.75

# Task 2: Use Multiple Assignment to initialize variables
distance_in_miles, input_driver_name, input_destination = 1_250, "  ALEX ", "johor bahru"

# Task 3: Clean up driver name and title case destination
cleaned_name = input_driver_name.strip().title()
city_destination = input_destination.title()

# Task 4: Calculate total gallons needed and total gas cost
est_gallon_needed = distance_in_miles / MILES_PER_GALLON
est_fuel_cost = est_gallon_needed * GAS_PRICE_PER_GALLON

# Task 5: Print a clean summary statement explaining the trip expenses. 
# Include a comment (#) at the top of your script explaining what the script does.

# Print line below show how the calculator will display
expense_summary = f'''Trip Expense Summary for {cleaned_name}
Destination:\t{city_destination}\n
Total Distance:\t{distance_in_miles}\n miles
Estimated Gallons Needed:\t{est_gallon_needed:.2f}\n
Estimated Fuel Cost:\t{est_fuel_cost:.2f}\n'''
print(expense_summary)
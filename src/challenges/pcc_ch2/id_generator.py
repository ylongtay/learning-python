# Challenge 3: Corporate Email & ID Badge Generator

# Scenario: Create HR system which automatically generate company email
# and employee badge profile from registration

# Task 1: Create variable that assigned to the registered text file
raw_filename = "employee_john_smith_profile.txt"

# Task 2: Clean the file name leaving only the name
employee_name = raw_filename.removeprefix("employee_").removesuffix("_profile.txt")

# Task 3: Store name in firstname and lastname variables
first_name = employee_name.removesuffix("_smith")
last_name = employee_name.removeprefix("john_")

# Task 4: Create a corporate email address
email = f"{first_name}.{last_name}@company.com"

# Task 5: Create a badge name display employee's name in CAPS
# badge_name = f"{first_name.upper()} {last_name.upper()}"
badge_name = f"{first_name} {last_name}".upper()
formatted_name = f"{first_name} {last_name}".title()

# Task 6: Print out an employee onboarding profile card.
printout = f"""--- HR ONBOARDING SYSTEM ---
Employee Name:\t{badge_name}
Formatted Name:\t{first_name.title()} {last_name.title()}
Company Email:\t{email}
Source File Processed:\t{raw_filename.removesuffix(".txt")}"""
print(printout)

# Optimized display with spaces instead of tab and use formatted_name variable
op_badge_print = f"""--- HR ONBOARDING SYSTEM ---
Employee Name:         {badge_name}
Formatted Name:        {formatted_name}
Company Email:         {email}
Source File Processed: {raw_filename.removesuffix(".txt")}"""
print(op_badge_print)
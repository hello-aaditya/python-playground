# Grocery Shopping Planner

# Prompt for user's name
name = input("ENTER YOUR NAME: ")

# Prompt for number of items
items_count = int(input("ENTER TOTAL NUMBER OF ITEMS: "))

# Prompt for total budget
total_budget = float(input("ENTER TOTAL BUDGET: "))

# Prompt for discount coupon (True/False)
has_coupon_input = input("DO YOU HAVE A COUPON (True/False): ")
has_coupon = has_coupon_input == "True"

# Print Summary
print(f"GROCERY SHOPPING SUMMARY: ")
print(f"NAME: {name}")
print(f"NUMBER OF ITEMS: {items_count}")
print(f"TOTAL BUDGET: ${total_budget}")
print(f"HAS DISCOUNT COUPON: {has_coupon}")
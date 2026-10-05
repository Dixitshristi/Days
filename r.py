# Raw text inputs
raw_units = "25"
raw_unit_price = "19.99"

# 1. Type Casting
clean_units = int(raw_units)            # '25' -> 25 (int)
clean_unit_price = float(raw_unit_price) # '19.99' -> 19.99 (float)

# 2. Mathematical Calculation
total_amount = clean_units * clean_unit_price

# 3. Cast back to string to build a message
confirmation = "Total order amount is: " + str(total_amount)

print(confirmation)
print("Type of total_amount:", type(total_amount))

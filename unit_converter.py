# Get the weight value first
weight_str = input("Please enter your weight: ")
weight_value = float(weight_str)
# Get the unit
unit = input("Please enter L or K as the unit: ")
# Use an if/elif/else block to perform the correct action
# We convert the 'unit' variable to uppercase for the comparison.
if unit.upper () == 'L':
# This block only runs if the unit is 'L' or 'l'
# The original weight was in punds, so we need to convert it
    weight_in_kg = weight_value * 0.453592
    print(f"The weight in kilograms is: {weight_in_kg} ")
elif unit.upper() == 'K':
# This block only runs if the unit is 'K' or 'k'.
# If the weight is already in kg, we will just display it.
    print(f"The weight is already {weight_value} kg.")  
else: 
# This blocks runs if the ser typed anything else.
    print("Invalid unit. Please enter L o K.")

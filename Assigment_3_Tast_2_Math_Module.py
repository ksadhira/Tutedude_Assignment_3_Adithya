'''Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.'''



import math

input_number = float(input("Enter a number: "))

sq_root = math.sqrt(input_number)
natural_log = math.log(input_number)
sine_value = math.sin(input_number)

print(f"Square root of {input_number}: {sq_root}")
print(f"Natural logarithm of {input_number}: {natural_log}")
print(f"Sine of {input_number} (in radians): {sine_value}")


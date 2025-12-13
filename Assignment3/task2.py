'''' Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''
import math

num = int(input("Enter a number: "))
output = math.sqrt(num)
print(f"Square root : {output}")
output = math.log(num)
print(f"Logarithm : {output}")
output = math.sin(num)
print(f"Sine : {output}")


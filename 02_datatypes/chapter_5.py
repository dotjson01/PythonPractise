import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 45
current_temp = 15.999999999999999999999

print(f"Ideal Temp: {ideal_temp}")
print(f"Current Temp: {current_temp}")
print(f"Difference in temp: {ideal_temp - current_temp}")
print(sys.float_info)
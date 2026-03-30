"""

Program Description:
This program will calculate the perimeter, area, and type of triangle.

Author: Sabirin Mohamed
"""
# This asks the user to input the lengths of the corresponding side for each triangle:
length_side_A = int(input('Please enter the length of side A of the triangle (in meters): '))
length_side_B = int(input('Please enter the length of side B of the triangle (in meters): '))
length_side_C = int(input('Please enter the length of side C of the triangle (in meters): '))

# This is will take the user input and add the numbers together, resulting in the perimeter of the triangle:
perimeter = length_side_A + length_side_B + length_side_C

# This outputs the perimeter of the triangle:
print('The perimeter of the triangle is:', perimeter,'m')

# This is the formula to calculate the semi perimeter, s:
s = 1/2 * (length_side_A + length_side_B + length_side_C)

# This is the formula to calculate the area of a triangle:
area =  s * (s - length_side_A) * (s - length_side_B) * (s - length_side_C)
import math
square_root = math.sqrt(area)

# This will output the area of the triangle:
print('The area of the triangle is',square_root,'m^2')

# This will output the type of triangle:
if length_side_A**2 + length_side_B**2 == length_side_C**2:
    print('It is a Right Triangle')
elif length_side_A**2 + length_side_B**2 > length_side_C**2:
    print('It is an Acute Triangle')
elif length_side_A**2 + length_side_B**2 < length_side_C**2:
    print('This is an Obtuse Triangle')

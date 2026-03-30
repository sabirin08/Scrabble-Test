"""

Program Description:
This program is takes in three integers and outputs the median value.

Author: Sabirin Mohamed
"""
first_number = int(input('Please enter the first number: '))
second_number = int(input('Please enter the second number: '))
third_number = int(input('Please enter the third number: '))


if second_number < first_number and first_number < third_number:
    print(f'The median number is {first_number}')
elif third_number < first_number and first_number < second_number:
    print(f'The median number is {first_number}')
if third_number < second_number and second_number < first_number:
    print(f'The median number is {second_number}')
elif first_number < second_number and second_number < third_number:
    print(f'The median number is {second_number}')
if second_number < third_number and third_number < first_number:
    print(f'The median number is {third_number}')
elif first_number < third_number and third_number < second_number:
    print(f'The median number is {third_number}')

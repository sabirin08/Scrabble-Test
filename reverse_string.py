"""

Program Description:
This program takes in a line of text as input and outputs that line of text in reverse.

Author: Sabirin Mohamed
"""
while True:
    string = input('Please enter your string: ')
    if string.lower() in ['quit']:
        break
    reversed_string = ''
    for x in range(len(string) -1, -1, -1):
        reversed_string += string[x]
    print('Reversed:', reversed_string)

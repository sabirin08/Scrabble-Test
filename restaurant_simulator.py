"""

Program Description:
This program is used to simulte a point-of-sale device for a restaurant.

Author: Sabirin Mohamed
"""
food = {
    'hot_dog': 1.50, 
    'pizza_slice': 1.99, 
    'whole_pizza': 9.95, 
    'soft_drink': 0.59,
}

hot_dogs = int(input('Please enter the number of Hot Dogs: '))
pizza_slices = int(input('Please enter the number of Pizza Slices: '))
whole_pizzas = int(input('Please enter the number of Whole Pizza: '))
soft_drinks = int(input('Please enter the number of Soft Drinks: '))

total = food['hot_dog'] * hot_dogs + food['pizza_slice'] * pizza_slices + food['whole_pizza'] * whole_pizzas + food['soft_drink'] * soft_drinks


print(f'\nThe total cost of the order is ${total}')

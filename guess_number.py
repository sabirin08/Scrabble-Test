"""

Program Description:
This program creates a guessing game that generates a random number between 1 and 100.

Author: Sabirin Mohamed
"""
import random
def random_guess():
    print('I have generated random number between 1 and 100. You will have 10 attempts to guess that number.')
    random_number = random.randint(1,100)
    for attempt in range(10):
        
        number_guessed = int(input('Guess: '))
        if number_guessed == random_number:
            print('You correctly guessed my random number!')
            break
        elif number_guessed < random_number:
            print('Your guess is less than my random number. Try again.')
        else:
            print('Your guess is greater than my random number. Try again.')
    else:
        print('Sorry, you have used all of your attempts.')
random_guess()

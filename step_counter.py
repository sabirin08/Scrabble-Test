"""

Program Description:
This program reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the steps_to_miles() function.

Author: Sabirin Mohamed
"""
class NegativeValueError(Exception):
    def __init__(self,value):
        self.value = value
def steps_to_miles():
    while True:
        try:
            val = int(input('Enter # of Steps :> '))
            if val < 0 and input:
                raise NegativeValueError('Exception: Negative Step Count Entered')
            miles = val / 2000
            print(f'{miles:.2f} miles')
        except ValueError:
            print('Exception: Non-Numeric Value Entered')
        except NegativeValueError as e:
            print(e)
        
        
steps_to_miles()      

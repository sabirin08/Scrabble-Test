"""

Program Description:
This program uses a database to store information and allows the user to input a unique identifier to access a record in order to sort, add, remove, update, and print. 

Author: Sabirin Mohamed
"""
# Create a database using dictionaries that stores two tables as records:
database = {
    'students': [
        {'Name': 'John Smith', 'ID': '299231', 'Age': 18, 'Year': 'Freshman', 'Eye Color': 'Brown'},
        {'Name': 'Mary Allen', 'ID': '908654', 'Age': 19, 'Year': 'Sophmore','Eye Color': 'Blue'},
        {'Name': 'James Young', 'ID': '807654', 'Age': 21, 'Year': 'Junior', 'Eye Color': 'Hazel'},
        {'Name': 'Natalie Duncan', 'ID': '765432', 'Age': 19, 'Year': 'Junior', 'Eye Color': 'Green'},
        {'Name': 'Taylor Swift', 'ID': '654321', 'Age': 22, 'Year': 'Senior', 'Eye color': 'Gray'}
    ],
    'schedule': [
        {'Course': 'CSC 1301', 'Instructor': 'Reggy Fernbank', 'Age': 29, 'Classroom': 'Aderhold 024', 'Office': '55 Park Place'},
        {'Course': 'MATH 1113', 'Instructor': 'Johnny Dunk', 'Age': 30, 'Classroom': 'Classroom South 129', 'Office': '25 Park Place'},
        {'Course': 'ENGL 2101', 'Instructor': 'Barbara Hanes', 'Age': 54, 'Classroom': 'Langdale Hall 312','Office': '69 Park Place' },
        {'Course': 'SCOM 2211', 'Instructor': 'Martha Stewart', 'Age': 42, 'Classroom': 'Sparks Hall 265', 'Office': '55 Park Place'},
        {'Course': 'BIOL 1211', 'Instructor': 'Kaya Hughes', 'Age': 25, 'Classroom': ' Petite Science Center 900', 'Office': '39 Park Place'},
    ]
}


# Create seperate functions for each Menu Command:

#Add Command:
def add_record(table, data):
    database[table].append(data)
    
#Remove Command:
def remove_record(table, record_id):
    for record in database[table]:
        if record['ID'] == record_id:
            database[table].remove(record)
            return True
    return False

#Print Command:
def print_records(table, record_id=None):
    if record_id is not None:
        for record in database[table]:
            if record['ID'] == record_id:
                return [record]
        return None
    else:
        return database[table]

#Update Command:
def update_record(table, record_id, column, new_value):
    for record in database[table]:
        if record['ID'] == record_id:
            if column in record:
                record[column] = new_value
                return True
    return False

# Create a loop that will execute the functions above:
while True:
    command = input('Menu: \n1- Add \n2- Remove \n3- Print \n4- Update \n5- Quit \nPlease type in your selected menu: ').lower()
# Create a stop word for the user to stop the code:
    if command in ['quit', 'q']:
        break
# Adds a new record:
    elif command.startswith('add student') or command.startswith('as') or command.startswith('add'):
        table = input("Enter table name: ")
        data = {}
        for column in database[table][0].keys():
            data[column] = input(f'Enter {column}: ')
        add_record(table, data)
        print('Record added.')
# Removes a specific record:
    elif command.startswith('remove') or command.startswith('rs') or command.startswith('remove'):
        table = input('Enter table name: ')
        record_id = input('Enter record ID to remove: ')
        if remove_record(table, record_id):
            print('Record removed.')
        else:
            print('Record not found.')
#Prints the entire record:
    elif command.startswith('print student') or command.startswith('ps') or command.startswith('print'):
        table = input('Enter table name: ')
        information = 'information' in command
        if information:
            record_id = input('Enter record ID to print: ')
            record = print_records(table, record_id)
            if record is not None:
                print(record)
            else:
                print('Record not found.')
        else:
            records = print_records(table)
            if records:
                for record in records:
                    print(record)
            else:
                print('No records found.')
# Updates a specific record record:
    elif command.startswith('update student') or command.startswith('us') or command.startswith('update'):
        table = input('Enter table name: ')
        record_id = input('Enter record ID to update: ')
        column = input('Enter column to update: ')
        new_value = input('Enter new value: ')
        if update_record(table, record_id, column, new_value):
            print('Record updated.')
        else:
            print('Record not found or column does not exist.')
    else:
        print('Invalid command. Please try again.')

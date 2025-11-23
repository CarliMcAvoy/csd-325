"""
Carli McAvoy
Module 8.2
JSON Practice
"""

import json

with open('student.json') as f:
    data = json.load(f)


def display_loop():

    for item in data:
        print(f'{item['L_Name']}, {item['F_Name']} : ID = {item['Student_ID']}, Email = {item['Email']}')


def display_values():

    print('This is the original student list:\n')

    display_loop()

    add_values()

    append_data()


def add_values():

    new_values = {
        "F_Name": "Carli",
        "L_Name": "McAvoy",
        "Student_ID": 82094,
        "Email": "cmcavoy@my365.bellevue.edu"
    }

    data.append(new_values)

    print('\nThis is the updated student list:\n')

    display_loop()


def append_data():

    with open('student.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print('\nSuccessfully updated JSON file.')


display_values()

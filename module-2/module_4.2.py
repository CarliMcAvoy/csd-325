"""
Carli McAvoy
August 31, 2025
Module 4.2
"""

"""
Program demonstrates use of functions, local variables, global variables, and the try/except functions
to print conversions
"""


def main():
    global miles
    intro()
    try:
        miles=float(input('How many miles did you travel? '))
        m_to_km(miles)
    except ValueError:
        print('ERROR: Value must be in numerical form.')

def intro():
    print('This program will convert miles to kilometers. '+
          'For reference, the conversion is: '+
          '1 mile = 1.60934 kilometers.')

def m_to_km(mi):
    kilometers=mi*1.60934
    print(f'You travel {kilometers} kilometers when you travel {miles} miles.')

main()



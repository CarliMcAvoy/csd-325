"""
Carli McAvoy
Module 7.2
Using Unit Testing to test python code
"""
def format_city_country(city, country, population='', language=''):

    if population and language:
        string = f'{city}, {country} - population {population}, {language}'
    elif population:
        string = f'{city}, {country} - population {population}'
    elif language:
        string = f'{city}, {country}, {language}'
    else:
        string = f'{city}, {country}'
    return string.title()

def city_country():

    while True:

        print('Enter "q" at any time to quit.')
        city = input('\nEnter the name of a city: ')
        if city == 'q':
            break

        country = input('Enter the name of a country: ')
        if country == 'q':
            break

        population = input('Enter the population: ')
        if population == 'q':
            break

        language = input('Enter the native language: ')
        if language == 'q':
            break

        format_string = format_city_country(city, country, population, language)

        print(f'{format_string}')

city_country()


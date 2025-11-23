import unittest
from city_functions import format_city_country

def test_city_country():

    format_string = format_city_country('berlin', 'germany')

    assert format_string == 'Berlin, Germany'

test_city_country()
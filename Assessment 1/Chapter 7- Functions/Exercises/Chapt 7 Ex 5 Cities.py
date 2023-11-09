# A funtion that accepts the name of a city and its country
def describe_city(city, country='UAE'):     # Parameter with a country default value
    print(city.title(), 'is in', country.title() + '.')


# Function for three different cities, with one of which is not in the default country.
describe_city('dubai')
describe_city('abu dhabi')
describe_city('cdo', 'philippines')

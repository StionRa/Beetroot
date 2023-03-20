def make_country(name, capital, **country_info):
    country = {}
    country['name'] = name
    country['capital'] = capital
    for key, value in country_info.items():
        country[key] = value
    return country

my_country = make_country('Ukraine', 'Kyiv', population = 2962180, founded = "482 CE")
print(my_country)

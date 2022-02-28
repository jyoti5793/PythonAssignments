countries = ['Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran']

def check_country_starts_with_A(countries):
    country_startswith_A = []
    for country in countries:
        if country.startswith('A'):
            country_startswith_A.append(country)
    return country_startswith_A
print(check_country_starts_with_A(countries))
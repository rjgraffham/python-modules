# 6.1  Person dictionary
catherine = {
    "first_name": "Catherine",
    "last_name": "Graffham",
    "age": 31,
    "city": "Coventry"
}

print(f"First name: {catherine['first_name']}")
print(f"Last name: {catherine['last_name']}")
print(f"Age: {catherine['age']}")
print(f"City: {catherine['city']}")


print("---")  # Section divider for output


# 6.2  Favourite numbers
favourite_numbers = {
    "Catherine": 21,
    "Halley": 7,
    "Robert": 77,
    "Amanda": 69,
    "Douglas Adams": 42
}

print(f"Catherine's favourite number is {favourite_numbers['Catherine']}.")
print(f"Halley's favourite number is {favourite_numbers['Halley']}.")
print(f"Robert's favourite number is {favourite_numbers['Robert']}.")
print(f"Amanda's favourite number is {favourite_numbers['Amanda']}.")
print(f"Douglas Adams' favourite number is {favourite_numbers['Douglas Adams']}.")


print("---")  # Section divider for output


# 6.3  Rivers
rivers = {
    "nile": "egypt",
    "seine": "france",
    "thames": "england"    
}

print("River facts:")
for river in rivers:
    print(f"- The {river.title()} is in {rivers[river].title()}.")

print("Rivers:")
for river in rivers:
    print(f"- {river}")

print("Countries:")
for country in rivers.values():
    print(f"- {country}")


print("---")  # Section divider for output


# 6.4  Pets
pets = [
    {
        "name": "Lucky",
        "animal": "cat",
        "fur_colour": "black",
        "owner": "Mark"
    },
    {
        "name": "Pepsi",
        "animal": "dog",
        "fur_colour": "white",
        "owner": "Halley"
    }
]

for pet in pets:
    print(f"{pet['name']} is a {pet['animal']} with {pet['fur_colour']} fur. {pet['name']}'s owner is {pet['owner']}.")


print("---")  # Section divider for output


# 6.5  Favourite places
favorite_places = {
    "Robert": "Birmingham",
    "Mark": "Glasgow",
    "Halley": "Coventry"
}

for person, place in favorite_places.items():
    print(f"{person}'s favourite place is {place}.")


print("---")  # Section divider for output


# 6.6  Cities
cities = {
    "Birmingham": {
        "country": "England",
        "population": 1_160_000,
        "fact": "Birmingham has more miles of canals than Venice"
    },
    "Glasgow": {
        "country": "Scotland",
        "population": 635_000,
        "fact": "Glasgow was founded by St. Mungo, patron saint of salmon"
    },
    "Coventry": {
        "country": "England",
        "population": 345_000,
        "fact": "Coventry has a statue of Lady Godiva, who reportedly rode through the city nude"
    }
}

for city, city_data in cities.items():
    print(f"{city} is a city in {city_data['country']}, with a population of approximately {city_data['population']:,}. Fun fact: {city_data['fact']}!")
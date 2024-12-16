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



print("---")  # Section divider for output


# 6.5  Favourite places


print("---")  # Section divider for output


# 6.6  Cities

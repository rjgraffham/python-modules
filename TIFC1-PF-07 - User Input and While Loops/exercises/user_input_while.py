# 7.1  Rental car
make_of_car = input("What make of car do you want?\n")
print(f"Okay, I'll see if I can find you a {make_of_car}.")


print("---")  # Section separator for output


# 7.2  Dinner group
number_in_group = int(input("How many people are in your dinner group?\n"))
if number_in_group > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Okay, your table is ready.")


print("---")  # Section separator for output


# 7.3  Divisible by 10
num = int(input("Enter a whole number: "))
if num % 10 == 0:
    print(f"{num:,} is a multiple of 10.")
else:
    print(f"{num:,} is not a multiple of 10.")


print("---")  # Section separator for output


# 7.4  Pizza toppings
while True:
    topping = input("What topping would you like to add to your pizza (or 'quit' to quit)? ").strip()
    if topping.lower() == "quit":
        print("Bye!")
        break
    else:
        print(f"Okay, I'll add {topping} to your pizza.")


print("---")  # Section separator for output


# 7.5  Ticket prices
age = int(input("How old are you (in whole years)?\n").strip())

if age < 3:
    ticket_price = 0
elif age <= 12:
    ticket_price = 10
else:
    ticket_price = 15

if ticket_price == 0:
    print("Your ticket is free.")
else:
    print(f"Your ticket is ${ticket_price}.")


print("---")  # Section separator for output


# 7.6  Infinite loop (Ctrl+C to get out)
print("Press Ctrl+C if you want to escape this infinite loop!")
while True:
    pass
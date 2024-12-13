# 4.1  Printing pizza names in a loop
my_fave_pizzas = ["pepperoni", "california chicken", "funghi"]

for kind_of_pizza in my_fave_pizzas:
    print(f"I really like {kind_of_pizza} pizza!")

print("In general, I just like pizza!")


print("---")  #  divider between sections of output


# 4.2  Printing animals with horns
animals_with_horns = ["ibex", "bison", "goat"]

for animal in animals_with_horns:
    print(f"It'd be pretty cool to meet a wild {animal}.")

print("Fun fact: All those animals have horns!")


print("---")  #  divider between sections of output


# 4.3  Printing numbers from 1 to 20
for n in range(1, 21):
    print(n)


print("---")  #  divider between sections of output


# 4.4  Making a list of numbers from 1 to 1,000,000 (inclusive),
#      verifying the ends of the list, and printing the sum.
numbers_to_a_million = list(range(1, 1_000_001))
print(f"The minimum number of the 1-1,000,000 list is {min(numbers_to_a_million)}")
print(f"The maximum number of the 1-1,000,000 list is {max(numbers_to_a_million)}")
print(f"The sum of the 1-1,000,000 list is {sum(numbers_to_a_million)}")


print("---")  #  divider between sections of output


# 4.5  Making and printing a list of multiples of 3
multiples = []
for n in range(1, 11):
    multiples.append(n * 3)

for n in multiples:
    print(n)


print("---")  #  divider between sections of output


# 4.6  Friend's pizzas extension to 4.1
friend_pizzas = my_fave_pizzas[:]
my_fave_pizzas.append("mexican chicken")
friend_pizzas.append("hawai'ian")

print("My favourite pizzas:")
for pizza in my_fave_pizzas:
    print(f"- {pizza}")

print("My friend's favourite pizzas:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

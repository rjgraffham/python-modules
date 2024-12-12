# store the message "Hello, world!" in a variable and print it
message = "Hello, World!"
print(message)

# store the message "Goodbye, world." in a variable, print it, then
# change it to "Hello again, world!" and print it again
another_message = "Goodbye, world."
print(another_message)
another_message = "Hello again, world!"
print(another_message)

# store my name in a variable, print a message including it
my_name = "Robert"
print("Hello, " + my_name + "!")

# store another name in a variable, print it in lower-/upper-/title-case
another_name = "Antony"
print("Uppercase: " + another_name.upper())
print("Lowercase: " + another_name.lower())
print("Title case: " + another_name.title())

# print the results of various arithmetic operations that result in 8
print(4 + 4)
print(16 - 8)
print(256 / 32)
print(2 * 4)
print(2 ** 3)

# store my favourite number in a variable, and print a message revealing
# that number
my_fav_number = 77
print("My favourite number? It's " + str(my_fav_number) + ".")

# 
# STRETCH
#

# print a message with an interpolated variable using an f-string
my_cat = "Lucky"
print(f"My cat's name is {my_cat}.")

# print a message with multiple variables
a = 200
b = 12
c = a * b
print(f"{a} * {b} = {c}")

# build a greeting by concatenating variables, and then print it
greeting_start = "Good"
greeting_middle = "Day"
greeting_name = "Robert"
greeting = greeting_start + " " + greeting_middle + " " + greeting_name
print(greeting)
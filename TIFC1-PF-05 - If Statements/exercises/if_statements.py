# 5.1  Conditional tests
fruit = "banana"
print("Is fruit == \"apple\"? I predict False.")
print(fruit == "apple")
print("Is fruit == \"banana\"? I predict True.")
print(fruit == "banana")
print("Is fruit < \"cherry\"? I predict True.")
print(fruit < "cherry")
print("Is fruit > \"apple\"? I predict True.")
print(fruit > "apple")

breakfast = ["sausage", "eggs"]
print("Is \"bacon\" in breakfast? I predict False.")
print("bacon" in breakfast)
print("Is \"hash browns\" in breakfast? I predict False.")
print("hash browns" in breakfast)
print("Are there three or more items in breakfast? I predict False.")
print(len(breakfast) >= 3)
print("Is breakfast alphabetically ordered? I predict False.")
print(breakfast == sorted(breakfast))
print("After sorting, is breakfast alphabetically ordered? I predict True.")
breakfast.sort()
print(breakfast == sorted(breakfast))
print("After sorting, is \"eggs\" the first item of breakfast? I predict True.")
print(breakfast[0] == "eggs")


print("---")  # Section divider for output


# 5.2  Stage of life
age = input("How many years old are you? (Positive whole numbers only.)\n").strip()
try:
    age = int(age)

    if age < 0:
        raise ValueError()

    if age < 2:
        life_stage = "a baby"
    elif age < 4:
        life_stage = "a toddler"
    elif age < 13:
        life_stage = "a kid"
    elif age < 20:
        life_stage = "a teenager"
    elif age < 65:
        life_stage = "an adult"
    else:
        life_stage = "an elder"

    print(f"You are {life_stage}.")
except ValueError:
    print(f"'{age}' is not a positive whole number.")


print("---")  # Section divider for output


# 5.3  Favourite fruits
favorite_fruits = ["grapes", "cherries", "apples"]

if "bananas" in favorite_fruits:
    print(f"You really like bananas!")
if "grapes" in favorite_fruits:
    print(f"You really like grapes!")
if "kiwis" in favorite_fruits:
    print(f"You really like kiwis!")
if "apples" in favorite_fruits:
    print(f"You really like apples!")
if "mangos" in favorite_fruits:
    print(f"You really like mangos!")


print("---")  # Section divider for output


# 5.4  Login check
usernames = ["user01", "rjgraffham", "user99", "user43", "admin"]

for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
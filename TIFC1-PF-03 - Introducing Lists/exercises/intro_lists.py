# 2.1  artists I like, printed one by one
names = ["Tame Impala", "Moon Hooch", "Beats Antique", "Run the Jewels"]
print(names[0])  # Tame Impala
print(names[1])  # Moon Hooch
print(names[2])  # Beats Antique
print(names[3])  # Run the Jewels

print("---")  # Print divider between parts

# 2.2  messages about artists one by one
print(f"I like to listen to music by {names[0]}")
print(f"I like to listen to music by {names[1]}")
print(f"I like to listen to music by {names[2]}")
print(f"I like to listen to music by {names[3]}")

print("---")  # Print divider between parts

# 2.3  statement about book or movie, and message to author/director
media_names = ["Angels and Demons", "The Dark Tower", "Agatha H and the Airship City", "Phil and Kaja Foglio"]
print(f"I liked {media_names[1]} when I last read it")
print(f"I enjoyed the character writing of {media_names[2]} by {media_names[3]}")

print("---")  # Print divider between parts

# 2.4  The Dinner Problem
# 2.4.1  Initial invites
dinner_guests = ["Catherine", "Halley", "Lyn"]
print(f"{dinner_guests[0]}, you are invited to dinner.")
print(f"{dinner_guests[1]}, you are invited to dinner.")
print(f"{dinner_guests[2]}, you are invited to dinner.")

print("---")  # Print divider between parts

# 2.4.2  A guest can't make it
missing_guest = dinner_guests[0]
print(f"{missing_guest} can't make it.")

print("---")  # Print divider between parts

# 2.4.3  A replacement guest and new invites
dinner_guests[0] = "Jodie"
print(f"{dinner_guests[0]}, you are invited to dinner.")
print(f"{dinner_guests[1]}, you are invited to dinner.")
print(f"{dinner_guests[2]}, you are invited to dinner.")

print("---")  # Print divider between parts

# 2.4.5  More space, so extra guests
print("A bigger table is available, so I'm inviting more guests.")
dinner_guests.insert(0, "Hugh")
dinner_guests.insert(2, "Amanda")
dinner_guests.append("Phoebe")
print(f"{dinner_guests[0]}, you are invited to dinner.")
print(f"{dinner_guests[1]}, you are invited to dinner.")
print(f"{dinner_guests[2]}, you are invited to dinner.")
print(f"{dinner_guests[3]}, you are invited to dinner.")
print(f"{dinner_guests[4]}, you are invited to dinner.")
print(f"{dinner_guests[5]}, you are invited to dinner.")

print("---")  # Print divider between parts

# 2.4.6  Bigger table won't be available, so uninvite the last 4 guests on the list
print("The bigger table won't arrive after all, so I'm reducing the guest list.")
print(f"Sorry {dinner_guests.pop()}, you're no longer invited.")
print(f"Sorry {dinner_guests.pop()}, you're no longer invited.")
print(f"Sorry {dinner_guests.pop()}, you're no longer invited.")
print(f"Sorry {dinner_guests.pop()}, you're no longer invited.")
print(f"{dinner_guests[0]}, you're still invited.")
print(f"{dinner_guests[1]}, you're still invited.")

print("---")  # Print divider between parts

# 2.4.7  Print number of guests before and after removing the last two guests
print(f"There are {len(dinner_guests)} guests before removing two.")
del dinner_guests[1]
del dinner_guests[0]
print(dinner_guests)
print(f"There are {len(dinner_guests)} guests after removing two.")

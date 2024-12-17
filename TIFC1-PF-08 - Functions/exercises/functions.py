# 8.1  Simple message function
def display_message():
    print("In this module, we are learning about functions.")

display_message()


print("---")  # Section separator for output


# 8.2  Favourite book printer
def favorite_book(title):
    print(f"One of my favourite books is {title}.")

favorite_book("Gideon the Ninth")


print("---")  # Section separator for output


# 8.3  Shirt info
def make_shirt(size="large", message="I love Python."):
    print(f"A {size} shirt with the message \"{message}\"")

make_shirt("small", "I wrote a shirt function and all I got was this shirt")
make_shirt(message="This shirt has the message passed first", size="medium")
make_shirt()
make_shirt("medium")


print("---")  # Section separator for output


# 8.4  Describe city
def describe_city(city, country="England"):
    print(f"{city} is in {country}")

describe_city("Birmingham")
describe_city("Coventry")
describe_city("Helsinki", "Finland")

print("---")  # Section separator for output


# 8.5  Album description
def make_album(artist_name, album_title, track_count=None):
    album = {
        "artist": artist_name,
        "title": album_title,
    }

    if track_count is not None:
        album["tracks"] = track_count

    return album

print(make_album("Daft Punk", "Random Access Memories"))
print(make_album("MGMT", "Oracular Spectacular"))
print(make_album("Jay-Z", "The Blueprint", 13))
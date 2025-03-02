zip_ = '''The zip() function takes two or more iterables (like lists or tuples) and combines them into a single iterable of tuples,
where each tuple contains elements from each iterable at the corresponding index.
If the iterables are of different lengths, zip() stops when the shortest iterable is exhausted. It returns zip object.'''
# Syntax is: zip(iterable1, iterable2, ...)
enumerate_ = '''The enumerate() function adds a counter to an iterable and returns it as an enumerate object,
which yields pairs of the form (index, value). It returns enumerate object.'''
# Syntax is: enumerate(iterable, start=0)
# Here are ones of it...

# Pairing and Sorting.

students = ("Anna", "Ben", "Chris", "Dana")
scores = (85, 92, 78, 90)
zipped = zip(students, scores)
sorted_ = sorted(zipped, key = lambda x: x[1], reverse = True)
convert_back = tuple(zip(*sorted_))
print(convert_back)

# Given a tuple of items, use enumerate() to find and print the indices of all items that contain the letter "a".

items = ("Apple", "Orange", "Grapes", "Berry", "Banana", "Cherry")
indexed = enumerate(items)
for index, item in indexed:
    print(f'Item {item} found at index {index}') # it's f-string, more usefull ).

# Use zip() to create a list of tuples where each tuple contains (name, age, city), convert this into a dictionary where names are keys and values are (age, city).

names = ("Liam", "Olivia", "Noah", "Emma")
ages = (23, 27, 22, 24)
cities = ("New York", "London", "Berlin", "Tokyo")
zipped = zip(names, ages, cities)
new_dict = {x: (a, b) for x, a, b in zipped}
print(new_dict)

# Given two tuples of player names and their scores, use zip() and enumerate() to print them as a ranked leaderboard (starting from 1).

players = ("Alice", "Bob", "Charlie", "David")
scores = (120, 95, 110, 130)
players_zip = zip(players, scores)
players_enumerate = enumerate(players_zip, start = 1)
for index, (name, score) in players_enumerate: # it's unpacking too...
    print(f'{index}. {name} - {score} points')

# You have a zipped object of tuples. Convert it back into separate tuples.

zipped_data = (("Alice", 25), ("Bob", 30), ("Charlie", 35))
def unzipping(zipped_data):
    unzipped_tuple = tuple(zip(*zipped_data))
    x, y = unzipped_tuple
    return x, y
print(unzipping(zipped_data))
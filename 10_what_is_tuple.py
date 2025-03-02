hint = '''Here is some manipulations...'''

# Unpack the first, second, and last elements into separate variables, ignore the middle elements, print the extracted variables.

data = (100, 200, 300, 400, 500)
a, b, *_, c = data
print(a, b, c)

# Print the third element, print the last element using negative indexing, print every second element starting from the first one.

my_tuple = ('Python', 'Java', 'C++', 'JavaScript', 'Go', 'Rust')
print(my_tuple[3])
print(my_tuple[::-1])
print(my_tuple[::2])

# Find the index of 50, find the index of 100.

numbers = (10, 20, 30, 40, 50, 60, 70, 80)
index_50 = numbers.index(50)
try:
    index_100 = numbers.index(100)
except ValueError:
    index_100 = None
print(index_50, index_100)

# Find how many times 'a' appears in the tuple, find how many times 'z' appears without causing an error.

elements = ('a', 'b', 'c', 'a', 'b', 'a', 'd', 'e', 'a')
count_a = elements.count('a')
try:
    count_z = elements.count('z')
except ValueError:
    count_z = None
print(count_a, count_z)

# Write a function that filters out all numbers less than 5 from the tuple and returns the sum of the remaining numbers.

tup = (1, 3, 7, 8, 2, 10)
def filter_and_sum(tup):
    new_tuple = tuple(filter(lambda x: x >= 5, tup))
    return sum(new_tuple)
print(filter_and_sum(tup))

# Write a program that combines the elements of each tuple into a single string,
# where each string is the tuple’s first element followed by the second. The result should be a list of strings.

tuple_list = [('a', 1), ('b', 2), ('c', 3)]
new_list = []
for i in tuple_list:
    word = ''
    for j in i:
        word += str(j)
    new_list.append(word)
print(new_list)

# Given a tuple of integers, write a program that calculates the sum of the elements at even indices.

tup = (10, 20, 30, 40, 50, 60)
filtered = sum(i for i in tup if tup.index(i) % 2 == 0)
print(filtered)

# Write a function that rotates the elements of a tuple n positions to the right.

def rotate_tuple(tup, n):
    if len(tup) == 0:
        return tup
    n = n % len(tup)
    return tup[-n:] + tup[:-n]
tup = (1, 2, 3, 4, 5)
n = 2
result = rotate_tuple(tup, n)
print(result)

# Write a function that returns a tuple containing the minimum and maximum values of the tuple,
# but only for the first n elements where n is a parameter passed to the function.

tup = (10, 20, 30, 40, 50)
def min_max(tup, n):
    return min(tup[:n]), max(tup[:n]) # we also pack returning variables into a tuple ).
print(min_max(tup, 3))

# Write a program that filters out all people aged under 25 and sorts the remaining people by age
# in descending order and returns the result as a list of tuples.

people = [('Alice', 25), ('Bob', 30), ('Charlie', 20), ('David', 35)]
people_2 = [(x, y) for x, y in people if y >= 25]
people_2.sort()
print(people_2)

# Write a function that compresses consecutive repeated values into a tuple of value and count.

tup = (1, 1, 2, 2, 2, 3, 3, 4)
def compress_tuple(tup):
    return tuple((x, tup.count(x)) for x in set(tup))
print(compress_tuple(tup))






range_ = '''Range is a built-in immutable sequence_type in Python.
It is not a list or tuple but a special range object that generates numbers on demand, making it memory-efficient.
It is Lazy Evaluated - stores only start, stop and step instead of generating all numbers at once'''
# Syntax is: range(start, stop, step). For start: default = 0, stop is required, for stop: default = 1
#Some exercises without range.

# Create a list of numbers from 1 to n using a while loop.

def create_list_while(n):
    i = 0
    list_of_numbers = []
    while i < n:
        i += 1
        list_of_numbers += [i]
    return list_of_numbers
print(create_list_while(10))

# Generate a list of numbers from 1 to n using recursion.

def generate_numbers(n):
    if n == 1:
        return [1]
    return generate_numbers(n - 1) + [n]
create_list = [x for x in generate_numbers(20)]
print(create_list)

# Create a list of numbers from 1 to n using recursion.

def create_list_rec(n, lst=None):
    i = 0
    list = []
    while i < n:
        i += 1
        list += [i]
    return list
print(create_list_rec(10))

# Sum the elements of a list using a loop

def sum_recursive(lst):
    sum_of_list = 0
    for i in lst:
        sum_of_list += i
    return sum_of_list
print(sum_recursive([1, 2, 3, 4, 5]))

# Square all elements in a list using map().

def square_numbers(lst):
   return list(map(lambda x: x ** 2, lst))
print(square_numbers([1, 2, 3, 4]))

# Create a list of numbers from 1 to n using a while loop.

def create_list(n):
    i = 0
    result = []
    while i < n:
        i += 1
        result += [i]
    return result
print(create_list(10))

# Here are with range. #
# Calculate the sum of a range of numbers

sum_of_range = sum(range(1, 11))
print(sum_of_range)

# Print numbers divisible by 5 in a specific range.

for i in range(5, 51):
    if i % 5 == 0:
        print(i)
#or#
for i in range(5, 51, 5):
    print(i)

# Print odd numbers in reverse order.

for i in range(19, 0, -1):
    if i % 2 == 1:
        print(i)

# Create a new list containing elements at even indices.

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
new_list = [my_list[i] for i in range(0, len(my_list) + 1, 2)]
print(new_list)
#or#
for i in range(0, len(my_list) + 1, 2):
    print(my_list[i])

# Print numbers in reverse order with a specific step.

for i in range(100, 49, -5):
    print(i)

# Create a function to check if a number is within a specific range.

def in_range(num, start, stop):
    return start >= num < stop
print(in_range(7, 7, 10))

# Create a list of numbers from 1 to n using a loop.

create_list = []
for i in range(1, 21):
    create_list.append(i)
print(create_list)
#or#
# We can use list comprehension ).

create_list_2 = [x for x in range(1, 21)]
print(create_list_2)
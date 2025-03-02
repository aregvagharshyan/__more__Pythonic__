tuple_ = '''Tuples are immutable, ordered, built-in data types in Python, meaning that once created, their elements cannot be changed.'''
#*****#
my_tuple = (1, 2, 3)
convert_into_tuple = tuple()
one_element_tuple = (1,) # without ',' it will define integer, not a tuple ).
# We can pack values into a tuple
packed = (1, 2, 3)
# We can unpack values from a tuple into variables
a, b, c = (1, 2, 3)
# Unpacking by first element
a, *lasts = (1, 2, 3)
print(a)
print(lasts)
# Ignoring by first element
a, *_ = (1, 2, 3)
print(a)
print(lasts)
# methods
my_tuple.count(2) # Returns the number of times a specified element appears
my_tuple.index(2) # Returns the index of the first occurrence of a specified element
# indexing and slicing
print(my_tuple[1])
print(my_tuple[1:3])
# Tuples can be used to pass multiple values to functions.
def print_values(tup):
    a, b, c = tup # we unpacked in this line ).
    print(a, b, c)
print_values((1, 2, 3))
# Merging tuples by using + operator, it will return a new tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2






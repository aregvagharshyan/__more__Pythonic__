set_ = '''A set in python is an mutable, unordered collection of unique elements. it's useful when you need to store
items without duplicates and perform operations like union, intersection, difference.'''
#*****#
my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
empty_set = set()  # Use set(), because {} creates an empty dictionary
# methods
my_set.add(5) #Adds an element to the set
my_set.remove(6) #Removes an element (raises error if not found)
my_set.discard(5) #Removes an element (no error if not found)
my_set.pop() #Removes a random element
my_set.clear()	#Removes all elements
my_set.union(my_set_2)	#Combines sets (returns new set)
my_set.intersection(my_set_2)	#Common elements (returns new set)
my_set.difference(my_set_2)	#Elements in set1 but not in set2
my_set.symmetric_difference(my_set_2)	#Elements in either set but not both
my_set.issubset(my_set_2)	#Checks if set1 is a subset of set2
my_set.issuperset(my_set_2)	#Checks if set1 is a superset of set2
# operators
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection: {3, 4}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric Difference: {1, 2, 5, 6}






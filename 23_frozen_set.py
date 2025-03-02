frozen_set = '''A frozenset is an immutable version of a set. Unlike regular sets, which are mutable and can be
modified after creation, a frozenset cannot be changed once it is created. This makes it hashable,
meaning it can be used as a key in dictionaries or stored inside other sets.'''
#*****#
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(type(A))
# exercises for it #
# Write a function that takes multiple lists and returns a frozenset containing only the unique elements across all lists: #

def unique_elements(*lists):
    new_set = set()
    for i in lists:
        for j in i:
            new_set.add(j)
    return frozenset(new_set)

print(unique_elements([1, 2, 3], [3, 4, 5], [5, 6, 7]))

# Given two frozenset objects, perform the following operations and return the results in a dictionary.

def frozenset_operations(fs1, fs2):
    fs1 =set(fs1)
    fs2 = set(fs2)
    new_dict = {}
    new_dict['union'] = frozenset(fs1.union(fs2))
    new_dict['intersection'] = frozenset(fs1.intersection(fs2))
    new_dict['difference'] = frozenset(fs1.difference(fs2))
    new_dict['symmetric_difference'] = frozenset(fs1.symmetric_difference(fs2))
    return new_dict

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])

print(frozenset_operations(fs1, fs2))

# Write a function that takes two frozenset objects and determines subset or a supersat?, return results in a dictionary.

def check_subset_superset(fs1, fs2):
    new_dict = {}
    fs1 = set(fs1)
    fs2 = set(fs2)
    new_dict['is_subset'] = fs1.issubset(fs2)
    new_dict['is_supersat'] = fs1.issuperset(fs2)
    return new_dict

fs1 = frozenset([1, 2])
fs2 = frozenset([1, 2, 3, 4])

print(check_subset_superset(fs1, fs2))

# Given a list of tuples, return a frozenset of unique tuples.

def unique_tuples(lst):
    return frozenset(lst)

tuples_list = [(1, 2), (3, 4), (1, 2), (5, 6)]

print(unique_tuples(tuples_list))

# Write a function that takes a sentence and returns a frozenset of unique words (case-insensitive).

def unique_words(sentence):
    return frozenset(sentence.split())

print(unique_words("Python is great and Python is powerful"))

# You have a dictionary of product prices. Convert it into an immutable lookup table using frozenset and allow efficient price lookup.

def create_lookup(prices):
   return frozenset(prices.items())

prices = {'apple': 100, 'banana': 50, 'orange': 80}
lookup = create_lookup(prices)

print(next((price for product, price in lookup if product == 'banana'), None))








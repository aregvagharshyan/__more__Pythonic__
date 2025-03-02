hint = '''And manipulations for set...'''

# Count the unique elements in the list.

def count_unique(lst):
    return len(set(lst))
print(count_unique([1, 2, 3, 2, 1, 4]))

# Check if all elements in sublist exist in mainlist.

def all_exist(sublist, mainlist):
    return set(sublist).issubset(set(mainlist))
print(all_exist([1, 2], [1, 2, 3, 4]))
print(all_exist([1, 5], [1, 2, 3, 4]))

# Find the common elements between two lists.

def common_elements(lst1, lst2):
    return set(lst1).intersection(set(lst2))
print(common_elements([1, 2, 3], [2, 3, 4]))

# Find elements in lst1 that are not in lst2.

def difference_elements(lst1, lst2):
    return set(lst1).difference(set(lst2))
print(difference_elements([1, 2, 3, 4], [3, 4, 5]))

# Find elements that are in either lst1 or lst2, but not both.

def symmetric_difference_elements(lst1, lst2):
    return set(lst1).symmetric_difference(set(lst2))
print(symmetric_difference_elements([1, 2, 3], [3, 4, 5]))

#  Check if set1 is a subset, superset, or neither of set2.

def check_subset_superset(set1, set2):
    set_subset_1 = set(set1)
    set_supersat_2 = set(set2)

    if set_subset_1.issubset(set_supersat_2) is True:
        return f'Set 1 is a subset'
    elif set_subset_1.issuperset(set_supersat_2) is True:
        return f'Set 1 is a superset'
    else:
        return f'No Relation'

print(check_subset_superset({1, 2}, {1, 2, 3, 4}))
print(check_subset_superset({1, 2, 3, 4}, {2, 3}))
print(check_subset_superset({1, 2}, {3, 4}))

# Modify sets and perform various set operations like union, intersection, and difference.

A = {1, 2, 3}
B = {3, 4, 5}
A.add(6)
B.remove(3)
union = A | B
intersection = A & B
difference = A - B
print(A)
print(B)
print(union)
print(intersection)
print(difference)

# for me )

my_set = {1, 2, 3, 4}
if 3 in my_set:
    print("Yes, it's have a access by name")

#

new_set = set()
new_set.add('apple')
new_set.add('banana')
new_set.add('cherry')
new_set.pop()
print(new_set)

# Perform union, intersection, difference, and symmetric difference using method calls.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union = A.union(B)
intersection = A.intersection(B)
case_1 = A.difference(B)
case_2 = B.difference(A)
case_3 = A.symmetric_difference(B)

# Check subset, or superset.

X = {2, 4}
Y = {1, 2, 3, 4, 5}
issubset = X.issubset(Y)
issuperset = Y.issuperset(X)

# Demonstrate set copy, clearing, and element removal.

set_of_numbers = {10, 20, 30, 40}
set_of_numbers.add(60)
set_of_numbers.remove(30)
copy_of_set = set_of_numbers.copy()
set_of_numbers.clear()
print(set_of_numbers)
print(copy_of_set)

# Convert a sentence into a set of unique words.

sentence = "Python is great and Python is fun"
set_of_sentence = set(sentence.split())
print(set_of_sentence)

# Find intersection between three sets.

S1 = {1, 2, 3, 4, 5}
S2 = {3, 4, 5, 6, 7}
S3 = {5, 6, 7, 8, 9}
int_S1 = S1.intersection(S2, S3)
print(int_S1)

# Find missing and extra values between two sets.

expected = {'Alice', 'Bob', 'Charlie', 'David'}
actual = {'Alice', 'Bob', 'Eve'}
expected_missing = expected.difference(actual)
extra_actual = actual.difference(expected)

# Count the unique characters in a string.

text = "apple banana apple orange banana apple mango"
list_text = text.split()
set_text = set(list_text)
print(len(set_text))

# Union, intersection, difference like operations.

first = {3,3,3,4}
second = {4, 5, 5, 5}
union_handmade = first | second
intersection_handmade  = first & second
difference_handmade = first - second

# Remove duplicates from a list.

def remove_duplicates(lst):
    set_of_list = set(lst)
    list_of_set = list(set_of_list)
    return list_of_set
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
print(remove_duplicates(numbers))

# Find common words between two sentences.

def common_words(s1, s2):
    set_1 = set(s1.split())
    set_2 = set(s2.split())
    return set_1.intersection(set_2)
sentence1 = "Python is fun and powerful"
sentence2 = "Python is easy and powerful"
print(common_words(sentence1, sentence2))

# Count the unique characters in a string.

def count_unique_chars(s):
    return len(set(s))
print(count_unique_chars("hello world"))

# Unique elements in both of them, symmetric_difference.

def unique_elements(set1, set2):
    return set1.symmetric_difference(set2)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(unique_elements(A, B))

# Write programme that checks uniqueness.

def is_unique(lst):
    return len(set(lst)) == len(lst)
print(is_unique([1, 2, 3, 4]))
print(is_unique([1, 2, 2, 3]))

# Find most frequent element.

def most_frequent(lst):
   new_dict = {lst.count(i): i for i in lst}
   max_count = max(new_dict.keys())
   for i, j in new_dict.items():
       if i == max_count:
           return j
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
print(most_frequent(numbers))


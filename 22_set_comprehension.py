set_comprehension = '''Set comprehension in Python is concise way to create sets.
The syntax is similar to list comprehensions but creates a set instead of a list'''
#*****#
# Syntax is: {expression for item in iterable if condition}
# exercises for it #

# Generates a set containing the squares of numbers from 1 to 10.

set_of_squares = {x ** 2 for x in range(1, 11)}
print(set_of_squares)

# Generates a set of even numbers between 1 and 20.

set_even = {x for x in range(1, 21) if x % 2 == 0}
print(set_even)

# Filters out vowels from the string 'hello world' using a set comprehension.

tuple_1 = 'a', 'e', 'i', 'o', 'u'
string_1 = 'hello world'
set_without_vowels = {z for z in string_1 if z not in tuple_1}
print(set_without_vowels)

# Creates a set of the lengths of the strings in the list.

list_1 = ["apple", "banana", "cherry"]
set_list = {len(x) for x in list_1}
print(set_list)

# Generates a set containing the negative absolute values of a list of numbers.

numbers = [1, 2, 3, -4, -5]
set_of_numbers = {-abs(x) for x in numbers}
print(set_of_numbers)

# Finds the intersection of two sets created from characters of two strings.

str_1 = 'hello'
str_2 = 'world'
set_1 = set(str_1)
set_2 = set(str_2)
intersection = set_1.intersection(set_2)
print(intersection)
#or#
set_3 = {x for x in set_1.intersection(set_2)}
print(set_3)
#or3
set_4 = {x for x in set_1 & set_2}
print(set_4)

# Generates a set containing all divisors of the number n.

n = 12
set_divisors = {x for x in range(1, n + 1) if n % x == 0}
print(set_divisors)

# Filters out words from the list that start with the letter 'a'.

list_of_strings = ["apple", "banana", "apricot", "cherry"]
set_of_list = {x for x in list_of_strings if x[0] == 'a'}
print(set_of_list)

# Set of cubes.

cube = {x ** 2 for x in range(1, 11)}

# Creates a set of odd numbers between 1 and 30.

odd = {x for x in range(1, 31) if x % 2 != 0}

# Filters out vowels and spaces from the string.

vowels_and_space = ' aioueAioue'
string = 'Aregak'
consonants = {x for x in string if x not in vowels_and_space}
print(consonants)

# Splits a sentence into words and creates a set from them.

sentence = 'Python is awesome!'
splitted = set(sentence.split())
print(splitted)

# Finds the common factors between two sets of numbers.

factor_1 = {1, 2, 3, 4, 6, 12}
factor_2 = {1, 2, 3, 6, 9, 18}
common_factors = factor_1.intersection(factor_2)
print(common_factors)

# Generates squares of even numbers between 1 and 20.

set_squares_even = {x ** 2 for x in range(1, 21) if x % 2 == 0}

# Finds words that are palindromes from a list.

words = ['Areg', 'ArrA', 'MassaM', 'Mels']
palindrome = {x for x in words if x == x[::-1]}
print(palindrome)

# Creates a set of tuples where the first value is even and the second value is odd.

set_tuples = set(tuple(zip((x for x in range(2, 11) if x % 2 == 0), (y for y in range(2, 11) if y % 2 !=0))))
print(set_tuples)

# Creates a set of tuples by pairing even numbers with odd numbers from ranges.

set_tuples = {(x, y) for x, y in zip(range(2, 11, 2), range(1, 10, 2))}
print(set_tuples)

# Creates fourth powers.

set_of_fourth = {x ** 4 for x in range(1, 11)}

# Creates a set of numbers between 1 and 50 that are divisible by both 3 and 5.

numbers = {x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0}
print(numbers)

# Creates a set of lowercase letters from a string.

string = 'AFwyhss'
set_of_string = {x for x in string if x == x.lower()}
print(set_of_string)

# Finds the intersection of words between two sentences.

sentence_1 = 'Barev brats'
sentence_2 = 'Barev axpers'
sentence_3 = set(sentence_1.split()).intersection(set(sentence_2.split()))
print(sentence_3)

# Extracts the digits from a list of numbers and creates a set.

numbers = [123, 456, 789]
new_set = set()
for i in numbers:
    for j in str(i):
        new_set.add(int(j))
print(new_set)
#or#
new_set_2 = {int(j) for i in numbers for j in str(i)}
print(new_set_2)

# Creates a set of words from the list that contain the letter 'e'.

list_of_words = ['Qaxaq', 'Peperonni']
set_with_specific_char = {x for x in list_of_words if 'e' in x}
print(set_with_specific_char)

# Computes factorials from 1 to n and stores them in a set.

n = 6
factorial = 1
new_set = set()
for i in range(1, n + 1):
    factorial *= i
    new_set.add(factorial)
print(new_set)

# Creates a set of points (x, y) on the circle with radius 5.

new_set = {(x, y) for x in range(-5, 6) for y in range(-5, 6) if x ** 2 + y ** 2 == 25}
print(new_set)

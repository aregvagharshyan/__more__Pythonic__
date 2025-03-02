filter_ = '''The filter() function filters elements from an iterable based on a function that returns
a Boolean value (True or False).'''
# Syntax is: filter(function, iterable)
map_ = '''The map() function applies a given function to each item of the iterable and returns an iterable 
(usually a map object, which can be converted to a list).'''
# Syntax is: map(function, iterable)
sorted_ = '''The sorted() function in Python is used to return a new list containing all elements of an iterable in sorted order.
It doesn’t modify the original iterable.'''
# Syntax is: sorted(iterable, key=None, reverse=False)
# Some practice of it.

# Convert a list of Celsius temperatures to Fahrenheit using map().

celsius_temps = [0, 20, 30, 40, 100]
farenhayt_temp = list(map(lambda x: x * (9 / 5) + 32, celsius_temps))
print(farenhayt_temp)

# Filter words from a list that have more than 5 characters using filter().

words = ["apple", "banana", "kiwi", "grapefruit", "pear", "strawberry"]
filtered_words = list(filter(lambda x: len(x) > 5, words))
print(filtered_words)

# Square the even numbers in a list using map() and filter().

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_square = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(even_square)

# Filter valid email addresses from a list using filter().

contacts = ["john.doe@gmail.com", "hello123", "test@company.com", "no-email"]
email = list(filter(lambda x: '@' in x, contacts))
print(email)

# Convert each word in a list to title case using map()

words = ["hello", "world", "python", "rocks"]
title_case = list(map(lambda x: x.capitalize(), words))
print(title_case)

# Filter unique even numbers from a list, then square them using map() and filter().

numbers = [2, 3, 2, 4, 5, 6, 7, 8, 8, 9]
result_of_numbers = list(map(lambda x : x ** 2, filter(lambda x: x % 2 == 0, set(numbers))))
print(result_of_numbers)

# Convert words to lowercase and remove duplicates from a list using map() and set().

words = ["Apple", "banana", "apple", "Banana", "cherry", "banana", "CHERRY"]
result_of_words = list(set(map(lambda x : x.lower(), words)))
print(result_of_words)

# Capitalize words in a sentence while excluding stopwords using map() and filter().

sentence = "The quick brown fox jumps over the lazy dog in a park"
stopwords = ["is", "and", "the", "a", "of", "in"]
result = list(map(lambda x: x.capitalize(), filter(lambda x: x not in stopwords, sentence.split())))
print(result)

# Square all digit strings in a list, filter out odd results, and sort in descending order.

data = ["hello", "42", "world", "100", "python", "35", "50"]
result = sorted([x for x in list(map(lambda x: int(x) ** 2, (filter(lambda x: x.isdigit(), data)))) if x % 2 == 0], reverse = True)
print(result)

# Filter words that are palindromes and have a length greater than 3 from a list.

words = ["madam", "noon", "car", "racecar", "apple", "level", "up"]
result = list(filter(lambda x: len(x) > 3 and x == x[::-1], words))
print(result)

# Capitalize words with more than 4 characters and sort them.

names = ["john", "Elizabeth", "ALICE", "Bob", "Catherine", "Eve"]
result = sorted([x.title() for x in names if len(x) > 4])
print(result)

# Flatten a nested list, filter out odd numbers, and square them using map() and filter().

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, [i for x in numbers for i in x])))
print(result)

# Find words containing vowels, remove duplicates, and reverse them.

words = ["sky", "hello", "world", "fly", "apple"]
vowels = 'aeiouAEIOU'
result = list(map(lambda x: x[::-1], (set([x for x in words for i in x if i in vowels]))))
print(result)

# Sum all the numbers found in a sentence.

text = "The year 2024 will be great, but 2023 was amazing!"
print(sum(list(map(lambda x: int(x), filter(lambda x: x.isdigit(), text.split())))))

# Filter words with more than 5 characters and sort them by length.

words = ["elephant", "cat", "giraffe", "dog", "crocodile", "fox"]
result = sorted(list(filter(lambda x: len(x) > 5, words)), key = len)
print(result)

# Square the even numbers from a list, filter out non-numeric values, and join the results as a string.

data = ["5", "10", "hello", "20", "odd", "30"]
result = list(map(lambda x: str(x), map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, map(lambda x: int(x), filter(lambda x: x.isdigit(), data))))))
final_result = ",".join(result)
print(final_result)


list_comprehension = '''List comprehension is a concise way to create lists using a single line of code. 
It replaces loops and map() functions, making code more readable and efficient.'''
# Syntax is: [expression for item in iterable if condition]
# exercises of it

# Create a list of numbers from 1 to 10.

List_1 = [x for x in range(1, 11)]
print(List_1)

# Create a list of squares of numbers from 1 to 10.

List_2 = [x ** 2 for x in range(1, 11)]

# Create a list of even numbers from 1 to 20.

List_3 = [x for x in range(1, 21) if x % 2 == 0]

#
List_4 = ['Areg', "Mels", 'Jorik']
List_5 = [x.upper() for x in List_4] #Convert all names in the list to uppercase.
List_6 = [x for x in List_4 if x[0] == 'A'] #Create a list of names that start with 'A'

# Find the length of each word in the list.

Words = ['Tom', 'Bob', 'Kevin']
Words_len = [len(x) for x in Words]
print(Words_len)

# Find all numbers from 1 to 50 that are divisible by both 3 and 5.

Numbers = [x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0]
print(Numbers)

# "Reverse each word in the list.

Words_reversed = [x[::-1] for x in Words]
print(Words_reversed)

# Replace all vowels in the words with '*'.

Vowels = 'aeiou'
Words = ['Tom', 'Bob', 'Kevin']
vowels_replace = [''.join(['*' if char in Vowels else char for char in word]) for word in Words]
print(vowels_replace)

# Create a list of numbers from 1 to 6, each multiplied by 2.

list_2 = [x + x for x in range(1, 7)]
print(list_2)

# Extract the main diagonal elements from a square matrix.

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

diagonal = [matrix[i][i] for i in range(len(matrix))]
print(diagonal)

# Remove duplicates from a list while preserving the order.

nums = [4, 2, 2, 8, 3, 3, 1]
nums_1 = []
nums_2 = [nums_1.append(x) for x in nums if x not in nums_1]
print(nums_1)

# Find all palindrome words in a given list.

words = ["racecar", "hello", "level", "python", "radar"]
palindrome = [x for x in words if x == x[::-1]]
print(palindrome)

# Sort words in the list based on their length.

words = ["apple", "banana", "kiwi", "grape"]
words_by_len = sorted([x for x in words], key = len)
print(words_by_len)

# Extract every second character from each word in a given list.

words = ["hello", "world", "python"]
words_by_even = [x[::2] for x in words]
print(words_by_even)

# Reverse each row in a given matrix.

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
new = []
for i in matrix:
    i = i[::-1]
    new.append(i)
for i in new:
    print(i)
#or#
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
new = [row[::-1] for row in matrix]
for row in new:
    print(row)

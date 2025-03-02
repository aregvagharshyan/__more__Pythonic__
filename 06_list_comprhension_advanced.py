# Here some advanced exercises.
# Flatten a nested list into a single list.

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
new_list = [j for i in nested_list for j in i]
print(new_list)

# Create a matrix with rows containing values from different ranges.

matrix = [[x for x in range(1, 6)],
          [y for y in range(6, 11)],
          [k for k in range(11, 16)],
          [i for i in range(16, 21)],
          [g for g in range(21, 26)]]
print(matrix)

# Create a matrix with each row containing 5 consecutive numbers.

matrix_1 = [[x for x in range(i, i + 5)] for i in range(1, 26, 5)]
for i in matrix_1:
    print(i)

# Generate a list of prime numbers between 2 and 100.

prime_numbers = [i for i in range(2, 101) if all(i % j != 0 for j in range(2, i))]
print(prime_numbers)

# Filter words from a list that have more than 5 characters.

words = ["Python", "AI", "DeepLearning", "Code", "Machine"]
words_sorted = [x for x in words if len(x) > 5]
print(words_sorted)

# Find palindrome words in a given list.

words = ["racecar", "level", "python", "radar", "hello"]
words_palindrome = [x for x in words if x == x[::-1]]
print(words_palindrome)

# Remove duplicates from a list.

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
new_nums = [x for x in set(nums)]
print(new_nums)
#or#
new_nums = []
[new_nums.append(x) for x in nums if x not in new_nums]

# Convert strings that represent digits into integers."

data = ["10", "5", "hello", "20", "Python", "30"]
integers = [int(x) for x in data if x.isdigit()]
print(integers)

# Convert a list of Celsius temperatures to Fahrenheit.

celsius = [0, 10, 20, 30, 40]
farenhayt = [x * 9 / 5 + 32 for x in celsius]
print(farenhayt)

# Calculate the sum of each row in a matrix.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_row_sum = [sum(x) for x in matrix]
print(matrix_row_sum)

# Extract unique vowels from a list of words.

words = ["hello", "world", "python", "programming"]
vowels = 'auioeAUIOE'
words_vowels = list(set([x for i in words for x in i if x in vowels]))
print(words_vowels)

# Generate a multiplication table from 1 to 10.

table = [[(i) * (j) for j in range(1,11)] for i in range(1,11)]
for row in table:
    print(row)

# Find the common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
new_list = [x for x in list1 if x in list2]
print(new_list)

# Transpose a matrix using loops.

matrix = [[1,2,3],
          [1,2,3],
          [1,2,3]]
matrix_transposed = []
for i in range(len(matrix[1])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    matrix_transposed.append(transposed_row)
for i in matrix_transposed:
    print(i)

# Transpose a matrix using list comprehension.

matrix_transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
for i in matrix_transposed:
    print(i)


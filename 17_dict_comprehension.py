dict_comprehension = '''Dictionary comprehension in Python is a concise way to create dictionaries from iterable objects,
like lists or other dictionaries. The syntax is similar to list comprehension but for dictionaries. Here’s the general syntax:'''
#*****#
# Syntax is: {key_expression: value_expression for item in iterable if condition}
hint = 'Here some exercises with dict comprehension too.'

# Finds The highest.

company = {
    "Engineering": {"Alice": 90000, "Bob": 85000},
    "HR": {"Charlie": 70000, "David": 75000}
}
company.get('Engineering').get('Bob', 'No Error')
company['Engineering'].setdefault('Eve', 95000)
company['HR'].pop('Charlie')
highest = max(x for k in company.values() for x in k.values())
print(highest)

# Word Count Function.

def word_count(text):
    words = text.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return ', '.join(f"{word}: {count}" for word, count in word_dict.items())
text = "apple banana apple orange banana apple"
print(word_count(text))

# Most Frequent Value.

data = {"a": 3, "b": 5, "c": 3, "d": 7, "e": 5, "f": 5}
frequently = []
for value in data.values():
    frequently.append(value)
print(f"The most frequently occurring value is {max(frequently)}, and it's appears {frequently.count(max(frequently))} time.")

# Combining Inventory from Stores.

store1 = {"apples": 5, "bananas": 8, "oranges": 3}
store2 = {"apples": 4, "bananas": 2, "grapes": 6}
store3 = {"oranges": 5, "grapes": 2, "pears": 7}
store_all = {}
for key, value in store1.items():
    if key in store2:
        value += store2[key]
    if key in store3:
        value += store3[key]
    store_all[key] = value
for key, value in store1.items():
    if key not in store_all:
        store_all[key] = value
for key, value in store2.items():
    if key not in store_all:
        store_all[key] = value
for key, value in store3.items():
    if key not in store_all:
        store_all[key] = value
print(store_all)

# Filtering Temperatures.

temperatures = {"Monday": 22, "Tuesday": 19, "Wednesday": 25, "Thursday": 18, "Friday": 20}
result = {x: k for x, k in temperatures.items() if k >= 20}
print(result)

# Sorting Words by Frequency.

words = {"hello": 5, "hi": 2, "Python": 10, "a": 1}
result = dict(sorted(words.items(), key = lambda x: x[1]))
print(result)

# Converting List of Tuples to Dictionary.

data = [("name", "Alice"), ("age", 25), ("city", "New York")]
print(dict(data))

# Finding Maximum Value in Scores.

scores = {"Alice": 85, "Bob": 92, "Charlie": 88}
max_score = max(scores, key=scores.get)
print(f"The highest score is by {max_score} with a score of {scores[max_score]}")

# Summing Values in a Nested Dictionary and then finds the key with the highest sum.

data = {
    "A": [1, 5, 3],
    "B": [7, 2],
    "C": [4, 6, 8],
    "D": [9]
}
summary = {x:sum(k) for x, k in data.items()}
highest = max(summary.values())
for i, j in summary.items():
    if j == highest:
        print(i,j)
sort = dict(sorted(summary.items(), key = lambda x: x[1], reverse = True))


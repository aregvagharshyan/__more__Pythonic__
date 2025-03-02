# Filter Even Numbers.

numbers = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
even = {x: k for x, k in numbers.items() if k % 2 == 0}
print(even)

# Reverse the Dictionary.

favorites = {
    "Alice": ["red", "blue"],
    "Bob": ["green", "blue"],
    "Charlie": ["red", "yellow"]
}
reverse_of_favorites = {}
for key, value in favorites.items():
    for values in value:
        reverse_of_favorites.setdefault(values, []).append(key)
print(reverse_of_favorites)

# Count Character Frequency in a Word.

word = "mississippi"
count_of_char = {x: word.count(x) for x in word}
print(count_of_char)

# Enumerate Tasks.

tasks = ["Buy groceries", "Clean room", "Finish project", "Exercise"]
enumerate_of_tasks = dict(enumerate(tasks, start = 1))
print(enumerate_of_tasks)

# Merge Products and Categories.

prices = {"laptop": 1200, "phone": 800, "tablet": 300}
categories = {"laptop": "electronics", "phone": "electronics", "watch": "accessory"}
merged = {
    item: {
        "price": prices.get(item, 0),
        "category": categories.get(item, "unknown")
    }
    for item in prices.keys() | categories.keys()
}
print(merged)

# Group Cities by Country.

data = [
    ("Armenia", "Yerevan", 1075000),
    ("France", "Paris", 2148000),
    ("Germany", "Berlin", 3769000),
    ("France", "Lyon", 513000),
    ("Germany", "Hamburg", 1841000)
]
data_dict = {}
for country, city, population in data:
    data_dict.setdefault(country, {}).update({city: population})
print(data_dict)

# Word Length Dictionary.

sentence = "Python dictionaries are very powerful"
list_of_sentence = sentence.split()
dict_of_it = {x: len(x) for x in list_of_sentence}
print(dict_of_it)

# Track Index of Names in a List.

names = "Alice,Bob,Charlie,Alice,Bob,Alice"
list_names = names.split(',')
dict_names = {x: [i for i, name in enumerate(list_names) if name == x] for x in list_names}
print(dict_names)

# Find Maximum Votes.

votes = {
    "Alice": 5,
    "Bob": 8,
    "Charlie": 8,
    "David": 3
}
result = []
max_value = max(votes.values())
for key, value in votes.items():
    if value == max_value:
        result.append(key)
print(result)

# Filter Cities Starting with 'N'.

cities = {
    "New York": 8419600,
    "Los Angeles": 3980400,
    "New Delhi": 3187000,
    "New Orleans": 390144,
    "Boston": 675647
}
dict_cities = {x: k for x, k in cities.items() if x[0] == 'N'}
print(dict_cities)

# Word Length Dictionary.

words = ["Python", "is", "awesome", "to", "learn"]
dict_of_words = {x:len(x) for x in words}
print(dict_of_words)

# Swap Keys and Values in a Dictionary.

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
swapped_grades = {x: k for k, x in grades.items()}
print(swapped_grades)

# Filter Words by Length.

words = ["table", "cup", "laptop", "pen", "notebook", "bottle"]
word_by_length = {x: len(x) for x in words if len(x) >= 5}
print(word_by_length)

# Merge Two Sales Dictionaries.

sales_january = {"apple": 50, "banana": 30, "orange": 20}
sales_february = {"apple": 40, "banana": 25, "grapes": 15}
sales_all = {}
for key_1, value_1 in sales_january.items():
    for key_2, value_2 in sales_february.items():
        if key_1 in sales_february:
            sales_january[key_1] = sales_february.get(key_1) + value_1
sales_all.update(sales_january)
for key, value in sales_february.items():
    if key not in sales_all:
        sales_all.update({key: value})
print(sales_all)

# Track Word Indices in a Sentence.

sentence = "hello world hello again world hello"
sentence_split = sentence.split()
dict_of_sentence = {x: [i for i, name in enumerate(sentence_split) if name == x] for x in sentence_split}
print(dict_of_sentence)

# Track Character Frequency in a Word.

word = "banana"
dict_1 = {}
for i in word:
    dict_1[i] = dict_1.get(i, 0) + 1
max_freque = max(dict_1.values())
dict_2 = {x: k for x, k in dict_1.items() if k == max_freque}
print(dict_2)

# Filter Scores Above 80.

scores = {"Alice": 95, "Bob": 78, "Charlie": 82, "David": 60, "Emma": 88}
new_scores = {x: k for x, k in scores.items() if k >= 80}
print(new_scores)

# Group Words by Last Letter.

words = ["cat", "hat", "dog", "log", "bat", "fog"]
dict_of_words = {}
for i in words:
    last_letter = i[-1]
    dict_of_words.setdefault(last_letter, []).append(i)
print(dict_of_words)

# Find Students with Highest Score.

students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 92, "Eve": 88}
max_score = max(students.values())
highest = [x for x, k in students.items() if k == max_score]
print(highest)
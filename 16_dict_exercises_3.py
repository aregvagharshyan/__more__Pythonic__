# Retrieve a Nested Dictionary Value.

data = {
    "user": {
        "profile": {
            "name": "Alice",
            "age": 30
        },
        "settings": {
            "theme": "dark"
        }
    }
}
def get_nested_value(d, lst):
    for key in lst:
        if key in d:
            d = d[key]
        else:
            return None
    return d
print(get_nested_value(data, ["user", "profile", "name"]))
print(get_nested_value(data, ["user", "settings", "theme"]))
print(get_nested_value(data, ["user", "address"]))

# Filter Products by Price.

products = {
    "laptop": 1200,
    "phone": 800,
    "tablet": 300,
    "monitor": 450,
    "keyboard": 150
}
new_products = {x: k for x, k in products.items() if k >= 500}
print(new_products)

# Swap Keys and Values in a Dictionary.

countries = {
    "AM": "Armenia",
    "US": "United States",
    "FR": "France",
    "DE": "Germany"
}
swapped_countries = {x: k for k, x in countries.items()}
print(swapped_countries)

# Merge Two Dictionaries (Adding Values).

sales_january = {"apple": 50, "banana": 30, "orange": 20}
sales_february = {"banana": 25, "orange": 35, "grape": 40}
for key, value in sales_january.items():
    if key in sales_february:
       sales_january[key] = sales_february.get(key) + value
for key, value in sales_february.items():
    if key not in sales_january:
        sales_january[key] = value
print(sales_january)
#or#
sales_january = {"apple": 50, "banana": 30, "orange": 20}
sales_february = {"banana": 25, "orange": 35, "grape": 40}
merged_sales = {x: sales_january.get(x, 0) + sales_february.get(x, 0) for x in set(sales_january) | set(sales_february)}
print(merged_sales)

# Group Scores by Name.

scores = [
    ("Alice", 85),
    ("Bob", 90),
    ("Alice", 92),
    ("Bob", 88),
    ("Charlie", 75),
    ("Alice", 78),
]
scores_dict = {}
for name, score in scores:
    scores_dict.setdefault(name, []).append(score)
print(scores_dict)

# Create a Dictionary from Two Lists.

keys = ["name", "age", "city"]
values = ["Alice", 25, "Yerevan"]
dict_keys_values = dict(zip(keys, values))
print(dict_keys_values)

# Filter Dictionary Based on Key Length.

dictionary = {
    "apple": "a fruit",
    "banana": "another fruit",
    "hi": "a greeting",
    "dictionary": "a collection of words",
    "pen": "a writing instrument"
}
new_dict = {x: k for x, k in dictionary.items() if len(x) >= 3}
print(new_dict)

# Count Word Frequency in a Sentence.

sentence = "this is a test this is only a test"
list_of_sentence = sentence.split()
dict_of_sentence = {x: list_of_sentence.count(x) for x in list_of_sentence}
print(dict_of_sentence)

# Merge Dictionaries with Default Values.

defaults = {"theme": "light", "font": "Arial", "show_notifications": True}
user_settings = {"theme": "dark", "font": "Times New Roman"}
merged = defaults | user_settings
for key, value in merged.items():
    if key not in user_settings:
        merged[key] = value
print(merged)

# Generate a Dictionary of Squared Numbers.

result = {x: x ** 2 for x in range(1, 6)}
print(result)

# Group Words by First Letter.

words = ["apple", "banana", "avocado", "blueberry", "cherry", "carrot"]
dict_2 = {}
for i in words:
    dict_2.setdefault(i[0],[]).append(i)
print(dict_2)

# Create a Dictionary from Two Lists (Students and Grades).

students = ["Alice", "Bob", "Charlie"]
grades = [85, 90, 78]
dict_of_students = dict(zip(students, grades))
print(dict_of_students)


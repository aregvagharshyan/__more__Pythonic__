# Find Anagrams.

words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"]
anagram_dict = {x:[i for i in words if sorted(i) == sorted(x)] for x in words}
print(anagram_dict)

# Flatten a Nested Dictionary.

nested = {
    "user": {
        "name": "Alice",
        "info": {
            "age": 25,
            "city": "Paris"
        }
    }
}
new_dict = {}
for key_1, value_1 in nested.items():
    for i, j in value_1.items():
        if isinstance(j, str):
            new_dict.setdefault(key_1 + '.' + i, j)
        if isinstance(j, dict):
            for x, y in j.items():
                new_dict.setdefault(key_1 + '.' + i +'.' + x, y)
print(new_dict)

# Find Top 3 Highest Sales Items.

sales = {"apple": 50, "banana": 30, "orange": 20, "grapes": 40, "mango": 60}
sales_values = list(sales.values())
sales_max_1 = max(sales_values)
sales_values.remove(sales_max_1)
sales_max_2 = max(sales_values)
sales_values.remove(sales_max_2)
sales_max_3 = max(sales_values)
max_sales = [sales_max_1, sales_max_2, sales_max_3]
new_dict = {x: k for x, k in sales.items() if k in max_sales}
sorted_list = list(sorted(zip(new_dict.keys(), new_dict.values()), key = lambda x: x[1], reverse = True))
print(sorted_list)

# Sort Student Scores in Each Subject.

students = {
    "Alice": {"math": 90, "english": 85},
    "Bob": {"math": 80, "english": 95},
    "Charlie": {"math": 85, "english": 78}
}
sorted_students = { name: list(sorted(zip(scores.keys(), scores.values()), key = lambda x: x[1])) for name, scores in students.items()}
sorted_dict = {x:dict(k) for x, k in sorted_students.items()}
print(sorted_dict)

# Count Element Frequencies in a Matrix.

matrix = [
    [1, 2, 3, 2],
    [4, 1, 2, 3],
    [1, 3, 4, 4]
]
list_matrix = [i for x in matrix for i in x]
dict_matrix_items = {}
for i in list_matrix:
    if i in dict_matrix_items:
        dict_matrix_items[i] += 1
    else:
        dict_matrix_items[i] = 1
print(dict_matrix_items)

# Track Indices of Elements in a List.

elements = ["apple", "banana", "apple", "cherry", "banana", "banana"]
dict_of_elements = {x:[i for i, val in enumerate(elements) if val == x] for x in elements}
print(dict_of_elements)

# Merge Multiple Dictionaries with Summed Values.

dicts = [
    {"apple": 10, "banana": 5},
    {"banana": 10, "orange": 8},
    {"apple": 5, "orange": 12, "grapes": 7}
]
new_dict = {}
for key_1, value_1 in dicts[0].items():
    for key_2, value_2 in dicts[1].items():
        for key_3, value_3 in dicts[2].items():
            if key_1 == key_2:
                new_dict[key_1] = value_1 + value_2
            elif key_1 == key_3:
                new_dict[key_1] = value_1 + value_3
            elif key_2 == key_3:
                new_dict[key_2] = value_2 + value_3
for key, value in dicts[0].items():
    if key not in new_dict:
        new_dict[key] = value
for key, value in dicts[1].items():
    if key not in new_dict:
        new_dict[key] = value
for key, value in dicts[2].items():
    if key not in new_dict:
        new_dict[key] = value
print(new_dict)

# Find the Deepest Key in a Nested Dictionary.

nested_dict = {
    "a": {"b": {"c": {"d": 5}}},
    "x": {"y": 10}
}
key = []
length = 0
max_depth = 0
deepest_key = ""
for k_1, v_1 in nested_dict.items():
    if isinstance(v_1, dict):
        key.append(k_1)
        length += 1
        key.append(length)
        for k_2, v_2 in v_1.items():
            if isinstance(v_2, dict):
                key.append(k_2)
                length += 1
                key.append(length)
                for k_3, v_3 in v_2.items():
                    if isinstance(v_3, dict):
                        key.append(k_3)
                        length += 1
                        key.append(length)
                        for k_4, v_4 in v_3.items():
                            if isinstance(v_4, dict):
                                key.append(k_4)
                                length += 1
                                key.append(length)
                                if length > max_depth:
                                    max_depth = length
                                    deepest_key = k_4
                            else:
                                if length > max_depth:
                                    max_depth = length
                                    deepest_key = k_4
                    else:
                        if length > max_depth:
                            max_depth = length
                            deepest_key = k_3
            else:
                if length > max_depth:
                    max_depth = length
                    deepest_key = k_2
    else:
        if length > max_depth:
            max_depth = length
            deepest_key = k_1
print(f"Deepest key: {deepest_key}, Depth: {max_depth}")

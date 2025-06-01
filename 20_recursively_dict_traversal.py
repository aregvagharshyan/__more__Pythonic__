algorithm_tree = '''recursive_function(d):
│
├── Check base case:
│   ├── If d is not a dict → return base value
│   └── If d is empty → return base value (optional)
│
├── Initialize result (e.g. sum = 0, list = [], count = 0, etc.)
│
├── For each key, value in d.items():
│   │
│   ├── If value is a dict:
│   │   └── Call recursive_function(value), combine result
│   │
│   └── Else:
│       └── Apply your condition (e.g. if int, str, etc.)
│           └── Update result (sum, count, append, etc.)
│
└── Return result'''
# Common Return Patterns:
# •sum, count, list, max, min, dict (modified), or paths


data = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
list_1 = []
def find_key(d, target_key):
    for x, y in d.items():
        if x == target_key:
            list_1.append(y)
        elif isinstance(y, dict):
            find_key(y, target_key)
find_key(data, 'e')
print(list_1)

#

data = {'a': {'x': 1}, 'b': {'x': 2, 'c': {'x': 3}}}
list_2 = []
def find_all_keys(d, target):
    for x, y in d.items():
        if x == target:
            list_2.append(y)
        elif isinstance(y, dict):
            find_all_keys(y, target)
find_all_keys(data, 'x')
print(list_2)

#

data = {'a': {'b': {'c': 5}}}
list_3 = []
def find_key_path(d, target):
    for x, y in d.items():
        if x == target:
            list_3.append(x)
        elif isinstance(y, dict):
            find_key_path(y, target)
            list_3.append(x)
find_key_path(data, 'c')
print(list_3)

#

data = {'a': {'x': 'hi'}, 'b': {'x': 10, 'y': {'x': 3.5}}}
list_4 = []
def find_key_type(d, target, annotation):
    for x, y in d.items():
        if x == target and isinstance(y, annotation):
            list_4.append(y)
        elif isinstance(y, dict):
            find_key_type(y, target, annotation)
find_key_type(data, 'x', int)
print(list_4)

#

data = {'a': {'target': 1}, 'b': {'target': 2}}
def replace_key(d, target, new_value):
    for x, y in d.items():
        if x == target:
            d[x] = new_value
        elif isinstance(y, dict):
            replace_key(y, target, new_value)
replace_key(data, 'target', 99)
print(data)

#

data = {
    "x": {
        "y": {
            "z": 1
        },
        "w": 2
    },
    "a": 3
}
list_1 = []
def all_keys(d):
    for x, y in d.items():
        if not isinstance(y, dict):
            list_1.append(x)
        elif isinstance(y, dict):
            all_keys(y)
            list_1.append(x)
all_keys(data)
print(list_1)

#

data = {
    "level1": {
        "level2": {
            "level3": {
                "level4": 123
            }
        }
    }
}
def maximum_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    return 1 + max(maximum_depth(v) for v in d.values())
print(maximum_depth(data))

#

data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "f": {}
        }
    },
    "g": {}
}
list_1 = []
def count_leaves(d):
    for x, y in d.items():
        if isinstance(y, int):
            list_1.append(x)
        elif isinstance(y, dict):
            count_leaves(y)
count_leaves(data)
count_tuple = (len(list_1), tuple(list_1))
print(count_tuple)

#

data = {
    "a": 10,
    "b": {
        "c": 20,
        "d": {
            "e": 30
        }
    }
}
list_2 = []
def collect_leaf_values(d):
    for x, y in d.items():
        if isinstance(y, int):
            list_2.append(y)
        elif isinstance(y, dict):
            collect_leaf_values(y)

collect_leaf_values(data)
print(list_2)

#

data = {
    "x": {
        "y": {
            "z": 1
        },
        "w": 2
    },
    "a": 3
}
def count_all_keys(d):
    count = 0
    for x, y in d.items():
        count += 1
        if isinstance(y, dict):
            count += count_all_keys(y)
    return count
print(count_all_keys(data))

#

data = {
    "x": 2,
    "y": {
        "z": 3,
        "w": {
            "v": 4
        }
    }
}

def square_leaves(d):
    for x, y in d.items():
        if isinstance(y, int):
            d[x] = (y ** 2)
        elif isinstance(y, dict):
            square_leaves(y)
    return d
print(square_leaves(data))

#

data = {
    "a": 1,
    "b": {
        "c": "hello",
        "d": {
            "e": 3,
            "f": 5.5
        }
    }
}
def count_int_values(d):
    count = 0
    for x, y in d.items():
        if isinstance(y, int):
            count += 1
        elif isinstance(y, dict):
            count += count_int_values(y)
    return count
print(count_int_values(data))

#

data = {
    "x": {
        "y": 10,
        "z": {
            "w": 5
        }
    },
    "a": 3,
    "b": "string"
}
def sum_int_leaves(d):
    count = 0
    for x, y in d.items():
        if isinstance(y, int):
            count += y
        elif isinstance(y, dict):
            count += sum_int_leaves(y)
    return count
print(sum_int_leaves(data))

#

data = {
    "a": {},
    "b": {
        "c": {},
        "d": {
            "e": 1,
            "f": {}
        }
    }
}
def count_empty_dicts(d):
    count = 0
    for x, y in d.items():
        if y == {}:
            count += 1
        elif x == {}:
            count += 1
        elif isinstance(y, dict):
            count += count_empty_dicts(y)
    return count
print(count_empty_dicts(data))

#

data = {
    "a": 1,
    "b": {
        "c": 2
    }
}
def prefix_keys(d, prefix):
    new_dict = {}
    for x, y in d.items():
        new_key = prefix + x
        if isinstance(y, dict):
            new_dict[new_key] = prefix_keys(y, prefix)
        else:
            new_dict[new_key] = y
    return new_dict
print(prefix_keys(data, 'p_'))

#

data = {
    "user": {
        "name": "Bob",
        "info": {
            "email": "bob@example.com",
            "age": 40
        }
    },
    "status": "active"
}
def count_string_leaves(d):
    count = 0
    for x, y in d.items():
        if isinstance(y, str):
            count += 1
        elif isinstance(y, dict):
            count += count_string_leaves(y)
    return count
print(count_string_leaves(data))

#

data = {
    "a": {
        "b": {
            "c": 1
        },
        "d": 2
    }
}
def keys_at_depth(d, target_depth, current_depth=0):
    result = []
    for key, value in d.items():
        if current_depth == target_depth:
            result.append(key)
        elif isinstance(value, dict):
            result.extend(keys_at_depth(value, target_depth, current_depth + 1))
    return result
print(keys_at_depth(data, 0))

#

data = {
    "a": 2,
    "b": {
        "c": 3,
        "d": {
            "e": 4.0
        }
    }
}
def product_numeric_leaves(d):
    mult = 1
    for x, y in d.items():
        if isinstance(y, (int, float)):
            mult *= y
        elif isinstance(y, dict):
            mult *= product_numeric_leaves(y)
    return mult
print(product_numeric_leaves(data))

#

data = {
    "a": 10,
    "b": {
        "c": 20,
        "d": {
            "e": 30
        }
    },
    "f": {
        "g": "done"
    }
}
def not_dict_keys(d):
    result = []
    for x, y in d.items():
        if not isinstance(y, dict):
            result.append(x)
        elif isinstance(y, dict):
            result.extend(not_dict_keys(y))
    return result
print(not_dict_keys(data))

#

data = {
    "a": 4,
    "b": {
        "x": 7,
        "y": {
            "z": 10
        }
    }
}

def even_leaf_values(d):
    count = 0
    for x, y in d.items():
        if isinstance(y, int) and y % 2 ==0:
            count += 1
        elif isinstance(y, dict):
            count += even_leaf_values(y)
    return count
print(even_leaf_values(data))

#

data = {
    "name": "Armen",
    "info": {
        "bio": {
            "text": "Developer",
            "desc": "Loves Python"
        }
    }
}
def long_leaf_value(d):
    result = []
    for x, y in d.items():
        if isinstance(y, str):
            result.append(y)
        elif isinstance(y, dict):
            result.extend(long_leaf_value(y))
    return result
all_strings = long_leaf_value(data)
max_string = max(all_strings, key = len)
print(max_string)

#

data = {
    "x": 1,
    "y": {"z": 2, "w": {"u": 3}},
    "k": 4
}
def all_int(d):
    result = []
    for x, y in d.items():
        if isinstance(y, int):
            result.append(y)
        elif isinstance(y, dict):
            result.extend(all_int(y))
    reversed_result = list(reversed(result))
    return reversed_result
print(all_int(data))

#

data = {
    "id": 1,
    "user": {
        "name": "Anna",
        "info": {
            "email": "a@example.com",
            "age": 22
        }
    }
}
def all_leaf_values(d):
    result = []
    for x, y in d.items():
        if not  isinstance(y, dict):
            result.append(y)
        elif isinstance(y, dict):
            result.extend(all_leaf_values(y))
    return result
print(all_leaf_values(data))

#

mixed = {"x": "hello", "y": [1, {"z": "world"}], "a": {"b": ["!"]}}
def extract_strings(d):
    result = []
    for x, y in d.items():
        if isinstance(y, str):
            result.append(y)
        elif isinstance(y, dict):
            result.extend(extract_strings(y))
        elif isinstance(y, list):
            for i in y:
                if isinstance(i, str):
                    result.append(i)
                elif isinstance(i, dict):
                    result.extend(extract_strings(i))
    return result
print(extract_strings(mixed))
algorithm_tree = '''while_loop_function(d):
│
├── Initialize result (sum, count, list, etc.)
├── Initialize stack/queue → [d]
│
├── While stack is not empty:
│   ├── Pop element (e.g. current_dict)
│   │
│   ├── If current is a dict:
│   │   └── For each value in current.values():
│   │       └── Push value to stack
│   │
│   └── Else:
│       └── Apply your condition (if int, str, etc.)
│           └── Update result
│
└── Return result'''
# Stack Tip: Use [d] as the initial stack. You can also push (key, value) or
# (path, value) if you need paths.


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

sum_of_val = 0
stack = [data]
while stack:
    current = stack.pop()
    for x, y in current.items():
        if isinstance(y, int):
            sum_of_val += y
        elif isinstance(y, dict):
            stack.append(y)
print(sum_of_val)

#

data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    }
}
def count_all_keys(d):
    count = 0
    stack = [d]
    while stack:
        current = stack.pop()
        for x, y in current.items():
            count += 1
            if isinstance(y, dict):
                stack.append(y)
    return count
print(count_all_keys(data))

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
    stack = [d]
    while stack:
        current = stack.pop()
        for x, y in current.items():
            if y == {}:
                count += 1
            elif isinstance(y, dict):
                stack.append(y)
    return count
print(count_empty_dicts(data))

#

data = {
    "a": 7,
    "b": {
        "c": 15,
        "d": {
            "e": 3
        }
    },
    "f": "text"
}
def max_int_leaf(d):
    result = []
    stack = [d]
    while stack:
        current = stack.pop()
        for x, y in current.items():
            if isinstance(y, int):
                result.append(y)
            elif isinstance(y, dict):
                stack.append(y)
    max_int = max(result)
    return max_int
print(max_int_leaf(data))

#

data = {
    "x": 1,
    "y": {"z": 2, "w": {"u": 3}},
    "k": "hello"
}
def sum_all_ints(d):
    sum_of_ints = 0
    stack = [d]
    while stack:
        current = stack.pop()
        for x, y in current.items():
            if isinstance(y, int):
                sum_of_ints += y
            elif isinstance(y, dict):
                stack.append(y)
    return sum_of_ints
print(sum_all_ints(data))

#

data = {
    "a": "one",
    "b": {"c": "two", "d": {"e": "three"}},
    "f": 10
}
def count_str(d):
    count = 0
    stack = [d]
    while stack:
        current = stack.pop()
        for x, y in current.items():
            if isinstance(y, str):
                count += 1
            elif isinstance(y, dict):
                stack.append(y)
    return count
print(count_str(data))

#

data = {
    "a": 42,
    "b": {"x": 3, "y": {"z": -8}},
    "c": "test"
}
def min_int(d):
    result = []
    stack = [d]
    while stack:
        current = stack.pop()
        for x, y in current.items():
            if isinstance(y, int):
                result.append(y)
            elif isinstance(y, dict):
                stack.append(y)
    min_of_result = min(result)
    return min_of_result
print(min_int(data))

#

data = {
    "ok": True,
    "config": {
        "debug": False,
        "flags": {
            "verbose": True
        }
    }
}
def boolean_values(d):
    result = []
    stack = [d]
    while stack:
        current = stack.pop()
        for x, y in current.items():
            if isinstance(y, bool):
                result.append(y)
            elif isinstance(y, dict):
                stack.append(y)
    return result
print(boolean_values(data))

#

data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "f": "text"
        }
    },
    "g": None
}
def count_all_leaf_values(d):
    count = 0
    stack = [d]
    while stack:
        current = stack.pop()
        for x, y in current.items():
            if not isinstance(y, dict):
                count += 1
            elif isinstance(y, dict):
                stack.append(y)
    return count
print(count_all_leaf_values(data))

#

nested = {
    'a': {'target': 1, 'b': {'target': 2}},
    'c': {'d': {'e': {'target': 3}}}
}

def leaf_value_by_key(d):
    result = []
    stack = [nested]
    while stack:
        current = stack.pop()
        for key, value in current.items():
            if key == 'target':
                result.append(value)
            elif isinstance(value, dict):
                stack.append(value)
    return result
print(leaf_value_by_key(nested))
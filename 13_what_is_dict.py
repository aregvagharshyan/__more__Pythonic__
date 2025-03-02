# Using methods.

students_grade = {"Alice": 90, "Bob": 85, "Charlie": 88}
print(students_grade.get('Alice'))
print(students_grade.keys())
print(students_grade.values())
print(students_grade.items())
students_grade["David"] = 92
#or#
students_grade.update({'David': 92})
students_grade.pop('Bob')
#or#
#del students_grade['Bob']
students_grade.clear()
#
inventory = {"apple": 10, "banana": 5}
inventory.setdefault('orange', 7)
inventory.setdefault('apple', 20)
#
product_prices = {"laptop": 1200, "phone": 800}
product_prices_copy = product_prices.copy()
product_prices['laptop'] = 1500
print(product_prices_copy)
#
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
dict_3 = {**dict_a, **dict_b}
dict_c = dict_a | dict_b
#
book_collection = {"Harry Potter": 5, "The Hobbit": 3}
book_collection.update({'1984': 4})
book_collection.popitem()
book_collection.setdefault('Melsi Gaxtniqy', 1)
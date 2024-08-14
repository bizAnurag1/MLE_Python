"""
Using lambda function for sorting
"""
strings_list = ["apple", "banana", "cherry", "date"]

sorted_strings = sorted(strings_list, key=lambda s: len(s))

print("Sorted by length:", sorted_strings)

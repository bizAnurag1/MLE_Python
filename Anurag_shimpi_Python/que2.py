"""
This script defines a function to add only string elements to a list.
If an element is not a string, it displays an appropriate message.
"""
add_if_string = lambda lst, ele: lst.append(ele) if isinstance(ele, str) else print("Enter string")

my_list = []

elements = ["hello", 123, "world"]
for element in elements:
    add_if_string(my_list, element)

print("Final list:", my_list)

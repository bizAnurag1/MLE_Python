"""
This script defines a function to add only string elements to a list.
If an element is not a string, it displays an appropriate message.
"""

def string_list(element):
    """
    given function is for checking the type of input element,
    if it is string then add it to list
    """
    if isinstance(element, str):
        my_list.append(element)
        print(f"{element} added to the list.")
    else:
        print(f"{element} is not a string.")

my_list = []
string_list("hello")
string_list(12)
string_list("abcd")
string_list("Anurag")

print("Final list:", my_list)

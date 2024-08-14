"""
Ask user to enter any 3 input e.g name, marks , mobile_num
   if name is with other special characters then it should not not ask for next makrs input
   note: 
	1) Create separate functions for validation of every variable 
	2) Every single block should have proper exception
    3) Every function must have the docstring
	4) Once the validation is done dictionary has to be created and store the dictionary to one 
       txt file
"""
import re
def validate_name(name):
    """
    Validates that the name contains only alphabets and spaces.
    """
    if not re.match("^[A-Za-z]+$", name):
        raise ValueError("Name contains special characters.")
    return name

def validate_marks(marks):
    """
    Validates that the marks are numeric and between 0 and 100.
    """
    try:
        marks = float(marks)
    except ValueError:
        raise ValueError("Marks must be numeric.")
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    return marks

def validate_mobile_num(mobile_num):
    """
    Validates that the mobile number is exactly 10 digits long.
    """
    if not (mobile_num.isdigit() and len(mobile_num) == 10):
        raise ValueError("Mobile number must be exactly 10 digits.")
    return mobile_num

def main():
    """
    Main function: to validate all inputs and saves it into text file as dictionary.
    """
    user_data = {}
    try:
        name = input("Enter your name: ")
        user_data["name"] = validate_name(name)
        marks = input("Enter your marks: ")
        user_data["marks"] = validate_marks(marks)
        mobile_num = input("Enter your mobile number: ")
        user_data["mobile_num"] = validate_mobile_num(mobile_num)
        # Save the dictionary to a text file
        with open("user_data.txt", "a") as file:
            file.write(str(user_data))
        print("User data has been saved successfully.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

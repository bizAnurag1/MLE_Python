"""
In the hotel user is entering the details of menu, quantity and printing the bill. 
number of menu may varies with customer's order 
generate a file having grocery bill as per the given format
"""
import datetime

def get_items():
    """
    Gets menu items, their quantities, and prices from the user.
    Returns: list of tuples: Each tuple contains a menu item, quantity, and price.
    """
    menu_items = []
    while True:
        try:
            item = input("Enter menu item or 'exit' to finish: ")
            if item.lower() == 'exit':
                break
            quantity = int(input("Enter quantity for {}: ".format(item)))
            price = float(input("Enter price for {}: ".format(item)))
            menu_items.append((item, quantity, price))
        except ValueError:
            print("Invalid input. Please enter the details correctly.")
    return menu_items

def calculate_total(menu_items):
    """
    Calculates the total cost and GST for the menu items.
    """
    total = sum(quantity * price for _, quantity, price in menu_items)
    gst = total * 0.10  # 10% GST
    total_with_gst = total + gst
    return total, gst, total_with_gst

def generate_bill(menu_items, total, gst, total_with_gst):
    """
    Generates the bill in the specified format and saves it to a file.
    """
    receipt_number = datetime.datetime.now().strftime("%H%M%S")
    current_date = datetime.datetime.today().strftime("%Y-%m-%d")
    hotel_name = "Welcome Hotel Name"
    bill_lines = [
        "-" * 33,
        "|   {:<27}|".format(hotel_name),
        "|{:<16} recpt: {}|".format(current_date, receipt_number),
        "-" * 33,
        "|SR.   Menu     qnt   price|",
    ]
    for idx, (menu_item, quantity, price) in enumerate(menu_items, start=1):
        bill_lines.append("|{:<5}{:<10}{:<5}{:<6}|".format(idx,menu_item,quantity,quantity*price))
    bill_lines.extend([
        "-" * 33,
        "|total               {:<6.2f}|".format(total),
        "|including GST 10% = {:<6.2f}|".format(gst),
        "|total with GST      {:<6.2f}|".format(total_with_gst),
        "-" * 33,
    ])
    bill_content = "\n".join(bill_lines)
    with open("grocery_bill.txt", "w") as file:
        file.write(bill_content)
    print("Bill has been generated and saved to grocery_bill.txt")
    print(bill_content)

def main():
    """main function"""
    menu_items = get_items()
    total, gst, total_with_gst = calculate_total(menu_items)
    generate_bill(menu_items, total, gst, total_with_gst)

if __name__ == "__main__":
    main()


menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99},
    6: {"name": 'ice cream',
        "price": 7.99}
}

def calculate_subtotal(order):
    print('Calculating bill subtotal...')
    subtotal = 0

    for item in order:
        subtotal += item['price']
    return round(subtotal,2)


def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    percent = 0.1 if subtotal>10 else 0.15
    tax = round(subtotal*percent,2)

    format_percent = '10%' if percent==0.1 else '15%'

    return tax, format_percent


def summarize_order(order,subtotal,tax):
    total = round(subtotal+tax,2)
    items = [item["name"] for item in order]

    return items, total


# This function is provided for you, and will print out the items in an order
def print_order(order):
    len_order = str(len(order))
    print('You have ordered {} items'.format(len_order))
    items = [item["name"] for item in order]
    print(items)


# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()


# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    flag = True
    while flag:
        item = input('Select menu item number {} (from 1 to {}): '.format(str(count),len(menu)))
        if item.isnumeric() and int(item) in range(1,len(menu)+1):
            count += 1
            order.append(menu[int(item)])

            if count > 3:
                more_item = input('Você quer adicionar mais items? "S" ou "N"')
                more_item.lower()
                if more_item == 'n':
                    flag = False
                else:
                    continue
        else:
            print('Tip a number in the correct range')     
    return order

'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()
    print_order(order)
    print()

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: {}".format(str(subtotal)))
    print()

    tax, percent = calculate_tax(subtotal)
    print("Tax for the order is: {}".format(str(tax)))
    print()

    items, subtotal = summarize_order(order,subtotal,tax)
    print(f'Items: {items} - Total Price: {subtotal} - Percent Add: {percent}')

if __name__ == "__main__":
    main()

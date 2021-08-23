# Shopping Receipt Calculator
import sys

# TODO this is an example app using all the principles from the tutorial,
#  plus a couple of new ones. Please run this and study it for preparation for the project


def calculate_total(items):
    total = 0.0
    for item in items:
        total += item['price']
    return total


def print_receipt(items, total):
    print("#####Receipt#####")
    print("-----Items------")
    for item in items:
        print(item['name'], '$', item['price'])
    print("-----Total------")
    print('$', total)
    print("----------------")


def ask_user_for_item():
    item_name = input("Please enter item name: ")
    price_valid = False
    while not price_valid:
        try:
            item_price = float(input("Please enter item price, e.g. 1.01: "))
            # If it gets to here the number was valid
            price_valid = True
        except:
            print('\nThe price you entered is invalid, please enter numbers and decimal point only!', file=sys.stderr)

    item_object = {
        'name': item_name,
        'price': item_price
    }
    return item_object


def main():
    should_add_items = True
    items = []

    while should_add_items is True:
        answer_string = input("Do you want to add an item to Shopping Receipt? (yes or no): ")
        if answer_string == 'yes':
            item = ask_user_for_item()
            items.append(item)
        elif answer_string == "no":
            should_add_items = False

    total = calculate_total(items)
    print_receipt(items, total)


if __name__ == "__main__":
    # TODO The program starts here
    # You can press the play button to start
    main()

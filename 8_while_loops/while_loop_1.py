# while loops


bananas_eaten = 1
monkey_is_hungry = True

while monkey_is_hungry:
    print(bananas_eaten)
    bananas_eaten = bananas_eaten + 1

    if bananas_eaten > 10:
        monkey_is_hungry = False

# TODO before running this, try to guess what number of bananas will print out last

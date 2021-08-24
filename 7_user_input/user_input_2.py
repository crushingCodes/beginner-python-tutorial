# 7. User Input

import random


value = int(input("Enter a number between 1 Numbers Start here and 10: "))

random_number = random.randint(1, 10)

if value == random_number:
    print("YOU WIN")
else:
    print("YOU LOSE! Number was", random_number)


# TODO 1. using a for loop, make this question appear 5 times in a row

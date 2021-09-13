# 7. User Input

import random


value = int(input("Enter a number between 1 Numbers Start here and 10: "))

random_answer = random.randint(1, 10)

if value == random_answer:
    print("YOU WIN")
else:
    print("YOU LOSE! Number was", random_answer)


# TODO 1. using a for loop, make this question appear 5 times in a row

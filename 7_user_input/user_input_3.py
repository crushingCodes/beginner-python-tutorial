# 7. User Input
import random

def check_guess(guess, answer):
    if guess == answer:
        print("YOU WIN")
    else:
        print("YOU LOSE! The answer was", answer)

def create_answer():
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    print(f'{number_1} + {number_2}')
    answer = number_1 + number_2
    return answer

answer = create_answer()
# !!!! Do not change above code !!!!

# TODO 1. change guess to accept the guess from the user
guess = None


# !!!! Do not change below code !!!!
check_guess(int(guess), answer)

# TODO 2. create function to create full quiz, answer guess and check_guess

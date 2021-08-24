# 7. User Input
import random

def check_guess(guess, answer):
    if guess == answer:
        print("YOU WIN")
    else:
        print("YOU LOSE! The answer was", answer)

def create_quiz():
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    print(f'{number_1} + {number_2}')
    answer = number_1 + number_2
    return answer

answer = create_quiz()
# !!!! Do not change above code !!!!

# TODO 1. change guess to accept the guess from the user
guess = None


# !!!! Do not change below code !!!!
check_guess(int(guess), answer)

# 10. Rock paper scissors

# TODO check instructions in project_instructions.py and complete the code here
import random


def ask_player_choice():
    # TODO complete this to ask user input
    # (1)Rock (2)Paper (3)Scissors:
    # return answer_number
    pass


def get_computer_choice():
    random_int = random.randint(1, 3)
    return random_int


def check_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("DRAW!")
    elif player_choice == 1 and computer_choice == 2:
        print("YOU LOSE!")
    elif player_choice == 1 and computer_choice == 3:
        print("YOU WIN!")
    elif player_choice == 2 and computer_choice == 1:
        print("YOU WIN!")
    elif player_choice == 2 and computer_choice == 3:
        print("YOU LOSE!")
    elif player_choice == 3 and computer_choice == 1:
        print("YOU LOSE!")
    elif player_choice == 3 and computer_choice == 2:
        print("YOU WIN!")


def change_number_to_word(number_value):
    if number_value == 1:
        return "Rock"
    elif number_value == 2:
        return "Paper"
    elif number_value == 3:
        return "Scissors"


def main():
    game_finished = False

    while game_finished is False:
        player_choice = ask_player_choice()
        print("Player choice:", change_number_to_word(player_choice))

        answer = input("Play again? (y, n): ")
        if answer == "y":
            game_finished = False
        elif answer == "n":
            game_finished = True


if __name__ == "__main__":
    # The program starts here
    # You can press the play button to start
    main()

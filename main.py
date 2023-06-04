# dice bone dwarf poker

import random
import os
from PIL import Image
import sys
import cv2
import time

os.system("cls")

img = cv2.imread("dice_poker.jpg", cv2.IMREAD_ANYCOLOR)
while True:
    cv2.imshow("dice_poker.jpg", img)
    cv2.waitKey(0)
    break
print(" dice bone dwarf poker game ")
print()

player = input(" player name, type here o  -->  ")


def main_game():
    final_human_points = 0
    final_computer_points = 0
    remis_resolut = 0
    while True:
        number_of_turns = int(input("enter the number of turns, enter an even number"))
        if number_of_turns % 2 == 0:
            print("positive_answer")
            for j in range(number_of_turns):
                round_result = throw_the_dice()
                if round_result == ("human"):
                    final_human_points += 1
                elif round_result == ("computer"):
                    final_computer_points += 1
                else:
                    remis_resolut += 1

            break

        else:
            print("negative_answer")
    print
    print("final score")
    print
    print(
        f"percentage of your wining final points: { player} ",
        (final_human_points * 100) / number_of_turns,
    )
    print(
        "percentage of final computer points",
        (final_computer_points * 100) / number_of_turns,
    )
    print(
        "percentage remis tours        ",
        (remis_resolut * 100) / number_of_turns,
    )


def throw_the_dice():
    mynumbers = []
    lista = [1, 2, 3, 4, 5, 6]

    while len(mynumbers) < 5:
        newnumber = random.choice(lista)

        mynumbers.append(newnumber)
    mynumbers.sort()
    print(" the results of a man throwing the dice:", mynumbers)
    print("")
    global computer_numbers
    computer_numbers = []

    while len(computer_numbers) < 5:
        newnumber = random.choice(lista)

        computer_numbers.append(newnumber)
    computer_numbers.sort()
    print(" the results of a computer throwing the dice:", computer_numbers)
    roll_the_dice_decision(mynumbers, computer_numbers)
    computer_numbers = computer_run(computer_numbers)

    return calculation_who_win(mynumbers, computer_numbers, player)


def roll_the_dice_decision(mynumbers, computer_numbers):
    used_numbers = []
    do_re_roll = input("set 1 if you want re roll the dices, set 2 if not --> ")
    if do_re_roll == "1":
        how_many_dices = int(input("how many dices do ypu want to roll 1 - 5 -->"))
        if how_many_dices < 1 or how_many_dices > 5:
            print("wrong number you dzban")
            return False
        else:
            for i in range(how_many_dices):
                which_dice_to_roll = int(input("which dice you want to roll "))
                used_nb = which_dice_to_roll
                #                if which_dice_to_roll in used_numbers:
                if used_nb in used_numbers:
                    continue
                mynumbers[which_dice_to_roll - 1] = random.randint(1, 6)
                used_numbers.append(which_dice_to_roll)
                print(used_numbers)
                mynumbers.sort()
                print(" the results of a man re roll the dice:", (mynumbers))


def computer_run(computer_numbers):
    a, b, c, d, e = computer_numbers
    if a == b == c == d == e:
        pass
    elif a == b == c == d != e:
        e = random.randint(1, 6)
    elif b == c == d == e != a:
        a = random.randint(1, 6)
    elif a == b == c and d == e:
        pass
    elif a == b and c == d == e:
        pass
    elif a == 2 and b == 3 and c == 4 and d == 5:
        e = random.randint(1, 6)
    elif b == 2 and c == 3 and d == 4 and e == 6:
        a = random.randint(1, 6)
    elif a == b == c != d:
        d = random.randint(1, 6)
        e = random.randint(1, 6)
    elif c == d == e != a:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
    elif b == c == d:
        a = random.randint(1, 6)
        e = random.randint(1, 6)
    elif b == c and d == e:
        a = random.randint(1, 6)
    elif a == b and d == e:
        c = random.randint(1, 6)
    elif a == b and c == d:
        e = random.randint(1, 6)
    elif a == b:
        c = random.randint(1, 6)
        d = random.randint(1, 6)
        e = random.randint(1, 6)
    elif b == c:
        a = random.randint(1, 6)
        d = random.randint(1, 6)
        e = random.randint(1, 6)
    elif c == d:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        e = random.randint(1, 6)
    elif d == e:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)

    computer_numbers = [a, b, c, d, e]
    computer_numbers.sort()
    print(" the results of a re roll computer throwing the dice:", computer_numbers)
    return computer_numbers


#    return computer_numbers


def calculate_score(list_of_numbers):
    score = 0

    a, b, c, d, e = list_of_numbers

    if a == b == c == d == e:
        score += 8
    elif a == b == c == d or b == c == d == e:
        score += 7
    elif a == b == c and d == e or a == b and c == d == e:
        score += 6
    elif a == 2 and b == 3 and c == 4 and d == 5 and e == 6:
        score += 5
    elif a == 1 and b == 2 and c == 3 and d == 4 and e == 5:
        score = +4
    elif a == b == c:
        score += 3
    elif c == d == e:
        score += 3
    elif b == c == d:
        score += 3
    elif b == c and d == e:
        score += 2
    elif a == b and d == e:
        score += 2
    elif a == b and c == d:
        score += 2
    elif a == b:
        score += 1
    elif b == c:
        score += 1
    elif c == d:
        score += 1
    elif d == e:
        score += 1
    return score


def calculation_who_win(mynumbers, computer_numbers, player):
    human_score = calculate_score(mynumbers)

    computer_score = calculate_score(computer_numbers)
    print(human_score)
    print(computer_score)

    if human_score > computer_score:
        print(f"You Win: { player} ")
        return "human"
    elif human_score < computer_score:
        print(" computer win")
        return "computer"
    else:
        print("remis")
        return "remis"


main_game()

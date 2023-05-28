# dice bone dwarf poker

import random
import os

print(" dice bone dwarf poker game ")
print()


def throw_the_dice():
    player = input(" player name, type here o  -->  ")
    # human_player = Player(player)
    # computer_player = Player("computer")
    mynumbers = []
    lista = [1, 2, 3, 4, 5, 6]

    while len(mynumbers) < 5:
        newnumber = random.choice(lista)

        mynumbers.append(newnumber)
    print(" the results of a man throwing the dice:", sorted(mynumbers))
    print("")
    computer_numbers = []
    # lista = [1, 2, 3, 4, 5, 6]

    while len(computer_numbers) < 5:
        newnumber = random.choice(lista)

        computer_numbers.append(newnumber)
    print(" the results of a computer throwing the dice:", sorted(computer_numbers))
    roll_the_dice_decision(mynumbers, computer_numbers)


print("what dice roll do you want to roll again")


def roll_the_dice_decision(mynumbers, computer_numbers):
    do_re_roll = input("set 1 if you want re roll the dices, set 2 if not")
    if do_re_roll == "1":
        how_many_dices = int(input("how many dices do ypu want to roll 1 - 5"))
        for i in range(how_many_dices):
            which_dice_to_roll = int(input("which dice you want to roll "))
            mynumbers[which_dice_to_roll - 1] = random.randint(1, 6)
        print(" the results of a man re roll the dice:", (mynumbers))

    calculation_who_win(mynumbers, computer_numbers)


def calculation_who_win(mynumbers, computer_numbers):
    human_score = 1

    core_point = 1
    a = mynumbers[core_point - 1]
    b = mynumbers[core_point]
    c = mynumbers[core_point + 1]
    d = mynumbers[core_point + 2]
    e = mynumbers[core_point + 3]
    computer_score = 1
    core_point_c = 1
    ax = computer_numbers[core_point_c - 1]
    bx = computer_numbers[core_point_c]
    cx = computer_numbers[core_point_c + 1]
    dx = computer_numbers[core_point_c + 2]
    ex = computer_numbers[core_point_c + 3]
    for i in range(1):
        if a == b and b != c:
            human_score += 1
        if b == c and c != d:
            human_score += 1
        if c == d and d != e:
            human_score += 1
        if d == e:
            human_score += 1
        if a == b and c == d:
            human_score += 2
        if b == c and d == e:
            human_score += 2
        if a == b and d == e:
            human_score += 2
        if a == b == c:
            human_score += 3
        if c == d == e:
            human_score += 3
        if b == c == d:
            human_score += 3
        if a == 1 and b == 2 and c == 3 and d == 4 and c == 5 and e == 6:
            human_score = +4
        if a == 2 and b == 3 and c == 4 and d == 5 and c == 6:
            human_score += 5
        if a == b == c and d == e or a == b and c == d == e:
            human_score += 6
        if a == b == c == d or b == c == d == e:
            human_score += 7
        if a == b == c == d == e:
            human_score += 8
    for i in range(1):
        if ax == bx and bx != cx:
            computer_score += 1
        if bx == cx and cx != dx:
            computer_score += 1
        if cx == dx and dx != ex:
            computer_score += 1
        if dx == ex:
            computer_score += 1
        if ax == bx and cx == dx:
            computer_score += 2
        if bx == cx and dx == ex:
            computer_score += 2
        if ax == bx and dx == ex:
            computer_score += 2
        if ax == bx == cx:
            computer_score += 3
        if bx == cx == dx:
            computer_score += 3
        if cx == dx == ex:
            computer_score += 3
        if ax == 1 and bx == 2 and cx == 3 and dx == 4 and cx == 5 and ex == 6:
            computer_score = +4
        if ax == 2 and bx == 3 and cx == 4 and dx == 5 and cx == 6:
            computer_score += 5
        if ax == bx == cx and dx == ex or ax == bx and cx == dx == ex:
            computer_score += 6
        if ax == bx == cx == dx or bx == cx == dx == ex:
            computer_score += 7
        if ax == bx == cx == dx == ex:
            computer_score += 8
        print(human_score)
        print(computer_score)
    if human_score > computer_score:
        print(" human win")
    elif human_score < computer_score:
        print(" computer win")
    else:
        print("remis")


# def who_win_the_game(human_score, computer_score):
# if human_score > computer_score:
#     print(" human win")
# elif human_score < computer_score:
#     print(" computer win")
# else:
#     print("remis")


throw_the_dice()

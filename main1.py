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
    computer_score = 1
    core_point = 1
    a = mynumbers[core_point - 1]
    b = mynumbers[core_point]
    c = mynumbers[core_point + 1]
    d = mynumbers[core_point + 2]
    e = mynumbers[core_point + 3]

    ac = computer_numbers[core_point - 1]
    bc = computer_numbers[core_point]
    cc = computer_numbers[core_point + 1]
    dc = computer_numbers[core_point + 2]
    ec = computer_numbers[core_point + 3]
    for i in range(1):
        if a == b and b != c and b != d and b != e or b == c or c == d or d == e:
            human_score += 1
        if a == b and c == d and b != e or b == c and d == e and a != b:
            human_score += 2
        if a == b == c and c != d and c != e or c == d == e and e != a and e != b:
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

        if ac == bc:
            computer_score += 1
        if ac == bc and cc == dc:
            computer_score += 2
        if ac == bc == cc or cc == dc == e:
            computer_score += 3
        if ac == 1 and bc == 2 and cc == 3 and dc == 4 and cc == 5:
            computer_score += 4
        if ac == 2 and bc == 3 and cc == 4 and dc == 5 and cc == 6:
            computer_score += 5
        if ac == bc == cc and dc == ec or ac == bc and cc == dc == ec:
            computer_score += 6
        if ac == bc == cc == dc or bc == cc == dc == ec:
            computer_score += 7
        if ac == bc == cc == dc == ec:
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

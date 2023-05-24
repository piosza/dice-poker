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
    clista = [1, 2, 3, 4, 5, 6]

    while len(computer_numbers) < 5:
        newnumber = random.choice(lista)

        computer_numbers.append(newnumber)
    print(" the results of a computer throwing the dice:", sorted(computer_numbers))
    roll_the_dice_decision(mynumbers, computer_numbers)


print("what dice roll do you want to roll again")


def roll_the_dice_decision(mynumbers, computer_numbers):
    do_re_roll = input("set 1 if you want re roll the dices, set 2 if not")
    if do_re_roll == "1":
        how_many_dices = int(input("how many dices do ypu want to roll 1 - 4"))
        for i in range(how_many_dices):
            which_dice_to_roll = int(input("which dice you want to roll "))
            mynumbers[which_dice_to_roll - 1] = random.randint(1, 6)
        print(" the results of a man re roll the dice:", (mynumbers))

    who_win(mynumbers, computer_numbers)


def who_win(mynumbers, computer_numbers):
    human_points = sum(mynumbers)
    computer_points = sum(computer_numbers)
    if human_points > computer_points:
        print(" human win")
    elif human_points < computer_points:
        print(" computer win")
    else:
        print("remis")


throw_the_dice()

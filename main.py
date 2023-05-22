# dice bone dwarf poker

import random
import os

print(" dice bone dwarf poker game ")
print()





def throw_the_dice():
    player = input(" player name, type here o  -->  ")
    human_player = Player(player)
    computer_player = Player("computer")
    myNumbers = []
    Lista = [1, 2, 3, 4, 5, 6]

    while len(myNumbers) < 5:
        newNumber = random.choice(Lista)

        myNumbers.append(newNumber)
    print(" the results of a man throwing the dice:", sorted(myNumbers))
    print("")
    computer_Numbers = []
    Lista = [1, 2, 3, 4, 5, 6]

    while len(computer_Numbers) < 5:
        newNumber = random.choice(Lista)

        computer_Numbers.append(newNumber)
    print(" the results of a computer throwing the dice:", sorted(computer_Numbers))


print ("what dice roll do you want to roll again")

def roll_the_dice_decision():
    x = int(input("set 1 if you want re roll the dices"))
    y = int(input("set 2 if not "))
    if x == 1:
        q = int(input("how many dices do ypu want to roll 1 - 4"))
        if q == 1:
            second_throw1()
        if q == 2:
            second_throw2()
        if q == 3:
            second_throw3()
        if q == 4:
            second_throw4()
    if y == 2:
        who_win()

def second_throw1(myNymbers):
    print("chose field ")
    z1 = int(input("set field for roll"))
    Lista = [1, 2, 3, 4, 5, 6]

    while len(myNumbers) == z1:
        newNumber = random.choice(Lista)

        myNumbers.append(newNumber)

def second_throw2():
    print("chose fields ")

def second_throw3():
    print("chose fields ")

def second_throw4():
    print("chose fields ")

def who_win():


throw_the_dice()

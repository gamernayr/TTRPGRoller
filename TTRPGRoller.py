# Title: Table Top RPG Roller
# Date: November 21, 2021
# Author: Ryan Epp
# Description: Rolls virtual dice by text input and gives results

import random

def roll(sides, num):
    sum = 0
    for i in range(num):
        sum = sum + random.randint(1,sides)
    return sum

class Roll():
    def __init__(self, sides, num, isPos, isDice):
        self.sides = sides
        self.num = num
        self.isPos = isPos
        self.isDice = isDice
    def eval(self):
        final = 0
        if self.isDice:
            final = roll(self.sides, self.num)
        else:
            final = self.sides
        if not self.isPos:
            final = final * -1
        return final

def input_to_rolls(string):
    roll_list = []

    builder = ""
    isPos = True
    for c in string:
        # Once we find 
        if c == '+' or c == '-':
            if builder != "":
                roll_list.append(build_roll(builder, isPos))
            builder = ""
            if c == '+':
                isPos = True
            else:
                isPos = False
        else:
            builder = builder + c
    roll_list.append(build_roll(builder, isPos))

    return roll_list

def build_roll(builder, isPos):
    split = builder.split('d')
    if len(split) == 2:
        numDice = int(split[0])
        numSides = int(split[1])
        return Roll(numSides, numDice, isPos, isDice=True)
    else:
        val = int(split[0])
        return Roll(val, -1, isPos, False)
    

repeat = True

print("TTRPG-Roller\n  Roll dice using XdXX (ex. 1d4+2d6-2)")

while repeat: # keep rolling
    print("--------")

    # split dice types
    rolls_to_process = input_to_rolls(input().replace(" ", ""))

    totalResult = 0

    for unit in rolls_to_process:
        totalResult = totalResult + unit.eval()

    print("[" + str(totalResult) + "]")
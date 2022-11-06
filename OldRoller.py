# Title: Table Top RPG Roller
# Date: November 21, 2021
# Author: Ryan Epp
# Description: Rolls virtual dice by text input and gives results

import random, re

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
    
def input_is_valid(n: str):
    if len(n) == 0:
        print("String input was empty")
        return False
    #elif re.search("^d", n) is None and re.search("d", n) is not None:
    #    print("Used dice quantifier without numbers")
    #    return False

    return True

def format_input(n: str):
    return re.sub("^0-9d", "", n)

repeat = True

print("TTRPG-Roller\n  Roll dice using XdXX (ex. 1d4+2d6-2)")

while repeat: # keep rolling
    print("--------")

    # split dice types
    input_from_user = format_input(input())
    if input_is_valid(input_from_user):
        rolls_to_process = input_to_rolls(input_from_user)

        totalResult = 0

        for unit in rolls_to_process:
            totalResult = totalResult + unit.eval()

        print("[" + str(totalResult) + "]")
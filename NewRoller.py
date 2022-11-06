# Title: Table Top RPG Roller
# Date: November 21, 2021
# Author: Ryan Epp
# Description: Rolls virtual dice by text input and gives results

import random, re

# Roll a specified number of dice with the same side and return the roll history
#  Returns a list of the rolled values
def roll(sides, num):
    roll_hist = []
    for _ in range(num):
        result = random.randint(1, sides)
        roll_hist.append(result)
    return roll_hist

# A roll can either be a set of the same dice, or a flat value
class Roll():
    def __init__(self, sides, num, isPos, isDice):
        self.sides = sides
        self.num = num
        self.isPos = isPos
        self.isDice = isDice
        self.roll_hist = []
    def eval(self):
        final = 0
        if self.isDice:
            self.roll_hist = roll(self.sides, self.num) 
            final = sum(self.roll_hist)
        else:
            final = self.sides
        #---
        # Can be a negative modifier
        if not self.isPos:
            final = final * -1
        #---
        if self.isDice:
            return "[" + str(self.num) + "d" + str(self.sides) + ": " + "".join(str(roll) + (" " if index < len(self.roll_hist)-1 else "") for index, roll in enumerate(self.roll_hist)) + "]", final
        else:
            return "[Mod: " + str(self.sides) + "]", self.sides

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
    # If the input was empty
    if len(n) == 0:
        print("String input was empty")
        return False
    # If the input didn't have a dice quantifier
    elif re.search("d", n) is None:
        print("No dice identifier [d]!")
        return False
    return True

def format_input(n: str):
    return re.sub("^0-9d", "", n)

print("Roll some dice!")

while True: # keep rolling
    print("--------")

    # split dice types
    input_from_user = format_input(input())
    if input_is_valid(input_from_user):
        rolls_to_process = input_to_rolls(input_from_user)

        totalResult = 0
        rolls_made = []

        for unit in rolls_to_process:
            rolls_made.append(unit.eval())
        
        for roll_made in rolls_made:
            totalResult = totalResult + roll_made[1]
            print(roll_made[0])

        print("[Total: " + str(totalResult) + "]")
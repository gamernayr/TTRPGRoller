# Title: Table Top RPG Roller
# Date: August 18, 2020
# Author: Ryan Epp
# Description: Rolls virtual dice by text input and gives results

import Dice

repeat = True

print("TTRPG-Roller\n  Roll dice using XdXX (ex. 1d4+2d6)\n  Do not use spaces")

while repeat: # keep rolling
    print("--------")

    # split dice types
    dices = input().split("+")

    totalResult = 0

    # have different dice types in list ["1d4", "1d10"]
    for param in dices: # for every param
        additive = 0
        paramSplit = param.split("d") # split the numDice and the powerDice (ndp)
        if(len(paramSplit) == 2): # check for dice or modifier
            try:
                numDice = int(paramSplit[0]) # number of dice to roll
                powerDice = int(paramSplit[1]) # what kind of dice to roll (d4, d6, ect.)
                # roll the dice and add them to the total road
                additive = Dice.roll(powerDice, numDice)
            except ValueError:
                print("Not a number, try again.")
                continue
        else: # is a mod, add the value to the total
            additive = int(paramSplit[0])

        totalResult += additive 

    print("[" + str(totalResult) + "]")
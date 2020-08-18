# Title: Table Top RPG Roller
# Date: August 18, 2020
# Author: Ryan Epp
# Description: Rolls virtual dice by text input and gives results

import Dice

repeat = True

print("TTPRG-Roller\n  Roll dice using XdXX\n  Supports modifiers (+Y) after dice input\n  Do not use spaces")

while repeat: # keep rolling
    print("--Dice--")
    
    # split dice types
    dices = input().split("+")

    # 

    
    print("--Mods--")

    mods = input()
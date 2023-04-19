# Title: Scion Dice Roller
# Date: August 18, 2020
# Author: Ryan Epp
# Description: Rolls virtual dice and counts the number of successes (>=7 on a d10), 
#              and notifies of a botch (no successes and a NAT 1).

import random

repeat = True

print("Scion-Dice-Roller")

while repeat: # keep rolling
    print("-----")
    try: # try for numbered input
        rolls = int(input())
    except ValueError: # skip if not a number
        print("Not a number")
        continue

    # keep track of success rolls and botch check
    succ = 0
    botch = False

    # make rolls
    for x in range(0,rolls):
        # roll a dice
        rollNum = random.randint(1,10)

        if rollNum == 1: # check for botch
            botch = True
        elif rollNum >= 7: # add successes
            succ += 2 if rollNum == 10 else 1
    
    # botch check
    if botch and succ == 0:
        print("Botched")
    else: # print success rolls
        print("Successes:",succ)
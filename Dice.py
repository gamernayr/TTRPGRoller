# Author: Ryan Epp
# Description: Contains dice for use by main class

import random

def roll(sides, num):
    return int(random.randint(1,sides) * num)

# specific dice to roll
def d4(num):
    return random.randint(1,4)*num

def d6(num):
    return random.randint(1,6)*num

def d8(num):
    return random.randint(1,8)*num

def d10(num):
    return random.randint(1,10)*num

def d12(num):
    return random.randint(1,12)*num

def d20(num):
    return random.randint(1,20)*num
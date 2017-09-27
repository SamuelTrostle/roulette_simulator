import random
import time

#Lists
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0, 00]

singlezero = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
              ,2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,
              0]
doublezero = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
              ,2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,
              0, 00]

#Lists to Append
spin_red = []
spin_black = []
spin_green = []
wilcard = []
wildcard00 = []
random_bet = random.choice(singlezero)

#Wheel Spins
def spin_wheel():
    spin = random.randint(0, 36)
    if spin not in black:
        spin_red.append(spin)
        #spin == red
    elif spin not in red:
        spin_black.append(spin)
    elif spin in green:
        spin_green.append(spin)

def spin_wheel_random():
    spin = random.randint(0, 36)
    if spin not in black:
        spin_red.append(spin)
        spin == red
    if random_bet in spin:
        wilcard.append(spin)
    if spin not in red:
        spin_black.append(spin)
        spin == black
    if random_bet in spin:
            wilcard.append(spin)
    if spin in green:
        spin == green
        if random_bet in spin:
            wilcard.append(spin)

def spin_wheel_00():
    spin = random.choice(doublezero)
    if spin not in black:
        spin_red.append(spin)
        spin == red
    if random_bet in spin:
        wilcard.append(spin)
    if spin not in red:
        spin_black.append(spin)
        spin == black
    if random_bet in spin:
            wildcard00.append(spin)
    if spin in green:
        spin == green
        if random_bet in spin:
            wildcard00.append(spin)


#Simulaiton Functions
def guess_always_red5():
    print("spinning 5 times betting red")
    time.sleep(1)
    spin_count = 0
    while spin_count < 5:
        spin_count = spin_count + 1
        spin_wheel()
    print("You won %s times out of 5 spins betting Red!\n" % len(spin_red))
    time.sleep(2)

def guess_always_red100():
    print("spinning 100 times betting red")
    time.sleep(1)
    spin_count = 0
    del spin_red[:]
    while spin_count < 100:
        spin_count = spin_count + 1
        spin_wheel()
        # print(simulation1)
    print("You won %s times out of 100 spins betting Red!\n" % len(spin_red))
    time.sleep(2)

def guess_always_red1000():
    print("spinning 1000 times betting red")
    time.sleep(1)
    spin_count = 0
    del spin_red[:]
    while spin_count < 1000:
        spin_count = spin_count + 1
        spin_wheel()
        # print(simulation1)
    print("You won %s times out of 1000 spins betting Red!\n" % len(spin_red))
    time.sleep(2)

def guess_always_black5():
    print("spinning 5 times betting black")
    time.sleep(1)
    spin_count = 0
    del spin_black[:]
    while spin_count < 5:
        spin_count = spin_count + 1
        spin_wheel()
        # print(simulation1)
    print("You won %s times out of 5 spins betting Black!\n" % len(spin_black))
    time.sleep(2)

def guess_always_black100():
    print("spinning 100 times betting black")
    time.sleep(1)
    spin_count = 0
    del spin_black[:]
    while spin_count < 100:
        spin_count = spin_count + 1
        spin_wheel()
        # print(simulation1)
    print("You won %s times out of 100 spins betting Black!\n" % len(spin_black))
    time.sleep(2)

def guess_always_black1000():
    print("spinning 1000 times betting black")
    time.sleep(1)
    spin_count = 0
    del spin_black[:]
    while spin_count < 1000:
        spin_count = spin_count + 1
        spin_wheel()
        # print(simulation1)
    print("You won %s times out of 1000 spins betting Black!\n" % len(spin_black))
    time.sleep(2)

def guess_randomly5():
    print("Spinning 5 times with a random bet")
    spin_count = 0
    while spin_count < 5:
        spin_count = spin_count + 1
        spin_wheel_random()
    print("You won %s times out of 5 spins betting randomly!\n" % len(wilcard))
    time.sleep(2)

def guess_randomly100():
    print("Spinning 100 times with a random bet")
    spin_count = 0
    while spin_count < 100:
        spin_count = spin_count + 1
        spin_wheel_random()
    print("You won %s times out of 100 spins betting randomly!\n" % len(wilcard))
    time.sleep(2)

def guess_randomly1000():
    print("Spinning 1000 times with a random bet")
    spin_count = 0
    while spin_count < 1000:
        spin_count = spin_count + 1
        spin_wheel_random()
    print("You won %s times out of 1000 spins betting randomly!\n" % len(wilcard))
    time.sleep(2)

def double_randomly5():
    print("Spinning 5 times with a random bet")
    spin_count = 0
    while spin_count < 5:
        spin_count = spin_count + 1
        spin_wheel_00()
    print("You won %s times out of 5 spins betting randomly!\n" % len(wilcard))
    time.sleep(2)

def double_randomly100():
    print("Spinning 5 times with a random bet")
    spin_count = 0
    while spin_count < 1000:
        spin_count = spin_count + 1
        spin_wheel_00()
    print("You won %s times out of 5 spins betting randomly!\n" % len(wilcard))
    time.sleep(2)

def double_randomly1000():
    print("Spinning 5 times with a random bet")
    spin_count = 0
    while spin_count < 1000:
        spin_count = spin_count + 1
        spin_wheel_00()
    print("You won %s times out of 1000 spins betting randomly!\n" % len(wilcard))
    time.sleep(2)



#comment out quote lines to run
#'''''''''
print("Welcome to Roulette")
print('simulation 1:')
guess_always_red5()

print('simulation 2:')
guess_always_red100()

print('simulation 3:')
guess_always_red1000()

print('simulation 4:')
guess_always_black5()

print('simulation 5:')
guess_always_black100()

print('simulation 6:')
guess_always_black1000()
#'''''''''

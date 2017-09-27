import random
import time
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0, 00]

wildcard = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
              ,2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,
              0, 00]
singlezero = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
              ,2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,
              0]
doublezero = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
              ,2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,
              0, 00]

loss = []
def start_sim(sim_detail, bet, rounds, zeros):
    print(sim_detail)
    spin_count = 0
    win = []
    while spin_count < rounds:
        spin_count = spin_count + 1
        spin = random.randint(0,36)
        newbet = random.choice(bet)
        #print("Your bet: " + str(newbet))
        #print("Result: " + str(spin))
        if spin in red and newbet in red:
            # print("You win!")
            win.append(spin)

        elif spin in red and newbet not in red:
            # print("You Lose!")
            loss.append(spin)

        elif spin in black and newbet in black:
            # print("You win!")
            win.append(spin)

        elif spin in black and newbet not in black:
            # print("You lose!")
            loss.append(spin)

        elif spin in green and newbet in green:
            # print("You win!")
            win.append(spin)

        elif spin in green and newbet not in green:
            # print("You lose")
            loss.append(spin)
        else:
            print("Whoops, uh something went wrong!")
    print("You won {0} times in {1} rounds!\n".format(len(win), rounds))
    del win
    #print("Winning numbers: " + str(win))

print("\nWelcome to Roulette...")
time.sleep(1)
print("Starting to bet...")
time.sleep(2.0)
#Single zero 5
start_sim("Simulation 1:", red, 5, singlezero)
start_sim("Simulation 2:", black, 5, singlezero)
start_sim("Simulation 3:", wildcard, 5, singlezero)

#Double zero 5
start_sim("Simmulation 4:", red, 5, doublezero)
start_sim("Simmulation 5:", black, 5, doublezero)
start_sim("Simmulation 6:", wildcard, 5, doublezero)

#Single zero 100
start_sim("Simulation 7:", red, 100, singlezero)
start_sim("Simulation 8:", black, 100, singlezero)
start_sim("Simulation 9:", wildcard, 100, singlezero)

#Double zero 100
start_sim("Simmulation 10:", red, 100, doublezero)
start_sim("Simmulation 11:", black, 100, doublezero)
start_sim("Simmulation 12:", wildcard, 100, doublezero)

#Single zero 1000
start_sim("Simulation 13:", red, 1000, singlezero)
start_sim("Simulation 14", black, 1000, singlezero)
start_sim("Simmulation 15:", wildcard, 1000, singlezero)

#Double zero 1000
start_sim("Simmulation 16:", red, 1000, doublezero)
start_sim("Simmulation 17:", black, 1000, doublezero)
start_sim("Simulation 18:", wildcard, 1000, doublezero)

print("Thanks for playing!")
exit = input("Press any key to exit")




#Monty Hall Project
#Write a Monte Carlo script to estimate the probability of winning in the classic
#Monty Hall Problem with 3, 6, 9, 20 and 100 doors, while following either one of the following policies: 
    #(i) randomly switch to one of the remaining doors or
    #(ii) stick with your original selection
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def montyFall(nDoors, trials, stayOrChange, actualTrials):
    wins = 0
    for i in range(trials):
        #creating the "stage"
        doors = ["GOAT"] * nDoors
        carDoor = random.randint(0, nDoors - 1)
        doors[carDoor] = "CAR"

        #contestant makes their choice
        contestantChoice = random.randint(0, nDoors - 1)

        #host slips and opens a door that could be the car door
        for j in range(nDoors):
            if j != contestantChoice:
                deletedDoor = j
                doors[j] = "X"
                break
        
        #if the host accidentally opens the car door he gets fired 
        #and the game does not count (so dont count it as a trial)
        if deletedDoor == carDoor:
            continue

        actualTrials+=1
        #now contestant makes a choice. Stay with the originally picked door or choose a new one
        #choice = random.randint(0, 1)
        choice = stayOrChange;

        if choice == 0: #stay
            result = doors[contestantChoice];
        if choice == 1: #newdoor
            del doors[contestantChoice]
            doors.remove("X")
            result = doors[random.randint(0, len(doors) - 1)]

        wins += 1 if result == "CAR" else 0
    return (actualTrials, wins)

def monty(nDoors, trials, stayOrChange):
    wins=0
    for i in range(trials):
        #creating the "stage"
        doors = ["GOAT"] * nDoors
        carDoor = random.randint(0, nDoors - 1)
        doors[carDoor] = "CAR"

        #contestant makes their choice
        contestantChoice = random.randint(0, nDoors - 1)

        #host takes away one door (that the contestant didnt pick and does not have the car)
        for j in range(nDoors):
            if doors[j] == "GOAT" and j != contestantChoice:
                doors[j] = "X"
                break


        #now contestant makes a choice. Stay with the originally picked door or choose a new one
        #choice = random.randint(0, 1)
        choice = stayOrChange;

        if choice == 0: #stay
            result = doors[contestantChoice];
        if choice == 1: #newdoor
            del doors[contestantChoice]
            doors.remove("X")
            result = doors[random.randint(0, len(doors) - 1)]

        wins += 1 if result == "CAR" else 0
    return wins

def plotApproximationImprovement(nDoors, stayOrChange, actualProb):
    results = {}
    trials = 5

    while(trials < 500000):
        results[trials] = monty(nDoors, trials, stayOrChange) / trials
        trials*=5


    # calculate the slope and y-intercept of the line
    x = [0, len(results)]
    y = [actualProb, actualProb]
    m, b = np.polyfit(x, y, 1)

    i = 0
    for (key, value) in results.items():
        plt.scatter(i, value)
        
        # calculate the distance from the point to the line
        x_point = i
        y_point = value
        distance = abs(m * x_point - y_point + b) / np.sqrt(m**2 + 1)
        
        # draw a vertical line segment to represent the gap
        plt.plot([i, i], [value, actualProb], linestyle='--', color='gray', linewidth=1)
        
        i += 1

    # draw the line

    plt.axhline(y=actualProb, color='r', linestyle='-')
    plt.xlabel('5^n Trials')
    plt.ylabel('Win Rate')
    plt.title(str(nDoors) + ' Doors case ' + str(stayOrChange))
    plt.show()

def plotProbability(nDoors):
    xLabels = ["Stay Variant", "Switch Variant"]
    values = [monty(nDoors, 100000, 0)/100000,monty(nDoors, 100000, 1)/100000]

    plt.bar(xLabels[0], values[0], color="blue")
    plt.bar(xLabels[1], values[1], color="red")
    plt.xlabel('Cases')
    plt.ylabel('Win Rate')
    plt.title(str(nDoors) + " Doors")
    plt.show()

def plotProbabilityMontyFall(nDoors):
    xLabels = ["Stay Variant", "Switch Variant"]
    (trials1, wins1) = montyFall(nDoors, 100000, 0, 0)
    (trials2, wins2) = montyFall(nDoors, 100000, 1, 0)
    values = [wins1/trials1, wins2/trials2]

    plt.bar(xLabels[0], values[0], color="blue")
    plt.bar(xLabels[1], values[1], color="red")
    plt.xlabel('Cases')
    plt.ylabel('Win Rate')
    plt.title(str(nDoors) + " Doors")
    plt.show()


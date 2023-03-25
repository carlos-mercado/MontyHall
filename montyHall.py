#Monty Hall Project
#Write a Monte Carlo script to estimate the probability of winning in the classic
#Monty Hall Problem with 3, 6, 9, 20 and 100 doors, while following either one of the following policies: 
    #(i) randomly switch to one of the remaining doors or
    #(ii) stick with your original selection
import random

nDoors = 10


wins = 0
trials = 100000

for i in range(trials):
    #creating the "stage"
    doors = ["GOAT"] * nDoors
    carDoor = random.randint(0, nDoors - 1)
    doors[carDoor] = "CAR"

    #contestant makes their choice
    contestantDoorChoice = random.randint(0, nDoors - 1)

    #take away all doors except for the one that the contestant chose and
    #the one that holds that car.

    removeThisMuch = nDoors - 2
    removed = 0
    j = 0
    while j < nDoors and removed != removeThisMuch:
        if doors[j] == "CAR" or j == contestantDoorChoice:
            j += 1
            continue
        else:
            doors[j] = "X"
            removed += 1
            j += 1
            


    #now contestant makes a choice. Stay with the originally picked door or choose a new one
    stayOrChange = random.randint(0, 1)
    #stayOrChange = 0
    #stayOrChange = 1

    if stayOrChange == 0: #stay with original door
        result = doors[contestantDoorChoice];
    if stayOrChange == 1: #choose a new door
        del doors[contestantDoorChoice]
        while "X" in doors:
            doors.remove("X")
        result = doors[0]
    
    wins += 1 if result == "CAR" else 0


percentageWins = (wins / trials) * 100
print(str(percentageWins) + "% of trials are wins")
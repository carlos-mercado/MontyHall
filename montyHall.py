#Monty Hall Project
#Write a Monte Carlo script to estimate the probability of winning in the classic
#Monty Hall Problem with 3, 6, 9, 20 and 100 doors, while following either one of the following policies: 
    #(i) randomly switch to one of the remaining doors or
    #(ii) stick with your original selection
import random

class DoorsTrial:
    def __init__(self, nDoors):
        self.nDoors = nDoors
    def testFunction(self):
        wins = 0
        bananaWins = 0
        trials = 100000

        for i in range(trials):
            #creating the "stage"
            doors = ["GOAT"] * self.nDoors
            carDoor = random.randint(0, self.nDoors - 1)
            doors[carDoor] = "CAR"

            #contestant makes their choice
            contestantDoorChoice = random.randint(0, self.nDoors - 1)

            #remove/open enough doors such that we are left with two doors at the end
            #note that we cannot open the contestants door or the door that contains the car.
            removeThisMuch = self.nDoors - 2
            removed = 0
            j = 0
            while j < self.nDoors and removed != removeThisMuch:
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
            #seperate case for where host slips on banana after contestant has made choice and selects random other door
            bananaResult = doors[random.randint(0, self.nDoors - 1)]

            if stayOrChange == 0: #stay with original door
                result = doors[contestantDoorChoice];
            if stayOrChange == 1: #choose a new door
                del doors[contestantDoorChoice]
                while "X" in doors:
                    doors.remove("X")
                result = doors[0]
            
            wins += 1 if result == "CAR" else 0
            #counting wins for the banana case
            bananaWins += 1 if bananaResult == "CAR" else 0

        percentageWins = (wins / trials) * 100
        #calculating banana case wins
        bananaPercentageWins = (bananaWins / trials) * 100
        print(str(percentageWins) + "% of trials are wins")
        #printing banana case wins
        print("For " + str(self.nDoors) + " trials where host slips on banana " + str(bananaPercentageWins) + "% of trials are wins")
    
trialOf3 = DoorsTrial(3)
trialOf3.testFunction()
trialOf6 = DoorsTrial(6)
trialOf6.testFunction()
trialOf9 = DoorsTrial(9)
trialOf9.testFunction()
trialOf20 = DoorsTrial(20)
trialOf20.testFunction()
trialOf100 = DoorsTrial(100)
trialOf100.testFunction()
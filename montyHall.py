#Monty Hall Project
#Write a Monte Carlo script to estimate the probability of winning in the classic
#Monty Hall Problem with 3, 6, 9, 20 and 100 doors, while following either one of the following policies: 
    #(i) randomly switch to one of the remaining doors or
    #(ii) stick with your original selection
import random

class DoorsTrial:
    def __init__(self, nDoors):
        self.nDoors = nDoors

    def keepDoor(self):
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

            wins += 1 if doors[contestantDoorChoice] == "CAR" else 0

        percentageWins = (wins / trials) * 100
        #calculating banana case wins
        bananaPercentageWins = (bananaWins / trials) * 100
        print(str(percentageWins) + "% of trials are wins if you stay with " + str(self.nDoors) + " doors possible. ")
        #printing banana case wins
        print("For " + str(self.nDoors) + " trials where host slips on banana " + str(bananaPercentageWins) + "% of trials are wins.\n")

    def switchDoor(self):
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

            wins += 1 if doors[contestantDoorChoice] != "CAR" else 0

        percentageWins = (wins / trials) * 100
        #calculating banana case wins
        bananaPercentageWins = (bananaWins / trials) * 100
        print(str(percentageWins) + "% of trials are wins if you always switch. ")
        #printing banana case wins
        print("For " + str(self.nDoors) + " trials where host slips on banana " + str(bananaPercentageWins) + "% of trials are wins.\n")

    def randomPick(self):
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

            if random.randint(0, 1) == 0: #stay with original door
                wins += 1 if doors[contestantDoorChoice] == "CAR" else 0
            else: #choose a new door
                wins += 1 if doors[contestantDoorChoice] != "CAR" else 0

        percentageWins = (wins / trials) * 100
        #calculating banana case wins
        bananaPercentageWins = (bananaWins / trials) * 100
        print(str(percentageWins) + "% of trials are wins if randomly stay and or switch. ")
        #printing banana case wins
        print("For " + str(self.nDoors) + " trials where host slips on banana " + str(bananaPercentageWins) + "% of trials are wins.\n")



trialOf3 = DoorsTrial(3)
trialOf3.keepDoor()
trialOf3.switchDoor()
trialOf3.randomPick()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

trialOf6 = DoorsTrial(6)
trialOf6.keepDoor()
trialOf6.switchDoor()
trialOf6.randomPick()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

trialOf9 = DoorsTrial(9)
trialOf9.keepDoor()
trialOf9.switchDoor()
trialOf9.randomPick()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

trialOf20 = DoorsTrial(20)
trialOf20.keepDoor()
trialOf20.switchDoor()
trialOf20.randomPick()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

trialOf100 = DoorsTrial(100)
trialOf100.keepDoor()
trialOf100.switchDoor()
trialOf100.randomPick()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
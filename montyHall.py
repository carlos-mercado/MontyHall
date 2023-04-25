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
        bananaLose = 0
        trials = 100000

        for i in range(trials):
            #creating the "stage"
            doors = ["GOAT"] * self.nDoors
            carDoor = random.randint(0, self.nDoors - 1)
            doors[carDoor] = "CAR"
            
            #there is a 1 and 5th chance that the host slips and opens a door
            #if the door that opens in the car, the contestant loses atomaticly
            if random.randint(0, 4) == 2 and doors[random.randint(0, self.nDoors - 1)] == "CAR":
                bananaLose += 1
                continue

            #contestant makes their choice
            contestantDoorChoice = random.randint(0, self.nDoors - 1)
            
            wins += 1 if doors[contestantDoorChoice] == "CAR" else 0

        percentageWins = (wins / trials) * 100
        #calculating banana case wins
        bananaPercentageWins = (bananaLose / trials) * 100
        print("There is a " + str(percentageWins) + "% chance of winning if you stay with your first pick with " + str(self.nDoors) + " doors possible. ")

        #printing banana case wins
        print("For 100000 trials, there is a " + str(bananaPercentageWins) + "% chance of host slipping on a banana and instantly losing.\n")

    def switchDoor(self):
        wins = 0
        bananaLose = 0
        trials = 100000

        for i in range(trials):
            #creating the "stage"
            doors = ["GOAT"] * self.nDoors
            carDoor = random.randint(0, self.nDoors - 1)
            doors[carDoor] = "CAR"

            #there is a 1 and 5th chance that the host slips and opens a door
            #if the door that opens in the car, the contestant loses atomaticly
            if random.randint(0, 4) == 2 and doors[random.randint(0, self.nDoors - 1)] == "CAR":
                bananaLose += 1
                continue

            #contestant makes their choice
            contestantDoorChoice = random.randint(0, self.nDoors - 1)

            #open a door that isn't the car door or the one selected by contestant
            hostRemovedDoor = random.randint(0, self.nDoors - 1)
            while hostRemovedDoor != carDoor and hostRemovedDoor != contestantDoorChoice:
                hostRemovedDoor = random.randint(0, self.nDoors - 1)

            #contestant picks a new door that isn't the one that is open or the first picked
            newDoorChoice = random.randint(0, self.nDoors - 1)
            while newDoorChoice != hostRemovedDoor and newDoorChoice != contestantDoorChoice:
                newDoorChoice = random.randint(0, self.nDoors - 1)

            wins += 1 if doors[newDoorChoice] == "CAR" else 0

        percentageWins = (wins / trials) * 100
        #calculating banana case wins
        bananaPercentageWins = (bananaLose / trials) * 100
        print("There is a " + str(percentageWins) + "% chance of winning if you switch to another door if there are originally " + str(self.nDoors) + " doors possible. ")
        #printing banana case wins
        print("For 100000 trials, there is a " + str(bananaPercentageWins) + "% chance of host slipping on a banana and instantly losing.\n")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
trialOf3 = DoorsTrial(3)
trialOf3.keepDoor()
trialOf3.switchDoor()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

trialOf6 = DoorsTrial(6)
trialOf6.keepDoor()
trialOf6.switchDoor()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

trialOf9 = DoorsTrial(9)
trialOf9.keepDoor()
trialOf9.switchDoor()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

trialOf20 = DoorsTrial(20)
trialOf20.keepDoor()
trialOf20.switchDoor()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

trialOf100 = DoorsTrial(100)
trialOf100.keepDoor()
trialOf100.switchDoor()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

#Black Jack Monty Carlo Simulation
# Policy 1: hand >= 17
# Policy 2: hand >= 17 && hard, else hit until ==21
# Policy 3: Always stick
# Run for 2 additional policies we make up as well
# Run as infinite deck and single deck. Start with infinite


#the below is for policies 1-3 for an infinite deck
import random

class BlackJackHand:
    def __init__(self, policy):
        self.policy = policy
    def testFunction(self):
        trials = 10000
        totalSum = 0
        averageSum = 0
        losses = 0
        for i in range(trials):
            deckOfCards = [2,3,4,5,6,7,8,9,10,10,10,11]
            #ace can technically be a 1 or 11, add implementation of this later
            condition = 0
            #0 = hard, 1 = soft
            sum = 0
            while (self.policy == 1 and sum < 17):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
            while(self.policy == 2 and sum < 17 and condition == 0):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
                if(currentCard == 11):
                    condition = 1
            while(self.policy == 3 and sum < 22):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
            totalSum += sum
            if sum > 21:
                losses += 1
        averageSum = (totalSum/trials)
        print("For policy " + str(self.policy) + " the average hand sum is " + str(averageSum) + " and have an average of " + str(losses) + " losses out of " + str(trials) + " trials")
policy1 = BlackJackHand(1)
policy1.testFunction()
policy2 = BlackJackHand(2)
policy2.testFunction()
policy3 = BlackJackHand(3)
policy3.testFunction()
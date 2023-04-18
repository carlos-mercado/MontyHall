# Black Jack Monty Carlo Simulation
# Policy 1: hand >= 17
# Policy 2: hand >= 17 && hard, else hit until ==21
# Policy 3: Always stick
# Policy 4: hand >20 (wins only on exactly 21)
# Policy 5: hit until hand is soft
# Run for 2 additional policies we make up as well
# Run as infinite deck and single deck. Start with infinite
import random

class BlackJackHand:
    def __init__(self, policy):
        self.policy = policy
    def testFunction(self):
        trials = 10000
        totalSum = 0
        averageSum = 0
        finiteTotalSum = 0
        finiteAverageSum = 0
        finiteLosses = 0
        losses = 0
        for i in range(trials):
            deckOfCards = [1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,11,11]
            # inefficent, but can be fixed
            #ace can technically be a 1 or 11, assume 11 for this assignment
            condition = 0
            #0 = hard, 1 = soft
            sum = 0
            #infinite deck
            #policy 1
            while (self.policy == 1 and sum < 17):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
            #policy 2
            while(self.policy == 2 and ((sum < 17 and condition == 0) or (sum < 22 and condition == 1))):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
                if(currentCard == 11 or 1):
                    condition = 1
            #policy 3
            while(self.policy == 3 and sum < 22):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
            #policy 4
            while(self.policy == 4 and sum < 21):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
            #policy 5
            while(self.policy == 5 and condition == 0 and sum < 22):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
                if(currentCard == 11 or 1):
                    condition = 1
            totalSum += sum
            if sum > 21:
                losses += 1
            #finite deck
            condition = 0
            sum = 0
            while (self.policy == 1 and sum < 17):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
                del deckOfCards[currentCard]
            while(self.policy == 2 and ((sum < 17 and condition == 0) or (sum < 22 and condition == 1))):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
                if(currentCard == 11 or 1):
                    condition = 1
                del deckOfCards[currentCard]
            while(self.policy == 3 and sum < 22):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
                del deckOfCards[currentCard]
            while(self.policy == 4 and sum < 21):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
                del deckOfCards[currentCard]
            while(self.policy == 5 and condition == 0 and sum < 22):
                currentCard = random.choice(deckOfCards)
                sum += currentCard
                if(currentCard == 11 or 1):
                    condition = 1
                del deckOfCards[currentCard]
            finiteTotalSum += sum
            if sum > 21:
                finiteLosses += 1
        averageSum = (totalSum/trials)
        finiteAverageSum = (finiteTotalSum/trials)
        print("For an infinite deck:")
        print("For policy " + str(self.policy) + " the average hand sum is " + str(averageSum) + " and have an average of " + str(losses) + " losses out of " + str(trials) + " trials")
        print("For a finite deck:")
        print("For policy " + str(self.policy) + " the average hand sum is " + str(finiteAverageSum) + " and have an average of " + str(finiteLosses) + " losses out of " + str(trials) + " trials")
policy1 = BlackJackHand(1)
policy1.testFunction()
print("----------------------------------------------------------------------")
policy2 = BlackJackHand(2)
policy2.testFunction()
print("----------------------------------------------------------------------")
policy3 = BlackJackHand(3)
policy3.testFunction()
print("----------------------------------------------------------------------")
policy4 = BlackJackHand(4)
policy4.testFunction()
print("----------------------------------------------------------------------")
policy5 = BlackJackHand(5)
policy5.testFunction()
print("----------------------------------------------------------------------")
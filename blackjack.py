# Black Jack Monty Carlo Simulation
# Policy 1: hand >= 17, stick
# Policy 2: hand >= 17 and hard stick, else hit unless == 21
# Policy 3: Always stick
# Policy 4: hit until we are at 21
# Policy 5: hit until face card
import random
import matplotlib.pyplot as plt

def generate_card():
    deck = [1,1,1,1, \
            2,2,2,2, \
            3,3,3,3, \
            4,4,4,4, \
            5,5,5,5, \
            6,6,6,6, \
            7,7,7,7, \
            8,8,8,8, \
            9,9,9,9, \
            10,10,10,10, \
            10,10,10,10, \
            10,10,10,10, \
            10,10,10,10]

    card = random.choice(deck)
    if card == 11:
        card = 1
    return card

def simulate_game(policy):
    # initialize game state
    dealer_cards = [generate_card(), generate_card()]
    player_cards = [generate_card(), generate_card()]
    player_stick = False
    dealer_stick = False
    while True:
        player_sum = sum(player_cards)
        dealer_sum = sum(dealer_cards)
        # check for blackjack
        if player_sum == 21:
            return 1 if dealer_sum != 21 else 0
        elif dealer_sum == 21:
            return -1
        # check for player bust
        elif player_sum > 21:
            return -1
        # check for dealer bust
        elif dealer_sum > 21:
            return 1
        
        # policy 1
        if policy == 1:
            if player_sum >= 17:
                player_stick = True
            else:
                player_cards.append(generate_card())
        # policy 2
        elif policy == 2:
            if player_sum >= 17 and not (1 in player_cards):
                player_stick = True
            elif player_sum == 21:
                player_stick = True
            else:
                player_cards.append(generate_card())
        # policy 3
        elif policy == 3:
            player_stick = True
        # policy 4
        elif policy == 4:
            if player_sum < 21:
                player_cards.append(generate_card())
        # policy 5
        elif policy == 5:
            if 10 not in player_cards:
                player_cards.append(generate_card())
            else:
                player_stick = True

        # player sticks
        if player_stick:
            while dealer_sum < 17:
                dealer_cards.append(generate_card())
                dealer_sum = sum(dealer_cards)
            if dealer_sum > 21:
                return 1
            elif dealer_sum > player_sum:
                return -1
            elif dealer_sum < player_sum:
                return 1
            else:
                return 0

def estimate_policy(policy, num_simulations):
    total_reward = 0
    total_wins = 0
    total_losses = 0
    for i in range(num_simulations):
        result = simulate_game(policy)
        total_reward += result
        total_wins += 1 if result == 1 else 0
        total_losses += 1 if result == -1 else 0
    return (total_wins,total_losses, total_reward/num_simulations)

def simulate_single_deck(policy):
    deck = [1,1,1,1, \
            2,2,2,2, \
            3,3,3,3, \
            4,4,4,4, \
            5,5,5,5, \
            6,6,6,6, \
            7,7,7,7, \
            8,8,8,8, \
            9,9,9,9, \
            10,10,10,10, \
            10,10,10,10, \
            10,10,10,10, \
            10,10,10,10]
    
    random.shuffle(deck)

    dealer_cards = [deck.pop(), deck.pop()]
    player_cards = [deck.pop(), deck.pop()]
    player_stick = False
    dealer_stick = False
    while True:
        player_sum = sum(player_cards)
        dealer_sum = sum(dealer_cards)
        # check for blackjack
        if player_sum == 21:
            return 1 if dealer_sum != 21 else 0
        elif dealer_sum == 21:
            return -1
        # check for player bust
        elif player_sum > 21:
            return -1
        # check for dealer bust
        elif dealer_sum > 21:
            return 1
        
        # policy 1
        if policy == 1:
            if player_sum >= 17:
                player_stick = True
            else:
                player_cards.append(deck.pop())
        # policy 2
        elif policy == 2:
            if player_sum >= 17 and not (1 in player_cards):
                player_stick = True
            elif player_sum == 21:
                player_stick = True
            else:
                player_cards.append(deck.pop())
        # policy 3
        elif policy == 3:
            player_stick = True
        # policy 4
        elif policy == 4:
            if player_sum < 21:
                player_cards.append(deck.pop())
        # policy 5
        elif policy == 5:
            if 10 not in player_cards:
                player_cards.append(deck.pop())
            else:
                player_stick = True

        # player sticks
        if player_stick:
            while dealer_sum < 17:
                dealer_cards.append(deck.pop())
                dealer_sum = sum(dealer_cards)
            if dealer_sum > 21:
                return 1
            elif dealer_sum > player_sum:
                return -1
            elif dealer_sum < player_sum:
                return 1
            else:
                return 0

def estimate_policy_singleDeck(policy, num_simulations):
    total_reward = 0
    total_wins = 0
    total_losses = 0
    for i in range(num_simulations):
        result = simulate_single_deck(policy)
        total_reward += result
        total_wins += 1 if result == 1 else 0
        total_losses += 1 if result == -1 else 0
    return (total_wins,total_losses, total_reward/num_simulations)

(p1_wins, p1_losses, p1_er) = estimate_policy(1, 100000)
(p2_wins, p2_losses, p2_er) = estimate_policy(2, 100000)
(p3_wins, p3_losses, p3_er) = estimate_policy(3, 100000)
(p4_wins, p4_losses, p4_er) = estimate_policy(4, 100000)
(p5_wins, p5_losses, p5_er) = estimate_policy(5, 100000)


#(p1_wins_single, p1_losses_single, p1_er_single) = estimate_policy_singleDeck(1, 100000)
#(p2_wins_single, p2_losses_single, p2_er_single) = estimate_policy_singleDeck(2, 100000)
#(p3_wins_single, p3_losses_single, p3_er_single) = estimate_policy_singleDeck(3, 100000)
#(p4_wins_single, p4_losses_single, p4_er_single) = estimate_policy_singleDeck(4, 100000)
(p5_wins_single, p5_losses_single, p5_er_single) = estimate_policy_singleDeck(5, 100000)

xAxis = ["Infinite", "Single"]
yAxis = [p5_wins, p5_wins_single]

plt.bar(xAxis, yAxis)
plt.xlabel('Deck Type')
plt.ylabel('Wins')
plt.title('Infinite vs. Single Deck Policy 5')

# add labels to the top of each bar
for i in range(len(xAxis)):
    plt.text(i, yAxis[i] + 0.5, str(yAxis[i]), ha='center')

plt.show()

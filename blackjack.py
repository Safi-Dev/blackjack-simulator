import random

def deal_card():
    return random.randint(1, 11)

def play_blackjack(strategy):
    player_total = deal_card() + deal_card()
    dealer_card = deal_card()

    while True:
        action = strategy(player_total, dealer_card)
        if action == "Surrender":
            return -0.5 
        elif action == "Stand":
            break
        elif action == "Hit":
            player_total += deal_card()
            if player_total > 21:
                return -1  
        elif action == "Double":
            player_total += deal_card()
            if player_total > 21:
                return -1  
            break


    dealer_total = dealer_card + deal_card()
    while dealer_total < 17:
        dealer_total += deal_card()
        if dealer_total > 21:
            return 1  

    if dealer_total > player_total:
        return -1  
    elif dealer_total < player_total:
        return 1  
    else:
        return 0  
    
def basic_strategy(player_total, dealer_card):
    if player_total >= 17:
        return "Stand"  # Stand if player total is 17 or higher
    elif player_total <= 11:
        return "Hit"    # Always hit if player total is 11 or lower
    elif player_total == 12 and dealer_card in [4, 5, 6]:
        return "Stand"  # Stand if player total is 12 and dealer's card is 4, 5, or 6
    elif player_total >= 13 and player_total <= 16 and dealer_card in [2, 3, 4, 5, 6]:
        return "Stand"  # Stand if player total is 13 to 16 and dealer's card is 2 to 6
    elif player_total == 16 and dealer_card in [9, 10, 11]:
        return "Surrender"  # Surrender if player total is 16 and dealer's card is 9, 10, or Ace
    else:
        return "Hit" 

def simulate_games(strategy, num_games):
    wins = 0
    losses = 0
    ties = 0

    for _ in range(num_games):
        result = play_blackjack(strategy)
        if result == 1:
            wins += 1
        elif result == -1:
            losses += 1
        else:
            ties += 1

    return wins, losses, ties

if __name__ == "__main__":
    num_games = 100000
    wins, losses, ties = simulate_games(basic_strategy, num_games)

    print("Results after", num_games, "games:")
    print("Wins:", wins)
    print("Losses:", losses)
    print("Ties:", ties)
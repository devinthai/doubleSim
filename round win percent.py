"""
round win percent was created to simulate the casino mode in DanMachi Memoria Freeze.
Author: u/sxedevin
Date: 8/11/2018
"""
import numpy as np

def chooseCard(size):
    card = np.random.randint(size)
    
    return card

def choice1():
    """
        choice1 represents the strategy of always picking the same card
    """
    return 2
    
def choice2():
    """
        choice2 represents the strategy of picking a random facedown card
    """
    choice = np.random.randint(4)
    return choice

def genDown1():
    """
        genDown1 uses the revised rules
    """
    down = []
        #generate 3 random cards
    for i in range(3):
        size = len(deck)
        spot = chooseCard(size)
        card = deck.pop(spot)
        
        down = down + [card]
    
        #generate the guaranteed winning card
    down = down + [15]
    np.random.shuffle(down)
    return down

def genDown2():
    """
        genDown2 uses the old rules
    """
    down = []
        #generate 3 random cards
    for i in range(4):
        size = len(deck)
        spot = chooseCard(size)
        card = deck.pop(spot)
        
        down = down + [card]
    
        #generate the guaranteed winning card
    np.random.shuffle(down)
    return down

def round1():
    #generate the cards in a suit
    suit = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    
    #generate a deck
    deck = suit + suit + suit + suit + [15]
    np.random.shuffle(deck)
    
    #choose the house card
    size = len(deck)
    spot = chooseCard(size)
    
    while(deck[spot] == 15):
        #the house cannot have a joker as their card
        spot = chooseCard(size)
    
    house = deck.pop(spot)
    
    #generate the four facedown cards
    down = []
    method = 1
    if(method==0):
        #generate 3 random cards
        for i in range(3):
            size = len(deck)
            spot = chooseCard(size)
            card = deck.pop(spot)
            
            down = down + [card]
        
            #generate the guaranteed winning card
            
        #if they're going to just add a joker
        #down = down + [15]
        
        #if they're going to add one higher card
        if(house == 14 and 15 in deck):
            down = down + [15]
        elif(house == 14 and 15 not in deck):
            size = len(deck)
            spot = chooseCard(size)
            card = deck.pop(spot)
            down = down + [card]
        else:
            down = down + [15]
        
        np.random.shuffle(down)
        
    if(method!=0):
        #generate 4 random cards
        for i in range(4):
            size = len(deck)
            spot = chooseCard(size)
            card = deck.pop(spot)
            
            down = down + [card]
        np.random.shuffle(down)
    
    #make your choice, choice1 for always same spot, choice2 for random
    spot = choice2()
    choice = down.pop(spot)
    
    #count the number of cards you could have won with
    winningCards = sum(1 for i in down if i>house)
    
    #check win conditions
    if choice > house:
        return 1, winningCards
    if choice == house:
        return 0, winningCards
    if choice < house:
        return -1, winningCards

def playRound():
    res = round1()
    if(res[0] == 0):
        playRound()
    if(res[0] < 0):
        return 0, res[1]
    else:
        return res

def main():
    """
        main simulates a given amount of rounds and outputs the win percentages and
        average number of winning cards per round respectively.
    """
    rounds = 500000
    
    winning = 0
    score = 0
    
    for i in range(rounds):
        res = playRound()
        score = score + res[0]
        winning = winning + res[1]
    
    return float(score)/rounds, float(winning)/(rounds)
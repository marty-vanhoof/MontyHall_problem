import numpy as np 
import random

def prizedoor(n):
    '''Given a positive integer n, return a random array of length n
    where each entry is either 0, 1, or 2 representing a hidden 
    prize behind door 0, 1, or 2.  Run n simulations of the prizedoor.'''
    
    return np.random.randint(3, size = n)

def initial_guess(n):
    '''This function also returns a random array of length n consisting
    of 0s, 1s, and 2s representing n simulations of contestants guessing
    a door randomly.'''
    
    return np.random.randint(3, size = n)

def goatdoor(prizedoors, guesses):
    '''This function simulates opening a "goat door" for each prize door
    and each guess.  The goat door should not be the prize door and should 
    be different from the contestant's guess.  Returns an array of goatdoors
    for n Monty Hall games.'''
    
    goatdoors = []
    # loop over all pairs of prizedoors and guesses
    for pair in zip(prizedoors, guesses):
        if pair[0] == pair[1]:
            # if the contestant guesses the prizedoor, Monty randomly picks one of the two remaining doors 
            other_doors = [ d for d in [0,1,2] if d != pair[0] ]
            goatdoors.append( random.choice(other_doors) )
        else:
            # if the guess is different from the prizedoor, Monty picks the one remaining door
            other_door = [ d for d in [0,1,2] if d not in (pair[0], pair[1]) ]
            goatdoors.append( other_door[0] )
        
    return np.array(goatdoors)

def switch_guess(guesses, goatdoors):
    '''This function implements the strategy of always switching
    a guess after a goat door is opened.  Returns an array of length
    n representing the contestants switching doors in n Monty Hall games.'''
    
    switches = []
    # loop over all pairs of guesses and goatdoors
    for pair in zip(guesses, goatdoors):
        # the contestant only has one choice of door to switch to after the goatdoor is opened
        switch_door = [ d for d in [0,1,2] if d not in (pair[0], pair[1]) ]
        switches.append( switch_door[0] )
        
    return np.array(switches)

def run_monty(n, switch=True):
    '''Simulate n Monty Hall games.  The default value of switch
    represents the contestants always switching their initial guess.
    Set switch=False to simulate the contestants not switching.'''
    
    prizedoors = prizedoor(n)
    guesses = initial_guess(n)
    goatdoors = goatdoor(prizedoors, guesses)
    if switch:
        contestantdoors = switch_guess(guesses, goatdoors)
    else:
        contestantdoors = guesses
        
    wins = 0
    # loop over all pairs of prizedoors and contestantdoors
    for pair in zip(prizedoors, contestantdoors):
        # if a prizedoor is the same as the corresponding contestantdoor, then
        # the contestant wins
        if pair[0] == pair[1]:
            wins += 1
            
    # print the relevant stats
    print('  Number of games: ', n)
    print('  Number of wins:  ', wins)
    print('  Win Percentage:   %.2f% %' % round(100 * wins / n, 2) )

print('Monty Hall simulations with switching the initial guess: ')
run_monty(100000, switch=True)
print()
print('Monty Hall simulations with not switching the initial guess: ')
run_monty(100000, switch=False)
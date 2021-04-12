#!/usr/bin/python3

import random, sys

print('ROCK, PAPER, SCISSORS!')

# tracking wins, losses and draws
wins = 0
losses = 0
draws = 0

while True: # main game loop
    print('%s Wins, %s Losses, %s Draws' % (wins,losses,draws))
    while True: # player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quits 
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # breaks out of the player loop and back into the main loop
        print('Type one of r, p, s, or q.')

    # display player choice
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # display computer choice
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')      

    # displays and record w/l/d

    if playerMove == computerMove:
        print('It\'s a draw!')
        draws = draws + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1                
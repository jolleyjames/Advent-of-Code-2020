'''
Advent of Code 2020, Day 22.
James Jolley, jim.jolley [at] gmail.com
'''

import numpy as np

def load_decks(path):
    '''
    Load hands for players for a game of Combat.
    '''
    player1 = []
    with open(path) as file:
        # skip 'Player 1' header
        file.readline()
        # load player 1's cards
        while True:
            line = file.readline().strip()
            if line != '':
                player1.append(int(line))
            else:
                # skip 'Player 2' header
                file.readline()
                break
        # load player 2's cards
        player2 = [int(line) for line in file.readlines()]
    return player1, player2

def play_round(p1, p2):
    '''
    Play a round of Combat with the players' decks. After the round, the
    winner will have their card followed by the loser's card at the end
    of their deck.
    '''
    if p1[0] == p2[0]:
        raise ValueError('ties undefined')
    winner,loser = (p1,p2) if p1[0] > p2[0] else (p2,p1)
    winner.extend((winner[0],loser[0]))
    del winner[0]
    del loser[0]

def play_game(p1, p2):
    '''
    Play an entire game of Combat. End when a player is out of cards.
    '''
    while len(p1) > 0 and len(p2) > 0:
        play_round(p1, p2)

def score(winner):
    '''
    Return the winner's score using their deck at the end of the game.
    '''
    winner = np.array(winner)
    return np.sum(winner * np.array(range(len(winner),0,-1)))

def play_recursive_game(p1, p2, inf_game_flag=1):
    '''
    Play a game of Recursive Combat. Since a game may end with both
    players holding cards, return the winning player (1 or 2).
    '''
    previous_hands = set()
    while len(p1) > 0 and len(p2) > 0:
        this_hand = (tuple(p1),tuple(p2))
        if this_hand in previous_hands:
            return inf_game_flag
        else:
            previous_hands.add(this_hand)
        # Check if this round is a sub-game
        if p1[0] < len(p1) and p2[0] < len(p2):
            winner = play_recursive_game(list(p1[1:]), list(p2[1:]))
            winner, loser = (p1,p2) if winner == 1 else (p2,p1)
            winner.extend((winner[0], loser[0]))
            del winner[0]
            del loser[0]
        else:
            play_round(p1, p2)
    return 1 if len(p1) > 0 else 2

if __name__ == '__main__':
    # part 1
    p1, p2 = load_decks('input/day22.txt')
    play_game(p1,p2)
    print(score(p1 if len(p1) > 0 else p2))
    # part 2
    p1, p2 = load_decks('input/day22.txt')
    winner = play_recursive_game(p1,p2)
    print(score(p1 if winner == 1 else p2))



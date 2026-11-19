import random
import pandas as pd 

def make_game() :
    return sorted(random.sample(range(1, 46), 6 ))

def make_games(count) :
    games =[]
    for i in range(count) :
        games.append(make_game())
    return games

def to_text(game) :
    words = []
    for i in game :
        words.append(f'{i:5d}')
    return '  '.join(words)
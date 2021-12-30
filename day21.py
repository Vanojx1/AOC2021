import re
from itertools import product
from functools import lru_cache

with open('input\\day21') as f:
    puzzle_input = f.read().splitlines()

class Dice(object):
    def __init__(self, faces) -> None:
        self.value = 1
        self.nroll = 0
        self.faces = faces
    
    def inc(self):
        self.value += 1
        if self.value == self.faces+1: self.value = 1

    def roll(self):
        self.nroll += 3
        def _():
            for _ in range(3):
                yield self.value
                self.inc()
        return sum(_())

class Win(StopIteration): pass
class Player(object):
    def __init__(self, id, start_pos, raise_on_win=False) -> None:
        self.id = id
        self.pos = start_pos
        self.score = 0
        self.raise_on_win = raise_on_win
    
    def move(self, roll):
        self.pos += roll % 10
        if self.pos > 10: self.pos %= 10
        self.score += self.pos
        if self.raise_on_win and self.score >= 1000: raise Win(self.id)
    
    def __repr__(self) -> str:
        return f"P({self.id} => {self.score})"
    
def get_players(raise_on_win=False):
    players = []
    for row in puzzle_input:
        id, start_pos = map(int, re.match(r'Player (\d+) starting position: (\d+)', row).groups())
        players.append(Player(id-1, start_pos, raise_on_win))
    return players

dice = Dice(100)
players = get_players(True)
while True:
    try:
        for player in players:
            player.move(dice.roll())
    except Win as winner:
        loser = players[winner.value^1]
        break
print('Part 1:', loser.score * dice.nroll)


def player_move(pos, score, roll):
    new_pos = ((pos - 1 + roll) % 10) + 1
    new_score = score + new_pos
    return new_pos, new_score

@lru_cache(maxsize=None)
def count_wins(player, pos0, score0, pos1, score1):
    if score0 >= 21:
        return 1, 0
    elif score1 >= 21:
        return 0, 1

    wins = [0, 0]
    for rolls in product(range(1, 4), repeat=3):
        if player == 0:
            new_pos, new_score = player_move(pos0, score0, sum(rolls))
            wins0, wins1 = count_wins(1, new_pos, new_score, pos1, score1)
        else:
            new_pos, new_score = player_move(pos1, score1, sum(rolls))
            wins0, wins1 = count_wins(0, pos0, score0, new_pos, new_score)

        wins[0] += wins0
        wins[1] += wins1
    return wins

p1, p2 = get_players(True)
wins = count_wins(0, p1.pos, 0, p2.pos, 0)

print('Part 2:', max(wins))
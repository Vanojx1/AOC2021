#  ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████      █████▒▒█████   ██▀███   ▄████▄  ▓█████     ▄▄▄▄    ██▀███   █    ██  ██░ ██  ▐██▌ 
# ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀    ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀    ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓██░ ██▒ ▐██▌ 
# ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███      ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███      ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒██▀▀██░ ▐██▌ 
# ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄    ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄    ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░▓█ ░██  ▓██▒ 
# ░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒   ░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒   ░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓ ░▓█▒░██▓ ▒▄▄  
# ░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░    ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░   ░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒  ▒ ░░▒░▒ ░▀▀▒ 
# ▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░    ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░   ▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░  ▒ ░▒░ ░ ░  ░ 
#  ░    ░   ░░   ░  ░░░ ░ ░   ░         ░       ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░       ░    ░   ░░   ░  ░░░ ░ ░  ░  ░░ ░    ░ 
#  ░         ░        ░                 ░  ░              ░ ░     ░     ░ ░         ░  ░    ░         ░        ░      ░  ░  ░ ░    
#       ░                                                               ░                        ░                                 

import re
from point import Point

with open('input\\day17') as f:
    puzzle_input, = f.read().splitlines()

X1, X2, Y1, Y2 = map(int, re.match(r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)', puzzle_input).groups())

class Probe(object):

    def __init__(self, vel_x, vel_y):
        self.curr_pos = Point(0, 0)
        self.vel_pair = (vel_x, vel_y)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.max_y = 0

    def move(self):
        self.curr_pos += Point(self.vel_x, self.vel_y)
        self.max_y = max(self.max_y, self.curr_pos.y)
        if self.vel_x > 0:
            self.vel_x -= 1
        elif self.vel_x < 0:
            self.vel_x += 1
        self.vel_y -= 1
    
    def check_hit(self):
        while True:
            if Y1 <= self.curr_pos.y <= Y2 and \
               X1 <= self.curr_pos.x <= X2: return self.vel_pair
            if self.curr_pos.x > X2 or self.curr_pos.y < Y1: break
            self.move()

valid_hits = set([])
max_y = 0
for vel_x in range(0, 1000):
    for vel_y in range(-500, 500):
        pr = Probe(vel_x, vel_y)
        if pos := pr.check_hit():
            valid_hits.add(pos)
            max_y = max(max_y, pr.max_y)
        
print('Part 1:', max_y)
print('Part 2:', len(valid_hits))

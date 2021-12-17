import re
from point import Point
from itertools import product
import pygame

with open('input\\day17') as f:
    puzzle_input, = f.read().splitlines()

x1, x2, y1, y2 = map(int, re.match(r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)', puzzle_input).groups())

print(x1, x2, y1, y2)

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def to_pygame(coords):
    """Convert coordinates into pygame coordinates (lower-left => top left)."""
    return (coords[0], SCREEN_HEIGHT - abs(coords[1]))


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))

circle = pygame.draw.circle(screen, (0, 0, 0), to_pygame([0, 0]), 25)

area = pygame.draw.rect(screen, (0, 0, 0), (*to_pygame([x1, y1]), abs(x2-x1), abs(y2-y1)))

print('POS',  (*to_pygame([x1, y1]), abs(x2-x1), abs(y2-y1)))

pygame.display.update()

# Main loop
running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

class Probe(object):

    def __init__(self, vel_x, vel_y):
        self.curr_pos = Point(0, 0)
        self.vel_x = vel_x
        self.vel_y = vel_y

    def move(self):
        self.curr_pos += Point(self.vel_x, self.vel_y)
        if self.vel_x > 0:
            self.vel_x -= 1
        elif self.vel_x < 0:
            self.vel_x += 1
        self.vel_y -= 1

valid_x = set([])
for vel in range(1, x2):
    p = Probe(vel, 0)
    while p.curr_pos.x <= x2 and p.vel_x != 0:
        p.move()
        if x1 <= p.curr_pos.x <= x2:
            # print('Valid', vel)
            valid_x.add(vel)

valid_y = set([])
vel = 1
while True:
    p = Probe(0, vel)
    # print(p.curr_pos)
    found = False
    while p.curr_pos.y >= y2:
        p.move()
        if y1 <= p.curr_pos.y <= y2:
            # print('Valid', vel)
            found = True
            valid_y.add(vel)
    if not found: break
    vel += 1

print(valid_x)
# print(valid_y)

max_y = 0
for x, y in product(valid_x, valid_y):
    p = Probe(x, y)
    while True:
        p.move()
        max_y = max(max_y, p.curr_pos.y)
        if y1 <= p.curr_pos.y <= y2: break

print(max_y)
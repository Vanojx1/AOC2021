from point import Point

with open('input\\day11') as f:
    puzzle_input = [list(map(int, r)) for r in f.read().splitlines()]

def singleton(cls):
    instances = {}
    def getinstance(x, y, *args):
        if (x, y) not in instances:
            instances[(x, y)] = cls(x, y, *args)
        return instances[(x, y)]
    return getinstance

@singleton
class Fish(Point):

    def __init__(self, x, y, power=0):
        super().__init__(x, y)
        self.power = power
        self.flashed = False
    
    def charge(self):
        if self.flashed: return False
        self.power += 1
        if self.power > 9:
            self.flashed = True
            [f.charge() for f in self.around]
            return True
        return False
    
    def check_charge(self):
        if self.power > 9:
            self.flashed = False
            self.power = 0
            return 1
        return 0
    
    def reset(self):
        self.flashed = False

    @property
    def around(self):
        for f in {Fish(self.x+o.real, self.y+o.imag) for o in (1+0j, 1+1j, 1j, -1+1j, -1+0j, -1-1j, -1j, 1-1j)}:
            if f in Fish.domain: yield f

fish_mapping = {Fish(x, y, l) for y, row in enumerate(puzzle_input) for x, l in enumerate(row)}
Fish.domain = fish_mapping

step = 1
total_flash = 0
while True:

    for fish in fish_mapping: fish.charge()

    def check():
        for f in fish_mapping: yield f.check_charge()
    
    flashed = sum(check())
    total_flash += flashed

    if step == 100:
        print('Part 1:', total_flash)

    if flashed == 100:
        print('Part 2:', step)
        break

    step += 1
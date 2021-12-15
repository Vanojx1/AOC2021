import  heapq as hq
from point import Point
from termcolor import colored

with open('input\\day15') as f:
    puzzle_input = f.read().splitlines()

class Cave(object):
    def __init__(self, risk_mapping, full_size=False):
        self.risk_mapping = risk_mapping
        self.full_size = full_size

        self.start = Point(0, 0)
        stop = max(risk_mapping.keys())
        self.BASE_SIZE = stop.x+1
        self.SIZE = self.full_size and self.BASE_SIZE*5 or self.BASE_SIZE
        self.stop = Point(self.SIZE-1, self.SIZE-1)

    def __contains__(self, pos):
        return pos.x >= 0 and pos.y >= 0 and pos.x <= self.stop.x and pos.y <= self.stop.y
 
    def get(self, pos):
        if self.full_size:
            xoff, x = pos.x // self.BASE_SIZE, pos.x % self.BASE_SIZE
            yoff, y = pos.y // self.BASE_SIZE, pos.y % self.BASE_SIZE
            return int((self.risk_mapping[Point(x, y)] + (xoff + yoff)-1) % 9)+1
        return self.risk_mapping[pos]

    def get_path(self):
        q = [(0, [self.start])]
        hq.heapify(q)
        visited = set([self.start])
        
        while q:
            tr, path = hq.heappop(q)

            if path[-1] == self.stop: return tr, path

            for n in (path[-1]+o for o in (1, 1j, -1, -1j)):
                if n in self and n not in visited:
                    hq.heappush(q, (tr+self.get(n), path+[n]))
                    visited.add(n)

    def print(self, path):
        print('-'*(self.SIZE+2))
        for y in range(self.stop.y+1): print('|' + ''.join([(lambda p: colored(str(self.get(p)), p in path and 'green' or 'grey'))(Point(x, y)) for x in range(self.stop.x+1)]) + '|')
        print('-'*(self.SIZE+2))


risk_mapping = {Point(x,y): int(r) for y, row in enumerate(puzzle_input) for x, r in enumerate(row)}

cave = Cave(risk_mapping)
risk, path = cave.get_path()
print('Part 1:', risk)
# cave.print(path)

cave = Cave(risk_mapping, full_size=True)
risk, path = cave.get_path()
print('Part 2:', risk)
# cave.print(path)


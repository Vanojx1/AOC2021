class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __hash__(self): return hash((self.x, self.y))
    def __lt__(self, o): return (self.y, self.x) < (o.y, o.x)
    def __eq__(self, o): return (self.y, self.x) == (o.y, o.x)
    def __radd__(self, o):
        if isinstance(o, complex): o = Point(o.real, o.imag)
        elif isinstance(o, int): o = Point(o, 0)
        return Point(self.x+o.x, self.y+o.y)
    def __add__(self, o):
        if isinstance(o, complex): o = Point(o.real, o.imag)
        elif isinstance(o, int): o = Point(o, 0)
        return Point(self.x+o.x, self.y+o.y)
    def __rsub__(self, o):
        if isinstance(o, complex): o = Point(o.real, o.imag)
        elif isinstance(o, int): o = Point(o, 0)
        return Point(self.x-o.x, self.y-o.y)
    def __sub__(self, o):
        if isinstance(o, complex): o = Point(o.real, o.imag)
        elif isinstance(o, int): o = Point(o, 0)
        return Point(self.x+o.x, self.y+o.y)
    def __repr__(self): return f'P({int(self.x)},{int(self.y)})'
    def dist(self, p2): return abs(self.x-p2.x) + abs(self.y-p2.y)

class Point(object):
    def check_type(fn):
        def wrap(self, o):
            if isinstance(o, complex): o = Point(o.real, o.imag)
            elif isinstance(o, int): o = Point(o, 0)
            return fn(self, o)
        return wrap
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __hash__(self): return hash((self.x, self.y))
    @check_type
    def __lt__(self, o): return (self.y, self.x) < (o.y, o.x)
    @check_type
    def __eq__(self, o): return (self.y, self.x) == (o.y, o.x)
    @check_type
    def __radd__(self, o): return Point(self.x+o.x, self.y+o.y)
    @check_type
    def __add__(self, o): return Point(self.x+o.x, self.y+o.y)
    @check_type
    def __rsub__(self, o): return Point(self.x-o.x, self.y-o.y)
    @check_type
    def __sub__(self, o): return Point(self.x+o.x, self.y+o.y)
    def __repr__(self): return f'P({int(self.x)},{int(self.y)})'
    def dist(self, p2): return abs(self.x-p2.x) + abs(self.y-p2.y)

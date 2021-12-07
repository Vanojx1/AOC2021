class Point(complex):
    def __hash__(self): return hash((self.real, self.imag))
    def __eq__(self, o): return self.real == o.real and self.imag == o.imag
    def __lt__(self, o): return (self.imag, self.real) < (o.imag, o.real)
    def __radd__(self, o): return Point(complex.__radd__(self, o))
    def __add__(self, o): return Point(complex.__add__(self, o))
    def __rsub__(self, o): return Point(complex.__rsub__(self, o))
    def __sub__(self, o): return Point(complex.__sub__(self, o))
    def __repr__(self): return f'P({int(self.real)},{int(self.imag)})'
    def dist(self, p2): return abs(self.x-p2.x) + abs(self.y-p2.y)
    @property
    def x(self): return int(self.real)
    @property
    def y(self): return int(self.imag)

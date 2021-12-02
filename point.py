class Point(complex):
    def __hash__(self): return hash((self.real, self.imag))
    def __eq__(self, other): return self.real == other.real and self.imag == other.imag
    def __lt__(self, other): return abs(self) < abs(other)
    def __radd__(self, other): return Point(complex.__radd__(self, other))
    def __add__(self, other): return Point(complex.__add__(self, other))
    def __rsub__(self, other): return Point(complex.__rsub__(self, other))
    def __sub__(self, other): return Point(complex.__sub__(self, other))
    def __repr__(self): return f'P({int(self.real)},{int(self.imag)})'

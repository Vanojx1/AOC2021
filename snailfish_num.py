import math
from termcolor import COLORS, colored

color_list = list(COLORS.keys())

class SnailfishNum(object):
    def __init__(self, num, parent=None, level=1, rl=None):
        self.num = num
        self.left = None
        self.right = None
        self.parent = parent
        self.level = level
        self.rl = rl

        self.num.pop(0)
        if self.num[0] in '0123456789':
            n = []
            while self.num[0] in '0123456789': n.append(self.num.pop(0))
            self.left = int(''.join(n))    
        elif self.num[0] == '[':
            self.left = SnailfishNum(self.num, self, level+1, 'L')
        self.num.pop(0)
        if self.num[0] in '0123456789':
            n = []
            while self.num[0] in '0123456789': n.append(self.num.pop(0))
            self.right = int(''.join(n))
        elif self.num[0] == '[':
            self.right = SnailfishNum(self.num, self, level+1, 'R')
        self.num.pop(0)

    @property
    def index(self):
        if self.parent is None: return ''
        return self.rl + self.parent.index

    @property
    def is_pair(self):
        return isinstance(self.left, int) and isinstance(self.right, int)

    @property
    def can_reduce(self):
        return self.level == 5 and self.is_pair
    
    @property
    def magnitude(self):
        return 3 * (self.left.magnitude if isinstance(self.left, SnailfishNum) else self.left) + \
               2 * (self.right.magnitude if isinstance(self.right, SnailfishNum) else self.right)

    def get_explode_pair(self):
        if self.can_reduce: return self
        if isinstance(self.left, SnailfishNum) and (el1 := self.left.get_explode_pair()): return el1
        if isinstance(self.right, SnailfishNum) and (el2 := self.right.get_explode_pair()): return el2

    def get_split_target(self):
        if isinstance(self.left, int) and self.left > 9: return (self, 'L')
        if isinstance(self.left, SnailfishNum) and (el1 := self.left.get_split_target()): return el1
        if isinstance(self.right, int) and self.right > 9: return (self, 'R')
        if isinstance(self.right, SnailfishNum) and (el2 := self.right.get_split_target()): return el2

    def reduce(self):
        explode_pair = self.get_explode_pair()
        if explode_pair:
            ord_nums = list(self.get_as_list())
            index_left = [i for i, (path, rl, el) in enumerate(ord_nums) if (path, rl) == (explode_pair.index, 'L')][0]
            if index_left > 0:
                _, rl, el = ord_nums[index_left-1]
                if rl == 'L': el.left += explode_pair.left
                else: el.right += explode_pair.left

            ord_nums = list(self.get_as_list())
            index_right = [i for i, (path, rl, el) in enumerate(ord_nums) if (path, rl) == (explode_pair.index, 'R')][0]
            if index_right < len(ord_nums)-1:
                _, rl, el = ord_nums[index_right+1]
                if rl == 'L': el.left += explode_pair.right
                else: el.right += explode_pair.right

            if explode_pair.rl == 'L': explode_pair.parent.left = 0
            else: explode_pair.parent.right = 0

            return True
        
        split_target = self.get_split_target()
        if split_target:
            t, side = split_target
            if side == 'L':
                str_num = f"[{math.floor(t.left/2)},{math.ceil(t.left/2)}]"
                t.left = SnailfishNum(list(str_num), t, t.level+1, side)
            else:
                str_num = f"[{math.floor(t.right/2)},{math.ceil(t.right/2)}]"
                t.right = SnailfishNum(list(str_num), t, t.level+1, side)
            return True

    @property
    def root(self):
        return self.parent.root if self.parent else self
    
    def get_as_list(self):
        if isinstance(self.left, int): yield (self.index, 'L', self)
        else: yield from self.left.get_as_list()
        if isinstance(self.right, int): yield (self.index, 'R', self)
        else: yield from self.right.get_as_list()

    def colored(self):
        l = self.left if isinstance(self.left, int) else self.left.colored()
        r = self.right if isinstance(self.right, int) else self.right.colored()
        return f"{colored('[', color_list[self.level-1])}{l},{r}{colored(']', color_list[self.level-1])}"

    def __repr__(self):
        return f"[{self.left},{self.right}]"
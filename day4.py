with open('input\\day4') as f:
    puzzle_input = f.read().splitlines()

class Board(object):

    def __init__(self, rows):
        parsed_rows = [list(map(int, r.replace('  ', ' ').strip().split(' '))) for r in rows]
        self.cols = [set([r[i] for r in parsed_rows]) for i in range(len(parsed_rows[0]))]
        self.rows = [set(rc) for rc in parsed_rows]

    def extract(self, n):
        for r, c in zip(self.rows, self.cols): (r.discard(n), c.discard(n))
        if any(len(r) == 0 for r in self.rows) or any(len(c) == 0 for c in self.cols):
            unmarked_sum = sum([sum(r) for r in self.rows])
            return unmarked_sum * n
        return False

numbers, *boards = puzzle_input
numbers = list(map(int, numbers.split(',')))
boards = [b for b in boards if len(b) > 0]

i = 0
bingo = []
while True:
    rows = boards[i:i+5]
    i += 5
    if not rows: break
    bingo.append(Board(rows))

winners = set([])
scores = []
for n in numbers:
    for i, board in enumerate(bingo):
        if (score := board.extract(n)) and i not in winners:
            scores.append(score)
            winners.add(i)

print('Part 1:', scores[0])
print('Part 2:', scores[-1])
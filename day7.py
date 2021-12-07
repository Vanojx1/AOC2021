with open('input\\day7') as f:
    puzzle_input, = f.read().splitlines()

crabs = list(map(int, puzzle_input.split(',')))
targets = list(range(min(crabs), max(crabs)))

def dist(a, b): return b-a

min_fuel = min(sum([abs(c-t) for c in crabs]) for t in targets)

print('Part 1:', min_fuel)

def dist(a, b): return sum(i+1 for i in range(b-a))

min_fuel = min(sum([dist(*sorted([t, c])) for c in crabs]) for t in targets)

print('Part 2:', min_fuel)

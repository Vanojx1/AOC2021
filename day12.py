from collections import defaultdict

with open('input\\day12') as f:
    puzzle_input = f.read().splitlines()

cave_tree = defaultdict(list)
for a, b in map(lambda x: x.split('-'), puzzle_input):
    if b != 'start': cave_tree[a].append(b)
    if a != 'start': cave_tree[b].append(a)

def gen_paths(check_twice=False):
    q = [(['start'], False)]
    while q:
        path, twice = q.pop()

        if path[-1] == 'end':
            yield path
            continue

        for next_cave in sorted(cave_tree[path[-1]], reverse=True):
            if next_cave == 'end' or next_cave.isupper() or next_cave not in path or (check_twice and not twice):
                q.append((path + [next_cave], twice or next_cave.islower() and next_cave in path))


print('Part 1:', len(list(gen_paths())))
print('Part 2:', len(list(gen_paths(True))))
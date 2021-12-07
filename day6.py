from collections import Counter

with open('input\\day6') as f:
    puzzle_input, = f.read().splitlines()

day = 1
spawn_schedule = Counter([n for n in map(int, puzzle_input.split(','))])
total_fish = sum(v for k, v in spawn_schedule.items())
while day < 256:
    for k in list(spawn_schedule.keys()):
        if k == day:
            spawn_schedule.update({day+7: spawn_schedule[k]})
            spawn_schedule.update({day+9: spawn_schedule[k]})
            total_fish += spawn_schedule[k]
    day += 1

    if day == 80: print('Part 1:', total_fish)
    if day == 256: print('Part 2:', total_fish)

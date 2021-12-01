with open('input\\day1') as f:
    puzzle_input = list(map(int, f.read().splitlines()))

inc = 0
for i in range(1, len(puzzle_input)):
    if puzzle_input[i] > puzzle_input[i-1]: inc += 1

print('Part 1:', inc)

inc = 0
window_list = list(map(lambda x: sum([puzzle_input[x], puzzle_input[x+1], puzzle_input[x+2]]), range(len(puzzle_input)-2)))
for i in range(1, len(window_list)):
    if window_list[i] > window_list[i-1]: inc += 1

print('Part 2:', inc)
import re

with open('input\\day8') as f:
    puzzle_input = f.read().splitlines()

total = 0
for pattern, out in map(lambda r: r.split('|'), puzzle_input):
    one = re.findall(r'\b[a-g]{2}\b', out)
    four = re.findall(r'\b[a-g]{4}\b', out)
    seven = re.findall(r'\b[a-g]{3}\b', out)
    eight = re.findall(r'\b[a-g]{7}\b', out)
    total += len(one) + len(four) + len(seven) + len(eight)

print('Part 1:', total)

total = 0
for pattern, out in map(lambda r: r.split(' | '), puzzle_input):  
    s_pattern = sorted(map(lambda x: ''.join(sorted(x)), pattern.split(' ')), key=len)

    n_1 = set(s_pattern[0])
    n_4 = set(s_pattern[2])
    n_7 = set(s_pattern[1])
    n_8 = set(s_pattern[9])
    n_235 = map(set, s_pattern[3:6])
    n_069 = map(set, s_pattern[6:9])

    L = n_4 - n_1

    for n in n_235:
        if n_1.issubset(n): n_3 = n
        elif L.issubset(n): n_5 = n
        else: n_2 = n

    for n in n_069:
        if n_4.issubset(n): n_9 = n
        elif L.issubset(n): n_6 = n
        else: n_0 = n

    nums_mapping = [n_0, n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9]
    num = int(''.join([str(nums_mapping.index(n)) for n in map(set, out.split(' '))]))
    total += num

print('Part 2:', total)

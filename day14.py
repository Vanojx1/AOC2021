from collections import defaultdict, Counter

with open('input\\day14') as f:
    template, _, *rules = f.read().splitlines()

rules = {k: v for k, v in map(lambda x: x.split(' -> '), rules)}

pairs = defaultdict(int, Counter([template[i:i+2] for i in range(len(template)-1)]))
elements = Counter(template)

step = 1
while True:
    for k, v in list(pairs.items()):
        if v == 0: continue
        a, b = k
        pairs[k] -= v
        pairs[a+rules[k]] += v
        pairs[rules[k]+b] += v
        elements.update({rules[k]: v})

    if step == 10:
        print('Part 1:', max(elements.values()) - min(elements.values()))
    if step == 40:
        print('Part 2:', max(elements.values()) - min(elements.values()))
        break
    step += 1

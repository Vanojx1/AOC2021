from collections import Counter

with open('input\\day3') as f:
    puzzle_input = f.read().splitlines()


count = [Counter(n[i] for n in puzzle_input) for i in range(len(puzzle_input[0]))]
most_commons = [c.most_common(1)[0][0] for c in count]
least_commons = [c.most_common()[-1][0] for c in count]
gamma_rate = int(''.join(most_commons), 2)
epsilon_rate = int(''.join(least_commons), 2)

print('Part 1:', gamma_rate * epsilon_rate)

nums = puzzle_input
for i in range(len(puzzle_input[0])):
    (v1, n1), (v2, n2) = Counter(n[i] for n in nums).most_common()
    most_common = '1' if n1 == n2 else (v1 if n1 > n2 else v2)
    nums = [n for n in nums if n[i] == most_common]
    if len(nums) == 1:
        oxygen_generator_rating = int(nums[0], 2)
        break

nums = puzzle_input
for i in range(len(puzzle_input[0])):
    (v1, n1), (v2, n2) = Counter(n[i] for n in nums).most_common()
    least_common = '0' if n1 == n2 else (v1 if n1 < n2 else v2)
    nums = [n for n in nums if n[i] == least_common]
    if len(nums) == 1:
        CO2_scrubber_rating = int(nums[0], 2)
        break

print('Part 2:', oxygen_generator_rating * CO2_scrubber_rating)
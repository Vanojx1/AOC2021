import re
from packet_parser import PacketParser

with open('input\\day16') as f:
    puzzle_input, = f.read().splitlines()

root_packet = list(re.sub(r'(\w)', lambda x: bin(int(x.group(1), 16)).replace('0b', '').zfill(4), puzzle_input))

packet = PacketParser(root_packet)

packet.print()

print('Part 1:', packet.version_sum)
print('Part 2:', packet.value)


from functools import reduce
from treelib import Tree

class PacketParser(object):

    OP_MAPPING = {
        0: lambda sub: reduce(lambda a, b: a + b, map(lambda p: p.value, sub), 0),
        1: lambda sub: reduce(lambda a, b: a * b, map(lambda p: p.value, sub), 1),
        2: lambda sub: min(map(lambda p: p.value, sub)),
        3: lambda sub: max(map(lambda p: p.value, sub)),
        5: lambda sub: sub[0].value > sub[1].value and 1 or 0,
        6: lambda sub: sub[0].value < sub[1].value and 1 or 0,
        7: lambda sub: sub[0].value == sub[1].value and 1 or 0,
    }

    def __init__(self, packet, level=0, parent=None):
        self.packet = packet
        self.parent = parent
        self.level = level
        self.length = 0
        self.version = int(self.pop_n(3), 2)
        self.type_id = int(self.pop_n(3), 2)
        self.sub_packets = []
        self.value = None
        
        if self.type_id != 4:
            length_type_ID = int(self.pop_n(1), 2)
            if length_type_ID == 0:
                total_length_in_bits = int(self.pop_n(15), 2)
                while sum(map(lambda s: s.length, self.sub_packets)) < total_length_in_bits: self.sub_packets.append(PacketParser(self.packet, level+1, self))
            else:
                number_of_sub = int(self.pop_n(11), 2)
                for _ in range(number_of_sub): self.sub_packets.append(PacketParser(self.packet, level+1, self))
        
        if self.type_id == 4:
            self.value = self.parse_as_literal()
        else:
            self.value = PacketParser.OP_MAPPING[self.type_id](self.sub_packets)
    
    def print(self, tree=None, index=None, parent=None):
        if tree is None:
            tree = Tree()
            tree.create_node(f"Version: {self.version}, Type ID: {self.type_id}, Value: {self.value}", f"{self.level}-root")
            for sub_index, sub in enumerate(self.sub_packets): sub.print(tree, sub_index, f"{self.level}-root")
            tree.show()
        else:
            name = f"{self.level}-{index}" + parent
            tree.create_node(f"Version: {self.version}, Type ID: {self.type_id}, Value: {self.value}", name, parent=parent)
            for sub_index, sub in enumerate(self.sub_packets): sub.print(tree, sub_index, name)

    @property
    def version_sum(self):
        return self.version + sum(sub.version_sum for sub in self.sub_packets)

    def pop_n(self, n):
        self.update_length(n) 
        def pop(popped=0):
            if popped == n: return ''
            return self.packet.pop(0) + pop(popped+1)
        return pop()
    
    def update_length(self, n):
        self.length += n
        if self.parent: self.parent.update_length(n)

    def parse_as_literal(self):
        n = ''
        while True:
            k = self.pop_n(5)
            prefix, g = k[0], k[1:]
            n += g
            if prefix == '0': break
        return int(n, 2)
import random

class Cache:
    def __init__(self, size, num_blocks, replacement_policy):
        self.size = size
        self.num_blocks = num_blocks
        self.replacement_policy = replacement_policy
        self.blocks = [[] for i in range(num_blocks)]
        self.usage_counters = [[0 for j in range(size//num_blocks)] for i in range(num_blocks)]
        self.hits = 0
        self.misses = 0

    def find(self, address):
        block_number = address % self.num_blocks
        tag = address // self.num_blocks
        set_number = tag % (self.size//self.num_blocks)
        set_contents = self.blocks[block_number][set_number]

        if tag in set_contents:
            self.hits += 1
            block_index = set_contents.index(tag)
            self.usage_counters[block_number][set_number][block_index] += 1
        else:
            self.misses += 1
            if len(set_contents) < self.size//self.num_blocks:
                self.blocks[block_number][set_number].append(tag)
                block_index = len(set_contents)
            else:
                block_index = self.replacement_policy(self.usage_counters[block_number][set_number])
                self.blocks[block_number][set_number][block_index] = tag
                self.usage_counters[block_number][set_number][block_index] = 1

    def print_stats(self):
        print('Hits: ', self.hits)
        print('Misses: ', self.misses)
        print('Hit rate: {:.2%}'.format(self.hits / (self.hits + self.misses)))

def lru_replacement_policy(usage_counters):
    return usage_counters.index(min(usage_counters))

def lfu_replacement_policy(usage_counters):
    return usage_counters.index(min(usage_counters))

def fifo_replacement_policy(usage_counters):
    return usage_counters.index(0)

# Exemplo de uso
cache_size = 16
num_blocks = 4
cache = Cache(cache_size, num_blocks, lru_replacement_policy)
addresses = [random.randint(0, 255) for i in range(100)]
for address in addresses:
    cache.find(address)
cache.print_stats()

from random import *
from d.memory import MemoryFIFO, MemoryCLOCK

MAX_PAGE_NUM = 10;
RAND_SEED = 42;

class Requests:
    def __init__(self, algo):
        random.seed(RAND_SEED);
        if algo == 'FIFO':
            self.memory = MemoryFIFO();
        if algo == 'CLOCK':
            self.memory = MemoryCLOCK();

    # Generates next page to be visited
    def nextPage(self, method='uniform'):
        roll = -1
        if method == 'uniform':
            roll = random.randint(0,MAX_PAGE_NUM);
        if method == 'exp':
            roll = random.expovariate(1.0/MAX_PAGE_NUM);
        if method == 'c':
            pass;
        # Roll for read or write
        rw = random.randint(0,1);
        if rw == 0 :
            # Read Only
            try:
                self.memory.readPage(roll);
            except LookupError as e:
                self.memory.alloc(roll);
        elif rw == 1:
            # Write to memory
            try:
                self.memory.writePage(roll);
            except LookupError as e:
                self.memory.alloc(roll);
        return;
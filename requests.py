from random import *
from memory import MemoryFIFO, MemoryCLOCK

class Requests:
    def __init__(self, maxPage, seed=None):
        random.seed(seed);
        self.maxPage = maxPage;

    # Generates next page to be visited
    def nextPage(self, method='uniform'):
        roll = -1
        if method == 'uniform':
            return self.uniform();
        if method == 'exp':
            return self.exp();
        if method == 'c':
            pass;
        # Roll for read or write
        # rw = random.randint(0,1);
        # if rw == 0 :
        #     # Read Only
        #     try:
        #         self.memory.readPage(roll);
        #     except LookupError as e:
        #         self.memory.alloc(roll);
        # elif rw == 1:
        #     # Write to memory
        #     try:
        #         self.memory.writePage(roll);
        #     except LookupError as e:
        #         self.memory.alloc(roll);
        # return;

    def uniform(self):
        return random.randint(0,self.maxPage);

    def exp(self):
        roll = random.expovariate(1.0/self.maxPage);
        if roll > self.maxPage: roll = self.maxPage;
        roll = round(roll, None);
        return roll;
    


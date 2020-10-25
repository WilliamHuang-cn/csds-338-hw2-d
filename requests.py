import random
from memory import MemoryFIFO, MemoryCLOCK
import math
class Requests:
    def __init__(self, maxPage, ranSeed=None):
        random.seed(ranSeed);
        self.maxPage = maxPage;
        # Generate a sequence of exponential distributions
        lambd = 1.0/self.maxPage;
        seq = []
        for i in range(self.maxPage):
            seq.append((lambd * math.exp(-lambd*i)) - (lambd * math.exp(-lambd*(i+1))));

        # Flattern the curve!
        flat = sum(seq[3:10]);
        for i in range(3,10):
            seq[i] = flat;

        self.weight = seq;

    # Generates next page to be visited
    def nextPage(self, method):
        roll = -1
        if method == 'uniform':
            return self.uniform();
        if method == 'exp':
            return self.exp();
        if method == 'c':
            return self.c();

    def uniform(self):
        return random.randint(0,self.maxPage);

    def exp(self):
        roll = random.expovariate(1.0/self.maxPage);
        if roll > self.maxPage: roll = self.maxPage;
        roll = round(roll, None);
        return roll;

    def c(self):
        return random.choices(range(self.maxPage), weights=self.weight)[0];

    


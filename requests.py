import random
from memory import MemoryFIFO, MemoryCLOCK

class Requests:
    def __init__(self, maxPage, ranSeed=None):
        random.seed(ranSeed);
        self.maxPage = maxPage;

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

        return;

    


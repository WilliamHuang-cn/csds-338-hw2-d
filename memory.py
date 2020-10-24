from page import page;

# Maximum number of pages stored in memory
MEM_LEN = 3;

class Memory:
    def __init__(self):
        self.physicalMemory = [];
        self.virtualMemory = [];
        pass;

    # Allocate pages into physical Memory
    def malloc(numberOfPages):
        pass;

    # Swap designated pages in to memory
    def swapIn(pageIndex):
        pass;

    # Swap designated pages out of memory
    def swapOut(pageIndex):
        pass;

    # Read from a certain page
    def access(pageIndex):
        pass;

    # Free a page from physical/virtual memory
    def free(pageIndex):
        pass;

class MemoryFIFO(memory):

    # Override with FIFO algorithm
    def swapOut(pageIndex):
        pass;

class MemoryCLOCK(memory):

    # Override with CLOCK algorithm
    def swapOut(pageIndex):
        pass;
    pass;
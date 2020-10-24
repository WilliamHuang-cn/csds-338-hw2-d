from page import page;

# Maximum number of pages stored in memory
MEM_LEN = 3;

class Memory:
    def __init__(self):
        self.physicalMemory = [None]*MEM_LEN;
        self.virtualMemory = [];
        pass;

    # Allocate pages into physical Memory
    def malloc(self, pageList):
        # WIP
        numberOfPages = len(pageList);
        while numberOfPages > 0:
            memIndex = self.nextFreeSpace();
            if memIndex == -1: 
                # Not enough memory avaliable. Need to swap some out
                pass;
            
            pass;

    # Swap designated pages in to memory
    def swapIn(self, pageIndex):
        pass;

    # Swap designated pages out of memory
    # Need to be override with subclasses 
    def swapOut(self, memoryIndex):
        raise BufferError("No swap algorithm specified. Cannot swap out to virtual memory");

    # Read from a certain page
    def access(self, pageIndex):
        pass;

    # Free a page from physical/virtual memory
    def free(self, pageIndex):
        pass;

    # Check for the next avaliable free memory space
    # Returns the index 
    def nextFreeSpace(self):
        for x in range(MEM_LEN):
            if self.physicalMemory[x] == None: return x;
        return -1;

class MemoryFIFO(memory):

    # Override with FIFO algorithm
    def swapOut(pageIndex):
        pass;

class MemoryCLOCK(memory):

    # Override with CLOCK algorithm
    def swapOut(pageIndex):
        pass;
    pass;
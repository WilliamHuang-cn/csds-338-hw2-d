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
    def swapOut(self):
        int temp = 0
        int index = 0
        for i in range(len(physicalMemory)):
            nextTemp = self.physicalMemory(i).age
            if nextTemp > temp  
                temp = nextTemp 
                index = i
        page = self.physicalMemory.pop(i)
        page.age = 0
        virtualMemory.append(page)
        self.physicalMemory.insert(i, None)
        return i
        pass

class MemoryCLOCK(memory):

    # Override with CLOCK algorithm
    def swapOut(self):
        page =  self.physicalMemory.pop(clockHand)
        virtualMemory.append(page)
        self.physicalMemory.insert(clockHand, None)
        return clockHand
            
        pass;
    pass;
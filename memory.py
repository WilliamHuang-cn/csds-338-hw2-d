from page import Page;

# Maximum number of pages stored in memory
MEM_LEN = 3;

class Memory:
    def __init__(self):
        self.physicalMemory = [None]*MEM_LEN;
        self.virtualMemory = [];        # We assume the size of virtual memory to be infinitive
        pass;

    # Allocate pages in physical Memory
    def alloc(self, pageList):
        for page in pageList:
            memIndex = self.nextFreeSpace();
            if memIndex == -1: 
                # Not enough memory avaliable. Page fault
                # Need to swap one out
                memIndex = self.swapOut();
            self.physicalMemory[memIndex] = page;

    # Swap designated pages in to memory
    def swapIn(self, pageIndex):
        # Find page in virtual memtory
        tmpIndex = self.findPage(self.virtualMemory, pageIndex);
        if tmpIndex == -1: 
            raise LookupError("Page not found in virtual memory.");
        tmpPage = self.virtualMemory.pop(tmpIndex);
        # Get a free position, or swap one out 
        memIndex = self.nextFreeSpace();
        if memIndex == -1:
            memIndex = self.swapOut();
        self.physicalMemory[memIndex] = tmpPage;
        

    # Swap designated pages out of memory according to algorithm
    # Need to be override with subclasses 
    # Returns the memory index of the page being swapped out
    def swapOut(self):
        raise NotImplementedError("No swap algorithm specified. Cannot swap out to virtual memory.");

    # Read from a certain page
    def readPage(self, pageIndex):
        tmpIndex = self.findPage(self.physicalMemory, pageIndex);
        if tmpIndex == -1: 
            raise LookupError("No such page.");
            return;
        (Page)(self.physicalMemory[tmpIndex]).referenced = 1;
    
    # Write data into a certain page
    def writePage(self, pageIndex):
        tmpIndex = self.findPage(self.physicalMemory, pageIndex);
        if tmpIndex == -1: 
            raise LookupError("No such page.");
            return;
        (Page)(self.physicalMemory[tmpIndex]).dirty = 1;
        (Page)(self.physicalMemory[tmpIndex]).referenced = 1;

    # Free a page from physical/virtual memory
    def free(self, pageIndex):
        tmpIndex = self.findPage(self.physicalMemory, pageIndex);
        if tmpIndex != -1: 
            self.physicalMemory[tmpIndex] = None;
        else: 
            tmpIndex = self.findPage(self.virtualMemory, pageIndex);
            if tmpIndex == -1:
                raise LookupError("No such page.");
                return;
            self.virtualMemory.pop(tmpIndex);


    # Check for the next avaliable free memory space
    # Returns the index 
    def nextFreeSpace(self):
        for x in range(MEM_LEN):
            if self.physicalMemory[x] == None: return x;
        return -1;

    def findPage(self, memory, pageIndex):
        tmpIndex = -1;
        for x in range(len(self.virtualMemory)):
            if self.virtualMemory[x].index == pageIndex:
                tmpIndex = x;
                break;
        return tmpIndex;

class MemoryFIFO(Memory):

    # Override with FIFO algorithm
    def swapOut(self):
        temp = 0
        index = 0
        for i in range(len(self.physicalMemory)):
            nextTemp = self.physicalMemory[i].age
            if nextTemp > temp:
                temp = nextTemp 
                index = i
        page = self.physicalMemory.pop(i)
        page.age = 0
        self.virtualMemory.append(page)
        self.physicalMemory.insert(i, None)
        return index
        pass

class MemoryCLOCK(Memory):

    # Override with CLOCK algorithm
    def swapOut(self):
        page =  self.physicalMemory.pop(clockHand)
        self.virtualMemory.append(page)
        self.physicalMemory.insert(clockHand, None)
        return clockHand
            
        pass;
    pass;
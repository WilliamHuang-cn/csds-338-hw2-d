from memory import MemoryCLOCK, MemoryFIFO
from requests import Requests

# Total number of request generated
NUM_REQUESTS = 100;
RAND_SEED = 42;
MAX_PAGE_NUM = 10;

# Maximum number of pages stored in memory
MEM_LEN = 3;

if __name__ == "__main__":

    requests = Requests(MAX_PAGE_NUM, RAND_SEED);

    print("Starting simulation ...");
    print("Total number of page faults will be measured for each algorithm. ");
    print("Number of page request generated: {0}".format(NUM_REQUESTS));

    print('---------------------------------------------------------------------')
    print('Type A request pattern: Uniform distribution')

    fifo = MemoryFIFO();
    clock = MemoryCLOCK();

    for x in range(NUM_REQUESTS):
        ran = requests.nextPage();
        fifo.readPage(ran);
        clock.readPage(ran);
    
    print();


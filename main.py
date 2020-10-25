from memory import MemoryCLOCK, MemoryFIFO
from requests import Requests

# Total number of request generated
NUM_REQUESTS = 20;
RAND_SEED = 4;
MAX_PAGE_NUM = 10;

# Maximum number of pages stored in memory
MEM_LEN = 5;

DEBUG = 0;

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
        ran = requests.nextPage('uniform');
        fifo.readPage(ran);
        clock.readPage(ran);
        if DEBUG == 1:
            print('Generated page index: '+str(ran));
            print(fifo);
            print(clock);
            print();
    
    print('FIFO page faults: '+str(fifo.pageFaults));
    print('FIFO number of swaps: '+str(fifo.numberOfSwaps));
    print('FIFO hit ratio: '+str(fifo.hit/NUM_REQUESTS));

    print('CLOCK page faults: '+str(clock.pageFaults));
    print('CLOCK number of swaps: '+str(clock.numberOfSwaps));
    print('CLOCK hit ratio: '+str(clock.hit/NUM_REQUESTS));

    print('---------------------------------------------------------------------')
    print('Type B request pattern: Exponential distribution')

    fifo = MemoryFIFO();
    clock = MemoryCLOCK();

    for x in range(NUM_REQUESTS):
        ran = requests.nextPage('exp');
        fifo.readPage(ran);
        clock.readPage(ran);
        if DEBUG == 1:
            print('Generated page index: '+str(ran));
            print(fifo);
            print(clock);
    
    print('FIFO page faults: '+str(fifo.pageFaults));
    print('FIFO number of swaps: '+str(fifo.numberOfSwaps));
    print('FIFO hit ratio: '+str(fifo.hit/NUM_REQUESTS));

    print('CLOCK page faults: '+str(clock.pageFaults));
    print('CLOCK number of swaps: '+str(clock.numberOfSwaps));
    print('CLOCK hit ratio: '+str(clock.hit/NUM_REQUESTS));

    # print('---------------------------------------------------------------------')
    # print('Type C request pattern: Exponential distribution + Uniform over 3 to 10')

    # fifo = MemoryFIFO();
    # clock = MemoryCLOCK();

    # for x in range(NUM_REQUESTS):
    #     ran = requests.nextPage('c');
    #     fifo.readPage(ran);
    #     clock.readPage(ran);
    #     if DEBUG == 1:
    #         print('Generated page index: '+str(ran));
    #         print(fifo);
    #         print(clock);
    
    # print('FIFO page faults: '+str(fifo.pageFaults));
    # print('FIFO number of swaps: '+str(fifo.numberOfSwaps));
    # print('FIFO hit ratio: '+str(fifo.hit/NUM_REQUESTS));

    # print('CLOCK page faults: '+str(clock.pageFaults));
    # print('CLOCK number of swaps: '+str(clock.numberOfSwaps));
    # print('CLOCK hit ratio: '+str(clock.hit/NUM_REQUESTS));


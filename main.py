from memory import MemoryCLOCK, MemoryFIFO
from requests import Requests

# Total number of request generated
NUM_REQUESTS = 100;

if __name__ == "__main__":
    print("Starting simulation ...");
    print("Total number of page faults will be measured for each algorithm. ");
    print("Number of page request generated: {0}".format(NUM_REQUESTS));



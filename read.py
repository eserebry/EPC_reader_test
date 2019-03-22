import threading
import queue
import time

def read_input(inputQueue):
    ''' Reading input from the keyboard '''

    print('Ready for keyboard input:')

    while (True):
        input_str = input()
        inputQueue.put(input_str)

def unique_list(input_EPC):
    '''Creating list of the unique EPC'''

    unique_EPC = [] #list of the unique EPC

    for x in input_EPC:
        if x not in unique_EPC:
            unique_EPC.append(x)

    str = '\n'.join(unique_EPC)
    print("Unique EPC:\n{}".format(str))


def main():
    '''Creating list of the inputed EPC during certain period of time'''

    input_EPC = [] #list of the all EPC inputed
    str = () #list to be converted to string

    inputQueue = queue.Queue()
    inputThread = threading.Thread(target=read_input, args=(inputQueue,), daemon=True)
    inputThread.start()

    start = time.time() #start time functiomn
    STOP_TIME = 5  #program will stop in 5 seconds

    while (True):
        if (inputQueue.qsize() > 0):
            input_str = inputQueue.get()
            input_EPC.append(input_str) 

            if (time.time() > start + STOP_TIME):
               break

    unique_list(input_EPC)

if (__name__ == '__main__'): 
    main()

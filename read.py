import threading
import queue
import time

def read_kbd_input(inputQueue):
    print('Ready for keyboard input:')
    while (True):
        input_str = input()
        inputQueue.put(input_str)

def main():
    EXIT_COMMAND = "exit"
    inputQueue = queue.Queue()

    inputThread = threading.Thread(target=read_kbd_input, args=(inputQueue,), daemon=True)
    inputThread.start()

    input_EPC = [] #list of the all EPC inputed

    unique_EPC = [] #list of unique EPC inputed

    str = ()

    start = time.time()

    PERIOD_OF_TIME = 5  #program will stop in 5  seconds

    while (True):
        if (inputQueue.qsize() > 0):
            input_str = inputQueue.get()
            input_EPC.append(input_str)
            #print("input_str = {}".format(input_str)) #printing string input for debug purposes
            #print("input_EPC = {}".format(input_EPC)) #printing list of unique EPC for debug purposes

        
            if (input_str == EXIT_COMMAND):
                print("Exiting serial terminal.")
                break

            if (time.time() > start + PERIOD_OF_TIME):
               break


    for x in input_EPC:
        if x not in unique_EPC:
            unique_EPC.append(x)
    str = '\n'.join(unique_EPC)
    print("Unique EPC:\n{}".format(str))
    #for x in unique_EPC:
        #print("Unique EPC: {}".format(unique_EPC))

            # Insert your code here to do whatever you want with the input_str.

        # The rest of your program goes here.

    time.sleep(0.01) 
    print("End.")

if (__name__ == '__main__'): 
    main()

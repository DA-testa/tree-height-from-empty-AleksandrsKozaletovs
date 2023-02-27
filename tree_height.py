# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    
    return max_height


def main():
    chose = input()
    if chose in "I" or chose in "i":
        numberInput = input()
        valueInput = input()
        inputResult = compute_height(numberInput,valueInput)
        print(inputResult)
    elif chose in "F" or chose in "f": 
         openFilename = input()
        if openFilename in "a":
            return        
        else:            
            with open(openFilename) as f:
                for line in f:
                    print(line.strip())
            fileResult = compute_height(f,1)
            print(fileResult)
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
#sys.setrecursionlimit(10**7)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()

if __name__ == "__main__":
    main()

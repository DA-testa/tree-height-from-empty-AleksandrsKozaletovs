# python3
# Aleksandrs Kozaļetovs 1.grupa 1.kurss
import sys
import threading
import numpy


def compute_height(countOfSymbols, parentsSymbols):
    # Write this function
    heightsArray = numpy.zeros(countOfSymbols) #create zeros Array   
    max_height = -1 # root
    
    for i in range (len(parentsSymbols)): # cikls, kas iet cauri visiem simboliem 
        element = i       
        heights = 1
        
        while parentsSymbols[element] != -1:
            if heightsArray[element] != 0:
                heights += heightsArray[element] -1
                break
            heights += 1
            element = parentsSymbols[k]
        heightsArray[i] = heights
        max_height = max(max_height,heightsArray[i])
        
   
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
        if "a" in openFilename :
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
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

if __name__ == "__main__":
    main()

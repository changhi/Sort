# Bubble Sort Functions

import sys
from Sort import *


def switch(array, index1):
    tmp = array[index1]
    array[index1] = array[index1 + 1]
    array[index1 + 1] = tmp
    print(array)


def bubbleSort(unsortedArray):
    for n in range(1, len(unsortedArray)):
        change = False
        for x in range(len(unsortedArray) - 1):
            if unsortedArray[x] > unsortedArray[x + 1]:
                switch(unsortedArray, x)
                change = True
        if not change:
            break
        print("After Pass: " + str(n))
    return unsortedArray


def main():
    try:
        userInput = sys.argv[1]
    except Exception as e:
        print(str(e) + "in main()")
    unsortedArrays = convertInput(userInput)
    for num, array in enumerate(unsortedArrays, start=1):
        print("Sorting Array " + str(num) + "...\n" + str(array) + "\nStart:")
        sortedArray = bubbleSort(array)
        print("done!")
        prGreen(str(sortedArray) + "\n")


if __name__ == '__main__':
    main()

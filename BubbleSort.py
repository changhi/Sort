# Bubble Sort Functions

import sys
from Sort import *


def switch(array, index1, index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp


def bubbleSort(unsortedArray):
    print("In Bubble")
    for n in range(len(unsortedArray)):
        for x in range(len(unsortedArray) - 1):
            print("tmp")
    return unsortedArray


def main():
    try:
        userInput = sys.argv[1]
    except Exception as e:
        print(str(e) + "in main()")
    unsortedArrays = convertInput(userInput)
    for num, array in enumerate(unsortedArrays, start=1):
        print("Sorting Array " + str(num) + "...")
        sortedArray = bubbleSort(array)
        print(sortedArray)


if __name__ == '__main__':
    main()

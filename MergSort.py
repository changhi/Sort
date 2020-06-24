# Merg Sort Functions
import sys
import math

from Sort import *


def merge(array1, array2):
    mergedArray = []

    while len(array1) != 0 and len(array2) != 0:
        if array1[0] <= array2[0]:
            add = array1.pop(0)
            mergedArray.append(add)
        else:
            add = array2.pop(0)
            mergedArray.append(add)

    if len(array1) == 0:
        mergedArray.extend(array2)
    elif len(array2) == 0:
        mergedArray.extend(array1)

    return mergedArray


def mergeSort(array):
    if len(array) == 1:
        return array
    mid = math.ceil(len(array) / 2)
    array1 = mergeSort(array[:mid])
    array2 = mergeSort(array[mid:])
    return merge(array1, array2)


def main():
    try:
        userInput = sys.argv[1]
    except Exception as e:
        print(str(e) + "in main()")
    unsortedArrays = convertInput(userInput)
    for num, array in enumerate(unsortedArrays, start=1):
        print("Sorting Array " + str(num) + "...\n" + str(array))
        sortedArray = mergeSort(array)
        print("done!")
        prGreen(str(sortedArray) + "\n")


if __name__ == '__main__':
    main()

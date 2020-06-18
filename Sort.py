# Functions shared by all Sort progams

import json


def convertInput(userInput):
    if ".txt" in userInput:
        try:
            file = open(userInput)
            unsortedArrays = []
            for line in file:
                unsortedArrays.append(json.loads(line))

            return unsortedArrays

        except Exception as e:
            print(str(e) + "in convertInput")

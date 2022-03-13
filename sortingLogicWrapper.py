from sqlite3 import InternalError
import bubbleSortLogic as bubble
import pConstants
class sortingLogicIterator():
    def __init__(self, inputList, sortingAlgo) -> None:
        self.indexList = [x for x in range(len(inputList))]
        if sortingAlgo == "bubbleSort":
            self.algoSpecificIterator = bubble.bubbleSortLogic(inputList)
        # put rest of algos in elifs here
        elif False:
            pass
        else:
            raise ValueError # Not a valid sorting algorithm


    def getValue(self, index: int) -> int:
        return self.algoSpecificIterator.getValue(index)
    
    def getNext(self):
        return self.algoSpecificIterator.getNext()

def indexesToSwap(startList,EndList):
    swaps = []
    for x in range(len(startList)):
        if startList[x] != EndList[x]:
            swaps.append(x)
    return (swaps[0],swaps[1])
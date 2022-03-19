import bubbleSortLogic as bubble
import mergeSortLogic as merge
import pConstants
class sortingLogicIterator():
    def __init__(self, inputList, sortingAlgo) -> None:
        self.swapCount = 0
        self.indexList = [x for x in range(len(inputList))]

        if sortingAlgo == pConstants.BUBBLE:
            self.algoSpecificIterator = bubble.bubbleSortLogic(inputList)
        # put rest of algos in elifs here
        elif sortingAlgo == pConstants.MERGE:
            self.algoSpecificIterator = merge.mergeSortLogic(inputList)
        else:
            raise ValueError # Not a valid sorting algorithm


    def getValue(self, index: int) -> int:
        return self.algoSpecificIterator.getValue(index)
    
    def getNext(self):
        ret = self.algoSpecificIterator.getNext()
        self.swapCount += 1
        return ret
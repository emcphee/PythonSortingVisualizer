

class mergeSortLogic():
    def __init__(self, inputList) -> None:
        self.indexToValueDict = {}
        self.listLen = len(inputList)
        for i in range(len(inputList)):
            self.indexToValueDict[i] = inputList[i]
        self.indexList = [x for x in range(len(inputList))]


    def getValue(self, index: int) -> int:
        return self.indexToValueDict[index]


    def getNext(self):
        
        

        return self.indexList
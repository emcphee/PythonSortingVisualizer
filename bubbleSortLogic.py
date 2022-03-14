

class bubbleSortLogic():
    def __init__(self, inputList) -> None:
        self.indexToValueLookup = inputList
        self.listLen = len(inputList)
        self.indexList = [x for x in range(len(inputList))]
        self.outerForLoop = 0
        self.innerForLoop = 0


    def getValue(self, index: int) -> int:
        return self.indexToValueLookup[index]


    def getNext(self):
        # this code simulates a double for loop generally used in a normal bubble sort algorithm,
        # I modified the algorithm to store all of the state of the double for loop in class instance
        # variables which allows the function to end and return to the state it left off on every time the iterator
        # is called.
        swapDone = False
        while not swapDone and self.outerForLoop < self.listLen:
            while not swapDone and self.innerForLoop < self.listLen - self.outerForLoop - 1:
                if self.getValue(self.indexList[self.innerForLoop]) > self.getValue(self.indexList[self.innerForLoop + 1]):
                    temp = self.indexList[self.innerForLoop]
                    self.indexList[self.innerForLoop]= self.indexList[self.innerForLoop+1]
                    self.indexList[self.innerForLoop+1] = temp
                    swapDone = True
                self.innerForLoop+=1
            # resets inner and increments outer if inner is at end
            if self.innerForLoop >= self.listLen - self.outerForLoop - 1:
                self.innerForLoop = 0
                self.outerForLoop += 1
        # StopIteration is raised when the sorting is completed
        if self.outerForLoop >= self.listLen:
            return None
        return self.indexList
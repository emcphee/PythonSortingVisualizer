import copy

class subList():
    def __init__(self, splitLevel, indexRange) -> None:
        self.splitLevel = splitLevel
        self.indexRange = indexRange
        self.rangeMax = indexRange[1]
        self.rangeMin = indexRange[0]
        self.rangeMiddle = self.rangeMin + (self.rangeMax - self.rangeMin)//2
    

    def leng(self): return self.indexRange[1]-self.indexRange[0]


    def pprint(self):
        print("splitLevel=",self.splitLevel,"Range=",self.indexRange)


class SplitStack():
    def __init__(self) -> None:
        self.stack = []
    

    def peek(self):
        return self.stack[0] if len(self.stack)>0 else None
    

    def pop(self):
        if len(self.stack)>0:
            ret = self.stack[0]
            self.stack = self.stack[1:]
            return ret
        else:
            raise "Popped empty stack"
    

    def push(self, obj):
        self.stack.reverse()
        self.stack.append(obj)
        self.stack.reverse()


    def size(self):
        return len(self.stack)


class MergeStack():
    def __init__(self) -> None:
        self.stack = []
    

    def peek(self):
        return self.stack[0] if len(self.stack)>0 else None
    

    def pop(self):
        if len(self.stack)>0:
            ret = self.stack[0]
            self.stack = self.stack[1:]
            return ret
        else:
            raise "Popped empty stack"
    

    def push(self, obj):
        self.stack.reverse()
        self.stack.append(obj)
        self.stack.reverse()

    
    def topTwoCanMerge(self):
        # makes sure 2 items exist on the stack
        if self.size() >= 2:
            first = self.stack[1]
            second = self.stack[0]
            # checks to make sure the split levels and the last of the first matches the first of the second
            if first.splitLevel == second.splitLevel:
                return True
        return False

    
    def size(self):
        return len(self.stack)


class mergeCacheClass():
    def __init__(self, sub1: subList, sub2: subList, curIndexList, indexToValue) -> None:
        assert sub1.splitLevel == sub2.splitLevel
        assert sub1.rangeMax == sub2.rangeMin or sub2.rangeMax == sub1.rangeMin

        self.indexToValue = indexToValue

        self.splitLevel = sub1.splitLevel - 1

        if sub1.rangeMax != sub2.rangeMin:
            sub1,sub2 = sub2,sub1

        # saves the two ranges to the cache for repeated calls
        self.sub1List = curIndexList[sub1.rangeMin:sub1.rangeMax]
        self.sub2List = curIndexList[sub2.rangeMin:sub2.rangeMax]
        
        # indexlist is saved to be edited by subsequent calls
        self.indexList = curIndexList

        # determines the min and max of the combined lists
        self.totalIndexRange = (min(sub1.rangeMin,sub2.rangeMin), max(sub1.rangeMax,sub2.rangeMax))

        # saves length of combined lists
        self.totalLength = self.totalIndexRange[1] - self.totalIndexRange[0]

    # returns the number of remaining numbers to place
    def remainingPlaces(self):
        return len(self.sub1List) + len(self.sub2List)

    # returns the index that the next number should be placed in
    def _findNextPlaceIndex(self):
        # start index + (length - remaining)                                # this -1 feels sussy
        return self.totalIndexRange[0] + (self.totalLength - self.remainingPlaces() - 1)

    # places the lower of the next numbers from each list into the next index
    def mergeOne(self):
        assert self.remainingPlaces() > 0

        # sub1List is empty so a number must be taken from sub2List
        if len(self.sub1List) == 0:
            nextInt = self.sub2List[0]
            # sub2List has the number removed
            self.sub2List = self.sub2List[1:]
            # index is determined and number is placed
            placeIndex = self._findNextPlaceIndex()
            self.indexList[placeIndex] = nextInt
        # sub2List is empty so a number must be taken from sub1List
        elif len(self.sub2List) == 0:
            nextInt = self.sub1List[0]
            # sub2List has the number removed
            self.sub1List = self.sub1List[1:]
            # index is determined and number is placed
            placeIndex = self._findNextPlaceIndex()
            self.indexList[placeIndex] = nextInt
        # neither lists are empty so the lower of the two numbers is pulled off
        # and placed in the next index location.
        else:
            # sub2List is the minimum so it is popped and set to the indexList
            if self.indexToValue[self.sub1List[0]] > self.indexToValue[self.sub2List[0]]:
                nextInt = self.sub2List[0]
                # sub2List has the number removed
                self.sub2List = self.sub2List[1:]
                # index is determined and number is placed
                placeIndex = self._findNextPlaceIndex()
                self.indexList[placeIndex] = nextInt
            # sub1List is the minimum so it is popped and set to the indexList
            else:
                nextInt = self.sub1List[0]
                # sub2List has the number removed
                self.sub1List = self.sub1List[1:]
                # index is determined and number is placed
                placeIndex = self._findNextPlaceIndex()
                self.indexList[placeIndex] = nextInt
        return self.indexList




class mergeSortLogic():
    def __init__(self, inputList) -> None:
        self.indexToValueLookup = inputList
        self.listLen = len(inputList)
        self.indexList = [x for x in range(len(inputList))]

        # initializes the merge stack as empty
        self.mergeStack = MergeStack()
        # initializes the split stack with the whole list
        self.splitStack = SplitStack()
        startingListObj = subList(0, (0, self.listLen))
        self.splitStack.push(startingListObj)

        # initializes the cache as None
        self.mergeCache = None


    def getVal(self, index: int) -> int:
        return self.indexToValueLookup[index]


    def createNextMergeCache(self):
        cacheCreated = False
        while not cacheCreated:
            if self.mergeStack.topTwoCanMerge():
                # popped second then first because second was
                # the second one put on the stack
                second = self.mergeStack.pop()
                first = self.mergeStack.pop()
                self.mergeCache = mergeCacheClass(first, second, self.indexList, self.indexToValueLookup)
                break
            
            # here we know that we need to split because no merge can be done
            assert self.splitStack.size() > 0
            splitPop = self.splitStack.pop()
            # split this splitPop subList object into two half subList objects
            splitFirstHalf = subList(splitPop.splitLevel+1, (splitPop.rangeMin, splitPop.rangeMiddle))
            splitSecondHalf = subList(splitPop.splitLevel+1, (splitPop.rangeMiddle, splitPop.rangeMax))
            if splitFirstHalf.leng() == 1:
                self.mergeStack.push(splitFirstHalf)
            else:
                self.splitStack.push(splitFirstHalf)
            if splitSecondHalf.leng() == 1:
                self.mergeStack.push(splitSecondHalf)
            else:
                self.splitStack.push(splitSecondHalf)

    
    def getNext(self):

        # returns None if sort completed successfully
        if self.mergeStack.size() == 1 and self.mergeStack.peek().splitLevel == 0:
            return None

        # merge cache is none so new lists need to be merged
        if self.mergeCache == None:
            self.createNextMergeCache()



        prevIndexList = copy.copy(self.indexList)
        # merge cache is guaranteed to exist so
        # it is called for the next placement
        self.indexList = self.mergeCache.mergeOne()

        # each time a new item is merged into place, the item that was previously in that place
        # is moved away to retain there being only 1 of each of the original list on the screen
        # on any given frame.
        # NOTE: this is technically not how mergeSort works at all but it gives a cleaner visual.
        #       in reality, it doesnt do the sort in place and there is extra space that is not visualized.
        indexesChanged = [x for x in range(len(prevIndexList)) if prevIndexList[x] != self.indexList[x]]
        if len(indexesChanged) > 0:
            indexChanged = indexesChanged[0]
            prevValue = prevIndexList[indexChanged]
            newValue = self.indexList[indexChanged]
            newValinPrev = prevIndexList.index(newValue)
            self.indexList[newValinPrev] = prevValue

        # if the mergeCache is out of things to place,
        # it is pushed to the mergeStack as a subList and deleted from the instance variable mergeCache
        if self.mergeCache.remainingPlaces() == 0:
            finishedMergeCache = subList(self.mergeCache.splitLevel, self.mergeCache.totalIndexRange)
            self.mergeStack.push(finishedMergeCache)
            self.mergeCache = None
        return self.indexList

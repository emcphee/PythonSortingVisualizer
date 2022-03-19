from tkinter.tix import TEXT
import sortingLogicWrapper
import graphics
import pConstants
import pygame
import random
import copy


pygame.init()


WIN = pygame.display.set_mode((pConstants.WIDTH,pConstants.HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

icon = pygame.image.load('bluesquare.png')
pygame.display.set_icon(icon)

inputList = [x for x in range(pConstants.LISTSIZE)]
random.shuffle(inputList)

sortIteratorGraph1 = sortingLogicWrapper.sortingLogicIterator(inputList, pConstants.BUBBLE)
sortIteratorGraph2 = sortingLogicWrapper.sortingLogicIterator(inputList, pConstants.MERGE)

# does a swap every 250ms
singleSwapTimer, t = pygame.USEREVENT+1, pConstants.TIMEBETWEENSWAPS
pygame.time.set_timer(singleSwapTimer, t)

# initializes font
myfont = pygame.font.SysFont('Arial', 24)
TEXT_COLOR = (0,0,255)
def mainLoop():
    sortingComplete = False
    clock = pygame.time.Clock()
    run = True


    graph1Bars = graphics.rebuildGraphBars(inputList, sortIteratorGraph1.indexList,1)
    graph2Bars = graphics.rebuildGraphBars(inputList, sortIteratorGraph2.indexList,2)

    while run:
        clock.tick(pConstants.FPSCAP)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == singleSwapTimer:
                if sortIteratorGraph1.indexList != None:
                    sortIteratorGraph1.indexList = sortIteratorGraph1.getNext()
                if sortIteratorGraph2.indexList != None:
                    sortIteratorGraph2.indexList = sortIteratorGraph2.getNext()
                if sortIteratorGraph1.indexList != None:
                    graph1Bars = graphics.rebuildGraphBars(inputList, sortIteratorGraph1.indexList,1)
                if sortIteratorGraph2.indexList != None:
                    graph2Bars = graphics.rebuildGraphBars(inputList, sortIteratorGraph2.indexList,2)
        graphics.drawStatics(WIN)

        graph1swapcount = myfont.render(str(sortIteratorGraph1.swapCount), True, pConstants.GRAPH1_COLOR)
        graph2swapcount = myfont.render(str(sortIteratorGraph2.swapCount), True, pConstants.GRAPH2_COLOR)

        # shows text in the middle of the screen slightly offset to the left
        WIN.blit(graph1swapcount,(30,pConstants.HEIGHT//2))
        WIN.blit(graph2swapcount,(pConstants.DRAWRANGEWIDTH[1] + 30,pConstants.HEIGHT//2))

        for bar in graph1Bars:
            pygame.draw.rect(WIN, pConstants.GRAPH1_COLOR, bar)
        
        for bar in graph2Bars:
            pygame.draw.rect(WIN, pConstants.GRAPH2_COLOR, bar)
        
        pygame.display.update()

    
    pygame.quit()




if __name__ == "__main__":
    mainLoop()

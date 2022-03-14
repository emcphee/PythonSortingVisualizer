"""
Base idea:
user opens up app, it asks which sorting algorithm to use,
then user can either give an input list up to 100 integers, or
random list can be generated for them.

so sortingLogic will get an input list to sort, and the algorithm to use.
"""

import sortingLogicWrapper
import graphics
import pConstants
import pygame
import random

WIN = pygame.display.set_mode((pConstants.WIDTH,pConstants.HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

icon = pygame.image.load('bluesquare.png')
pygame.display.set_icon(icon)

inputList = [x for x in range(pConstants.LISTSIZE)]
random.shuffle(inputList)
sortIterator = sortingLogicWrapper.sortingLogicIterator(inputList, pConstants.ALGO)

# does a swap every 250ms
singleSwapTimer, t = pygame.USEREVENT+1, pConstants.TIMEBETWEENSWAPS
pygame.time.set_timer(singleSwapTimer, t)

def mainLoop():
    sortingComplete = False
    clock = pygame.time.Clock()
    run = True


    graphBars = graphics.rebuildGraphBars(inputList, sortIterator.indexList)

    while run:
        clock.tick(pConstants.FPSCAP)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
            if event.type == singleSwapTimer and not sortingComplete:
                sortIterator.indexList = sortIterator.getNext()
                if sortIterator.indexList != None:
                    graphBars = graphics.rebuildGraphBars(inputList, sortIterator.indexList)
                else:
                    sortingComplete = True
        
        graphics.drawStatics(WIN)

        for bar in graphBars:
            pygame.draw.rect(WIN, pConstants.BAR_COLOR, bar)
        
        pygame.display.update()

    
    pygame.quit()




if __name__ == "__main__":
    mainLoop()

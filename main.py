
import sortingLogicWrapper
import graphics
import interfaceLogic
import pConstants
import pygame
import random
import copy

pygame.init()


WIN = pygame.display.set_mode((pConstants.WIDTH,pConstants.HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

icon = pygame.image.load('bluesquare.png')
pygame.display.set_icon(icon)



# initializes font
myfont = pygame.font.SysFont('Arial', 24)


def mainLoop():
    clock = pygame.time.Clock()

    speed = interfaceLogic.speedSwitcher()
    size = interfaceLogic.sizeSwitcher()

    singleSwapTimer, t = pygame.USEREVENT+1, speed.curSpeed
    pygame.time.set_timer(singleSwapTimer, t)


    run = True
    
    inputList = [x for x in range(size.curSize)]
    sortIteratorGraph1 = None
    sortIteratorGraph2 = None
    graph1Bars = None
    graph2Bars = None

    # start = start
    buttons = []
    buttons.append(graphics.Button(WIN, "start", (pConstants.WIDTH/2 - 20, 15),25,(0,200,0), "start"))
    buttons.append(graphics.Button(WIN, "speedup ", (pConstants.WIDTH/2 - 90, pConstants.HEIGHT - 35),25,(0,200,0), "speedup"))
    buttons.append(graphics.Button(WIN, "slowdown", (pConstants.WIDTH/2 - 190, pConstants.HEIGHT - 35),25,(0,200,0), "slowdown"))
    buttons.append(graphics.Button(WIN, " size up ", (pConstants.WIDTH/2 + 120, pConstants.HEIGHT - 35),25,(0,200,0), "sizeup"))
    buttons.append(graphics.Button(WIN, "size down", (pConstants.WIDTH/2 + 20, pConstants.HEIGHT - 35),25,(0,200,0), "sizedown"))

    restart = False

    graph1Bars = graphics.rebuildGraphBars(inputList, [x for x in range(size.curSize)],1)
    graph2Bars = graphics.rebuildGraphBars(inputList, [x for x in range(size.curSize)],2)
    while run:
        clock.tick(pConstants.FPSCAP)

        if restart:
            inputList = [x for x in range(size.curSize)]
            random.shuffle(inputList)
            restart = False
            sortIteratorGraph1 = sortingLogicWrapper.sortingLogicIterator(inputList, pConstants.BUBBLE)
            sortIteratorGraph2 = sortingLogicWrapper.sortingLogicIterator(inputList, pConstants.MERGE)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            for button in buttons:
                ret = button.click(event)
                if ret:
                    if ret == "start":
                        restart = True
                    if ret == "speedup":
                        if speed.increase():
                            singleSwapTimer, t = pygame.USEREVENT+1, speed.curSpeed
                            pygame.time.set_timer(singleSwapTimer, t)
                    if ret == "slowdown":
                        if speed.decrease():
                            singleSwapTimer, t = pygame.USEREVENT+1, speed.curSpeed
                            pygame.time.set_timer(singleSwapTimer, t)
                    if ret == "sizeup":
                        if size.increase():
                            sortIteratorGraph1 = None
                            sortIteratorGraph2 = None
                            graph1Bars = graphics.rebuildGraphBars([x for x in range(size.curSize)], [x for x in range(size.curSize)],1)
                            graph2Bars = graphics.rebuildGraphBars([x for x in range(size.curSize)], [x for x in range(size.curSize)],2)
                    if ret == "sizedown":
                        if size.decrease():
                            sortIteratorGraph1 = None
                            sortIteratorGraph2 = None
                            graph1Bars = graphics.rebuildGraphBars([x for x in range(size.curSize)], [x for x in range(size.curSize)],1)
                            graph2Bars = graphics.rebuildGraphBars([x for x in range(size.curSize)], [x for x in range(size.curSize)],2)


                
            if event.type == singleSwapTimer:
                if sortIteratorGraph1 != None:
                    if sortIteratorGraph1.indexList != None:
                        sortIteratorGraph1.indexList = sortIteratorGraph1.getNext()
                    if sortIteratorGraph2.indexList != None:
                        sortIteratorGraph2.indexList = sortIteratorGraph2.getNext()
                    if sortIteratorGraph1.indexList != None:
                        graph1Bars = graphics.rebuildGraphBars(inputList, sortIteratorGraph1.indexList,1)
                    if sortIteratorGraph2.indexList != None:
                        graph2Bars = graphics.rebuildGraphBars(inputList, sortIteratorGraph2.indexList,2)
        
        graphics.drawStatics(WIN)
        for button in buttons:
            button.show()

        count1 = sortIteratorGraph1.swapCount if sortIteratorGraph1 != None else 0
        count2 = sortIteratorGraph2.swapCount if sortIteratorGraph2 != None else 0
        graph1swapcount = myfont.render(str(count1), True, pConstants.GRAPH1_COLOR)
        graph2swapcount = myfont.render(str(count2), True, pConstants.GRAPH2_COLOR)

        # shows text in the middle of the screen slightly offset to the left
        WIN.blit(graph1swapcount,(30,pConstants.HEIGHT//2))
        WIN.blit(graph2swapcount,(pConstants.DRAWRANGEWIDTH[1] + 30,pConstants.HEIGHT//2))
        
        if graph1Bars != None:
            for bar in graph1Bars:
                pygame.draw.rect(WIN, pConstants.GRAPH1_COLOR, bar)
            
            for bar in graph2Bars:
                pygame.draw.rect(WIN, pConstants.GRAPH2_COLOR, bar)
        
        pygame.display.update()

    
    pygame.quit()




if __name__ == "__main__":
    mainLoop()

import pygame
import pConstants

def drawStatics(window):
    #fills the background
    window.fill(pConstants.BACKGROUND_COLOR)

    # top ; left to right line
    pygame.draw.line(window, (0, 0, 0), (pConstants.DRAWRANGEWIDTH[0], pConstants.DRAWRANGEHEIGHT[0]), (pConstants.DRAWRANGEWIDTH[1], pConstants.DRAWRANGEHEIGHT[0]))
    # bottom ; left to right line
    pygame.draw.line(window, (0, 0, 0), (pConstants.DRAWRANGEWIDTH[0], pConstants.DRAWRANGEHEIGHT[1]), (pConstants.DRAWRANGEWIDTH[1], pConstants.DRAWRANGEHEIGHT[1]))
    # left ; up to down line
    pygame.draw.line(window, (0, 0, 0), (pConstants.DRAWRANGEWIDTH[0], pConstants.DRAWRANGEHEIGHT[0]), (pConstants.DRAWRANGEWIDTH[0], pConstants.DRAWRANGEHEIGHT[1]))
    # right ; up to down line
    pygame.draw.line(window, (0, 0, 0), (pConstants.DRAWRANGEWIDTH[1], pConstants.DRAWRANGEHEIGHT[0]), (pConstants.DRAWRANGEWIDTH[1], pConstants.DRAWRANGEHEIGHT[1]))


# boxLength = (Width/numBoxes) / (1 + spaceBetweenRatio)
# spaceBetween = boxLength * spaceBetweenRatio

# graph 1 means *.5 , graph 2 means *.5 + drawrang/2
def rebuildGraphBars(originList, indexList, graphNum):
    bars = []
    highestBarVal = max(originList)
    barHeightRatios = [originList[x]/highestBarVal for x in indexList]

    numBoxes = len(originList)
    boxLength = (pConstants.WIDTH*0.8/numBoxes)/2 / (1 + pConstants.SPACEBETWEENBOXESRATIO)
    spaceBetween = boxLength * pConstants.SPACEBETWEENBOXESRATIO
    totalBetweenTwo = boxLength+spaceBetween

    widthOffset = pConstants.DRAWRANGEWIDTH_GRAPH1[0] if graphNum == 1 else pConstants.DRAWRANGEWIDTH_GRAPH2[0]
    for i in indexList:
        # magic 2 is there for fixing offset
        rectPos = (widthOffset + totalBetweenTwo*i + 2, pConstants.DRAWRANGEHEIGHT[0] + (0.8*pConstants.HEIGHT)*(1 - barHeightRatios[i]))
        rectDims = (boxLength, (0.8*pConstants.HEIGHT)*barHeightRatios[i] )
        newRect = pygame.Rect(rectPos, rectDims)
        bars.append(newRect)
    
    return bars
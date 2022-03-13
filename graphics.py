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

def rebuildGraphBars(originList, indexList):
    bars = []
    highestBarVal = max(originList)
    barHeightRatios = [originList[x]/highestBarVal for x in indexList]

    numBoxes = len(originList)
    boxLength = (pConstants.WIDTH*0.8/numBoxes) / (1 + pConstants.SPACEBETWEENBOXESRATIO)
    spaceBetween = boxLength * pConstants.SPACEBETWEENBOXESRATIO
    totalBetweenTwo = boxLength+spaceBetween

    for i in indexList:
        # magic 2 is there for fixing offset
        rectPos = (pConstants.DRAWRANGEWIDTH[0] + totalBetweenTwo*i + 2, pConstants.DRAWRANGEHEIGHT[0] + (0.8*pConstants.HEIGHT)*(1 - barHeightRatios[i]))
        rectDims = (boxLength, (0.8*pConstants.HEIGHT)*barHeightRatios[i] )
        newRect = pygame.Rect(rectPos, rectDims)
        bars.append(newRect)
    
    return bars
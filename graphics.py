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

class Button:
    def __init__(self, WIN, text,  pos, font, fillColor, buttonType):
        self.buttonType = buttonType
        (self.xPos, self.yPos) = pos
        self.WIN = WIN
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, fillColor)
 
    def change_text(self, text, fillColor):
        """Change the text whe you click"""
        self.text = self.font.render(text, True, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(fillColor)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.xPos, self.yPos, self.size[0], self.size[1])
 
    def show(self):
        self.WIN.blit(self.surface, (self.xPos, self.yPos) )
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return self.buttonType

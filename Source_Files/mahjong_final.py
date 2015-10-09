#Hyun Hee(Clara)Kim
#hyunheek
#Term Project: Mahjong Solitaire
#image: The Noun Project 

import pygame, sys
from pygame.locals import * 
from graphicsLibrary1 import *
from time import sleep 
import random
import copy 

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption('Mahjong Solitare')

class MahjongSolitare(object):
    def __init__(self):
        #initial information to make the game
        self.width = 950
        self.height = 600
        self.scoreTile = None 
        self.library = graphicsLibrary()
        self.easyTime = 600
        self.initCounts()
        self.initRowCol()
        self.initData()
        self.tileLevel  =  1
        self.tileSet = self.storeTileSet(self.library)
        self.autoCheck = copy.deepcopy(self.tileSet)
        self.scoreList = self.tileScore(self.library) 
        self.tileNum = 144
        self.emptyBoard()
        self.font = "comicsansms"
        self.gameFont = "Courier"
        self.tileInsert = ["None" for i in xrange (0,self.tileNum)]
        self.randomNumCheck = [i for i in xrange (0,self.tileNum)]
        self.called = [] 
        self.insertCheck = copy.deepcopy(self.randomNumCheck)
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.tileCount = 0

    def initCounts(self):
        #initial information for the counts needed in the game 
        self.count = 0
        self.checkCount = 0 
        self.countClick = 0 
        self.startSecond = 0
        self.noneTile = 0
        self.minute = 0

    def emptyBoard(self):
        #all the empty Board that is needed in the game 
        self.board = []
        self.legalBoard = [] 
        self.selected = []
        self.selected1 = []
        self.noneTiles = []
        self.debugging = [] 

    def initRowCol(self):
        #information neeeded to find the coordinates of the board 
        self.tileRange = 40 
        self.start = 150
        self.imageWidth = 50
        self.imageHeight = 65
        self.tileHeight = 65
        self.tileWidth = 0
        self.firstRow = 12 
        self.fourthRow = 12
        self.secondRow = 8
        self.thirdRow = 10
        self.boardStart = 65
        

    def initData(self):
        #information needed for features of the game 
        self.running = True
        self.click = False
        self.hint = False
        self.gameOver = False
        self.score = False
        self.openingPage = True
        self.playButton = True
        self.numToCheck = None
        self.help = False
        self.win = False
        self.replay = False
        self.levelButton = False
        self.restartGame = True
        self.tileStart = True 

    def initAnimation(self):
        #information need to draw the game
        self.height1 = 30
        self.height2 = 290
        self.drawOffBoard()
        self.drawBoard(self.height1)
        self.drawBoard(self.height2)
        self.drawTopBoard()
        self.button = Button()
        self.game = GameOver()
        self.timer = Timer()
        self.scoreGame = Score()
        self.opening = OpeningPage()
        self.original = copy.deepcopy(self.board)
        self.checkIndex = copy.deepcopy(self.board)
        self.different = DifferentLevel()

    def drawTileBoard(self):
        #place tiles on the given board coordinates 
        while self.drawTile() != True:
            self.drawTile(self.tileCount)  
        
    def storeTileSet(self,library):
        #place all the tile imge needed 
        if self.tileLevel == 1:
            self.initTileSet = list([library.bamboo1.image,
                library.bamboo2.image,library.wind2.image,
                                     library.dragon3.image])*36
        if self.tileLevel == 2:
            self.initTileSet = list([library.bamboo1.image,
            library.character1.image,library.circle2.image,
            library.dragon1.image,library.wind1.image,
            library.season1.image])*24
        if self.tileLevel == 3:
            self.fullTile(library)
        return self.initTileSet

    def fullTile(self,library):
        #full tiles board, 144 tiles 
        self.initTileSet = list([library.bamboo1.image,
                                 library.bamboo2.image,
        library.bamboo3.image,library.bamboo4.image,
        library.bamboo5.image,library.bamboo6.image,
        library.bamboo7.image,library.bamboo8.image,library.bamboo9.image,
        library.character1.image,library.character2.image,
        library.character3.image,library.character4.image,
        library.character5.image,library.character6.image,
        library.character7.image,library.character8.image,
        library.character9.image,library.circle1.image,
        library.circle2.image,library.circle3.image,library.circle4.image,
        library.circle5.image,library.circle6.image,library.circle7.image,
        library.circle8.image,library.circle9.image,library.dragon1.image,
        library.dragon2.image,library.dragon3.image,library.wind1.image,
        library.wind2.image,library.wind3.image,library.wind4.image])*4
        self.initTileSet += list([library.season1.image,
        library.season2.image,library.flower1.image,
                                  library.flower2.image])*2
        

    def tileScore(self,library):
        #place the different score tiles into dictionary
        self.storeScore = {"1":set([library.bamboo1.image,library.bamboo2.image,
        library.bamboo3.image,library.bamboo4.image,
        library.bamboo5.image,library.bamboo6.image,
        library.bamboo7.image,library.bamboo8.image,library.bamboo9.image]),
        "2": set([library.character1.image,library.character2.image,
        library.character3.image,library.character4.image,
        library.character5.image,library.character6.image,
        library.character7.image,library.character8.image,
        library.character9.image]), "3":set([library.circle1.image,
        library.circle2.image,library.circle3.image,library.circle4.image,
        library.circle5.image,library.circle6.image,library.circle7.image,
        library.circle8.image,library.circle9.image]), "4":
                          set([library.dragon1.image,
        library.dragon2.image,library.dragon3.image]), "5":
                          set([library.wind1.image,
        library.wind2.image,library.wind3.image,library.wind4.image]),
        "6":set([library.season1.image,library.season2.image,
            library.season3.image,library.season4.image]), "7":
            set([library.flower1.image,library.flower2.image,
                 library.flower3.image,library.flower4.image])}
        return self.storeScore
    
    def tileChoice(self,numTile):
        #randomly choose the tile from the library 
        tileList = self.tileSet
        self.tileDraw = self.tileSet[numTile]
        return self.tileDraw

    def setBackground(self):
        #image citation: http://wallnoy.com/cool-background-35-
        #16439-wallpapers-4K.html/cool-background-35-2
        #set the background for the game 
        background = pygame.image.load("background.jpg")
        DISPLAYSURF.blit(background,(0,0))
        
    def drawBoard(self,height):
        #list the coordinates need to draw the tiles
        self.boardStart = height 
        rowNum = [self.firstRow,self.secondRow,self.thirdRow,self.fourthRow]
        widthStart = [self.start, self.start + (2*self.tileRange),
                      self.start+self.tileRange,self.start]
        for i in xrange (0,len(rowNum)):
            self.drawRow(rowNum[i],widthStart[i],self.boardStart +
                         (self.tileHeight*(i)))
            self.tileHeight = 65
            self.boardStart = height

    def drawTopBoard(self):
        #list the coordinates needed to draw the top tiles 
        self.layer = 6
        count = 1
        self.highLevel = 38 
        for number in xrange (self.layer,0,-2):
            for col in xrange (0,number):
                colStart = ((self.height1+((self.imageHeight-5)*count))
                            + (self.imageHeight * col))
                for row in xrange (0,number):
                    rowStart = (self.start+
                        ((self.secondRow-(self.layer-count))*self.highLevel) + 
                    ((self.imageWidth-10) * row))
                    self.board += [(rowStart,colStart)]
            count += 1
        colStart -= self.imageHeight/2
        rowStart -= self.imageWidth/2
        self.topTile = (rowStart,colStart)
        self.board += [(rowStart,colStart)]
        
    def drawOffBoard(self):
        #coordinates to draw the three off tiles 
        self.offTile = 3
        for number in xrange (0,self.offTile):
            if number == 0:
                rowStart = self.start - (self.imageWidth-5)
            if number > 0:
                rowStart = (self.start + (self.firstRow* (self.imageWidth-10))
                +((self.imageWidth-10)*(number-1)))
            colStart = self.height/2 - (self.imageHeight/2)
            self.board += [(rowStart,colStart)]

    def drawTile(self,count =0):
        #takes the coordinate from the drawBoard & check if all 144 tiles
        #has been placed in the legal place on the board 
        count = self.count
        #base case for the recursion
        if (count == 144):
            return True
        result = self.checkNotIncluded()
        if result == True:
            self.count += 2
        else:
            self.drawTile(self.count)
        return False 

    def checkNotIncluded(self):
        numToCheck = None  
        #make sure we do not create same image twice
        #and the image we created is not place in an illegal place
        count = 0
        checked = False
        #make a copy of the board
        #choose the place to put the tile 
        result = self.placeRandom()
        if result == True:
            tile1 = random.choice(self.randomNumCheck)
            self.tileInsert[self.numToCheck[0]] = self.tileSet[tile1]
            self.randomNumCheck.remove(tile1)
            tile2 = random.choice(self.randomNumCheck)
            #check to see if we are placing two identical tile at the same time
            for number in xrange (0,self.tileNum):
                while self.tileSet[tile1] != self.tileSet[tile2]:
                    tile2 = random.choice(self.randomNumCheck)
            self.tileInsert[self.numToCheck[1]] = self.tileSet[tile2]
            self.randomNumCheck.remove(tile2)
        else:
            #if it is placed in the legal place, put the list to wehere it was
            #before and run the function again 
            for number in self.tileInsert:
                if number == self.numToCheck[0]:
                    self.tileInsert[number] = "None"
                if number == self.numToCheck[1]:
                    self.tileInsert[number] = "None"
            self.checkNotIncluded()
        return True 
                                       
    def placeRandom(self):
        #randomly chooses places to put the tile
        for number in xrange (0,len(self.checkIndex)):
            if self.checkIndex[number] == self.topTile:
                self.checkIndex[number] = None
        firstPlace = random.choice(self.insertCheck)
        if firstPlace not in self.called:
            self.called += [firstPlace]
            firstNumber =  firstPlace
            self.checkIndex[firstPlace] = None
        else:
            #make sure not to put tile in the place that already hasa tile 
            while firstPlace in self.called:
                firstPlace = random.choice(self.insertCheck)
            self.called += [firstPlace]
            #store the index 
            firstNumber = firstPlace
            self.checkIndex[firstPlace] = None
        secondPlace = random.choice(self.insertCheck)
        #repeat the process again for the second tile 
        if firstPlace not in self.called:
            self.called += [secondPlace]
            secondNumber = secondPlace
            self.checkIndex[secondPlace] = None
        else:
            while secondPlace in self.called:
                secondPlace = random.choice(self.insertCheck)
            self.called += [secondPlace]
            secondNumber = secondPlace
            self.checkIndex[secondPlace] = None
        self.numToCheck = (firstNumber,secondNumber)
        answer = self.overLappingTiles(self.numToCheck,self.tileInsert)
        return answer 
        
        
    def overLappingTiles(self,numToCheck,tileInsert):
        rangeWidth = 20 
        highCount = 0
        #make sure that there is no same tile overlapping each other
        for tile in xrange(0,len(numToCheck)-1):
            if numToCheck[0] != None and numToCheck[1] != None:
                pointA = self.board[numToCheck[tile]][0]
                pointB = self.board[numToCheck[tile]][1]
                #check through the possible range and see if there is an
                #identical tile within that range 
                for tileRow in xrange (pointA - rangeWidth,pointA):
                    for tileCol in xrange (pointB-rangeWidth,pointB):
                        possibleCase = (tileRow,tileCol)
                        if possibleCase in self.checkIndex:
                            if possibleCase == tileInsert[numToCheck[tile]]:
                                highCount += 1
        if highCount > 1:
            return False
        return True

    def drawRow(self,tileRow,tileWidth,tileHeight): 
        #find the coordinates for the tile that will be drawn 
        self.firstRow = tileRow
        self.tileHeight = tileHeight
        for width in xrange (0,self.firstRow):
            self.tileWidth = tileWidth + (self.tileRange*width)
            self.board += [(self.tileWidth,self.tileHeight)]
            #store the coordinates

    def isLegal(self,point):
        #check if the tile selected is legal 
        specialCase = 5
        self.legalBoard = [] 
        count = 0 
        (pointA,pointB) = point
        if self.board[self.tileNum-1] != None:
            if point in self.board[self.tileNum-(specialCase):self.tileNum-1]:
                return False
            else:
                return self.firstCalled(point)
        elif self.board[self.tileNum-1] == None:
            return self.firstCalled(point)

    def firstCalled(self,point):
        #checks if the tile is legal 
        rangeXY = 20 
        (pointA,pointB) = point
        count = 0
        highCount = 0
        for xAxis in xrange (pointA - self.tileRange, pointA+(2*self.tileRange),
                             self.tileRange): 
            self.point = (xAxis,pointB)
            if self.point in self.board:
               count += 1
        #check posssible overlappoing tile, if there is, it is legal 
        for tileRow in xrange (pointA-rangeXY, pointA):
            for tileCol in xrange (pointB-rangeXY,pointB):
                possibleCase = (tileRow,tileCol)
                if possibleCase in self.board:
                    highCount += 1
        if count == 2:
            if highCount == 0:
                return True
        if count == 1:
            #top tile does not need to be check for overlapping 
            if point != self.board[self.tileNum-1]:
                if highCount == 0:
                    return True
            else:
                return True
        return False
    
    def clicked(self,event):
        #click the tile that the user wants 
        self.located = []
        (eventA,eventB) = event
        for tile in xrange (len(self.board)-1,-1,-1):
            if self.board[tile] != None:
                (tileR,tileTop) = (self.board[tile][0],self.board[tile][1])
                (tileL,tileBottom) = (tileR + self.tileRange,
                                      tileTop + self.tileHeight)
                if tileR < eventA < tileL and tileTop < eventB < tileBottom:
                    if self.isLegal(self.board[tile]) == True:
                        #first tile is clicked 
                        self.countClick += 1
                        if self.countClick == 1:
                            self.firstClicked = self.tileInsert[tile]
                            self.firstLocated = self.board[tile]
                            self.selected1 += [self.board[tile]]
                        elif self.countClick == 2:
                            #two tiles clicked
                            self.twoTileClicked(tile)

    def twoTileClicked(self,tile):
        #check to see if the tile clicked are idenitcal 
        if (self.tileInsert[tile] == self.firstClicked
        and self.board[tile] != self.firstLocated):
            #same tile 
            self.selected1 += [self.board[tile]]
            self.hint = False
            self.scoreTile = self.tileInsert[tile]
        else:
            #not the same tile
            self.selected1 = []
            self.selected1 += [self.board[tile]]
            self.countClick = 1
            self.firstLocated = self.board[tile]
            self.firstClicked = self.tileInsert[tile]
        

    def tileClicked(self,event):
        #check if the indicated tile has been clicked 
        (clickA,clickB) = event
        tileRight = self.button.drawWidth
        tileTop = self.button.drawHeight
        tileLeft = tileRight + self.button.buttonWidth
        tileBottom = tileTop + self.button.buttonHeight
        menuRight = self.button.drawWidth
        menuTop = tileTop - self.button.buttonHeight*2
        menuLeft = menuRight + self.button.buttonWidth
        menuBottom = menuTop + self.button.buttonHeight
        pauseTop = menuTop - self.button.buttonHeight *2
        pauseBottom = pauseTop + self.button.buttonHeight
        reTop = pauseTop - self.button.buttonHeight * 2
        reBottom = reTop + self.button.buttonHeight
        #check to see if the place we clicked is within the button range 
        if (tileRight < clickA < tileLeft) and (tileTop < clickB < tileBottom):
            return "hint"
        if (menuRight < clickA < menuLeft) and (menuTop < clickB < menuBottom):
            return "menu"
        if ((menuRight < clickA <menuLeft) and
                            (pauseTop < clickB < pauseBottom)):
            return "pause"
        if (menuRight < clickA <menuLeft) and (reTop < clickB < reBottom):
            return "restart" 
            
                   
    def run(self):
        #run the animation
        self.initAnimation()
        while self.running:
            if self.replay != True: self.drawTileBoard()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    #when the button is clicked
                    self.checkGameOver()
                    self.clicked(event.pos)
                    self.click = True
                    if self.playButton != False:
                        self.openingPageMaterial(event.pos)
                    else:
                        self.playButtonsTile(event.pos)
                        if self.winButton(event.pos) == "replay":
                            self.replay = True
                        self.twoLegalTile()
                        if self.gameOver == True: self.gameIsOver(event.pos)
                    for tiles in xrange (0,len(self.board)):
                        if self.board[tiles] == None:
                            if tiles not in self.noneTiles:
                                self.noneTiles += [tiles]
                                self.noneTile += 1
                    if self.noneTile == self.tileNum: self.win = True
            if self.replay == True: self.redrawInit() 
            self.redrawAll()
            pygame.display.update()

    def gameIsOver(self,event):
        #game is Over 
        self.restartGame = True
        if self.game.clickButtons(event) == "redraw":
            self.redrawInit()
            self.gameOver != True
        if self.game.clickButtons(event) == "shuffle":
            self.gameShuffle()  
        

    def twoLegalTile(self):
        #two correct tile is clicked
        if len(self.selected1)== 2:
            self.score = True
            for row in xrange (len(self.board)):
                #remove the tiles from the board 
                if self.board[row] == self.selected1[0]:
                    self.board[row] = None
                    self.tileInsert[row] = None
                if self.board[row] == self.selected1[1]:
                    self.board[row] = None
                    self.tileInsert[row] = None 
            self.countClick = 0
            self.selected1 = []
        

    def openingPageMaterial(self,event):
        #different buttons located in the opening page is clicked 
        if self.opening.choiceClicked(event) == "start":
            #show the level page 
            self.levelButton = True
        if self.levelButton == True:
            if self.different.clickLevel(event) == "Easy":
                self.tileLevel = 1
                self.minute = 5 
                self.redrawInit()
                self.playButton = False
            if self.different.clickLevel(event) == "Medium":
                self.tileLevel = 2
                self.minute = 4
                self.redrawInit()
                self.playButton = False
            if self.different.clickLevel(event) == "hard":
                self.tileLevel = 3
                self.minute = 3
                self.redrawInit()
                self.playButton = False 
        if self.opening.choiceClicked(event) == "help":
            self.help = True
        if self.opening.clickHelpPage(event) == "menu":
            #return back to the menu 
            self.help = False
            self.replay = True

    def playButtonsTile(self,event):
        #the different button located in the game screen is clicked
        if self.tileClicked(event) == "hint":
            self.hintFunction()
            if len(self.finalList) == 0:
                self.gameOver = True
        if self.tileClicked(event) == "pause":
            if self.tileStart == True:
                self.tileStart = False
            else:
                self.tileStart = True
        if self.tileClicked(event) == "restart":
            self.replay = True
        if (self.tileClicked(event) ==
        "menu" or self.winButton(event)== "menu"):
            self.redrawInit()
            self.levelButton = False 
            self.playButton = True
            self.help != True 

    def checkGameOver(self):
        #check if there is any legal tiles left in the board 
        self.hintList = []
        self.finalList = []
        self.hintIndex = []
        self.possibleSame = []
        count = 0
        #go through the tile to find legal tiles 
        for row in xrange (0,len(self.board)):
            if self.original[row]!= None:
                if self.isLegal(self.original[row]) == True:
                    self.hintList += [self.tileInsert[row]]
                    self.hintIndex += [self.board[row]]
        #check if legal tiles has a pair 
        for legal in xrange (len(self.hintList)):
            for tileNum in xrange (0,len(self.hintList)):
                if tileNum != legal:
                    if count < 1:
                        if self.hintList[legal] != None: 
                           if self.hintList[legal] == self.hintList[tileNum]:
                                count += 1 
                                self.finalList += [self.hintIndex[legal]]
                                self.finalList += [self.hintIndex[tileNum]]
        if len(self.finalList) == 0:
            #if no pair is found, game is over 
            self.gameOver = True 
        else:
            self.gameOvER = False  

    def gameShuffle(self):
        #shuffles the board if there is no legal tile left on the board
        #and the game is not yet ended 
        count = 0 
        tileShuffle = []
        indexShuffle = []
        self.restartGame = False
        self.gameOver = False 
        for tile in xrange (0,len(self.tileInsert)):
            if self.tileInsert[tile] != None:
                tileShuffle += [tile]
                indexShuffle += [tile]
        while count <= len(tileShuffle):
        #stores all the tiles that is left on the board 
            newTile = random.choice(tileShuffle)
            newPlace = random.choice(indexShuffle)
            (self.tileInsert[newTile],
              self.tileInsert[newPlace]) = (self.tileInsert[newPlace],
                                            self.tileInsert[newTile])
            count += 1               

    def redrawInit(self):
        #initial information needed to redraw the game board 
        self.tileNum = 144
        self.scoreCount = 0
        self.tileInsert = ["None" for i in xrange (0,self.tileNum)]
        self.board = copy.deepcopy(self.original)
        self.checkIndex = copy.deepcopy(self.board)
        self.randomNumCheck = [i for i in xrange (0,self.tileNum)]
        self.insertCheck = copy.deepcopy(self.randomNumCheck)
        self.called = [] 
        self.count = 0
        self.noneTile = 0
        self.second = 59
        self.milli = 10
        self.noneTiles = []
        self.located = []
        self.tileSet = self.storeTileSet(self.library)
        self.drawTileBoard()
        self.timer = Timer()
        self.timer.timerIncrease(self.minute)
        self.scoreGame = Score()
        self.replay = False
        self.win = False 
        self.playButton = True
        self.restartGame = False
        self.tileStart = True

    def hintFunction(self):
        #finds coordinates of the possible two tile 
        self.hintList = []
        self.finalList = []
        self.hintIndex = []
        self.possibleSame = []
        count = 0
        #repeat process of checkGame Over 
        for row in xrange (0,len(self.board)):
            if self.original[row]!= None:
                if self.isLegal(self.original[row]) == True:
                    self.hintList += [self.tileInsert[row]]
                    self.hintIndex += [self.board[row]]
        for legal in xrange (len(self.hintList)):
            for tileNum in xrange (0,len(self.hintList)):
                if tileNum != legal:
                    if count < 1:
                        if self.hintList[legal] != None:
                            #give the two pair from the number of paris found 
                           if self.hintList[legal] == self.hintList[tileNum]:
                                count += 1 
                                self.finalList += [self.hintIndex[legal]]
                                self.finalList += [self.hintIndex[tileNum]]
        self.hint = True 
        return self.finalList

    def redrawAll(self):
        #redraws the game 
        self.screen.fill((0,0,0))
        self.setBackground()
        if self.playButton != False:
            self.opening = OpeningPage()
            self.opening.drawTitle(self.width,self.height)
            self.opening.drawPlayButton(self.width,self.height)
            if self.help == True:
                self.opening.drawHelpPage(self.width,self.height)
            if self.levelButton == True:
                self.different.drawLevel(self.width,self.height)
        #draw the tile that was stored beforehand
        else:
            for tileDraw in xrange (0,len(self.board)):
                tile = self.tileInsert[tileDraw]
                if tile != None:
                    tile = pygame.transform.scale(tile,(50,70))
                    self.screen.blit(tile,self.board[tileDraw])
            if self.click == True:
                for draw in xrange (0,len(self.selected1)):
                    if len(self.selected1) > 0:
                        s =pygame.Surface((self.imageWidth-10,self.imageHeight))
                        s.set_alpha(128)
                        s.fill((255,255,255))
                        self.screen.blit(s,self.selected1[draw])
            if self.win == True: self.winGame()
            self.drawInformation()

    def winGame(self):
        #Image Credit: Podium by Andrew J. Young from The Noun Project 
        #draws the win Image when game is won 
        fontS = 10 
        ratio = 1.5
        win = pygame.image.load("icon_3834.png")
        win = pygame.transform.scale(win,(self.width/2,self.height/2))
        self.screen.blit(win,(self.width/4,self.height/4))
        textFont = pygame.font.SysFont(self.font,fontS*(ratio*2))
        text1 = textFont.render("REPLAY",1,self.white)
        self.screen.blit(text1,(self.width/4 + (fontS*2),self.height/ratio))
        text2 = textFont.render("MENU",1,self.white)
        self.screen.blit(text2,(self.width/ratio -(fontS*2),self.height/ratio))

    def winButton(self,event):
        #go back to what button indicated if the button is clicked 
        (clickA,clickB) = event 
        ratio = 1.5
        boxRatio = 6 
        replayRight = self.width/4 + 20
        replayTop = self.height/ratio
        replayLeft = replayRight + self.width/boxRatio
        replayBottom = replayTop + self.height/boxRatio
        menuRight = self.width/ratio - 20
        menuTop = self.height/ratio
        menuLeft = menuRight + self.width/boxRatio
        menuBottom = menuTop + self.height/boxRatio
        if self.win != False:
            if (menuRight < clickA < menuLeft) and (menuTop < clickB <
                menuBottom):
                return "menu"
            if ((replayRight < clickA <replayLeft) and
                        (replayTop < clickB < replayBottom)):
                return "replay"       
        
    def drawInformation(self):
        #draw addional information needed for the game 
        self.button.drawButton(self.width,self.height)
        if self.hint == True:
            #draw the hint tile
            for drawHint in xrange (0,len(self.finalList)):
                hint = self.finalList[drawHint]
                if hint != None:
                    hintTile = pygame.Surface((self.imageWidth-5,
                                               self.imageHeight))
                    hintTile.set_alpha(128)
                    hintTile.fill((255,218,185))
                    DISPLAYSURF.blit(hintTile,self.finalList[drawHint])
        if self.restartGame == True:
            #draw the game Over Sign 
            self.game.drawGameButton(self.width,self.height)
        #draw timer with second increases
        if self.tileStart == True:
            self.timer.timerIncrease(self.minute)
        self.timer.drawTimer(self.width,self.height)         
        #draw Score
        if self.score == True:
            self.scoreGame.findScore(self.scoreTile)
            self.scoreGame.drawScore(self.width,self.height)
            self.score = False
        self.scoreGame.drawScore(self.width,self.height)

class Win(MahjongSolitare):
    #win Image 
    def __init__(self):
        #initial information to draw Win Image 
        super(Win,self).__init__()
        self.fontSize = 15

    def drawImage(self,width,height):
        #Image credit: Podium by Andrew J. Young from The Noun Project 
        #draws the Win Image 
        win = pygame.image.load("icon_3834.png")
        win = pygame.transform.scale(win,(width/2,height/2))
        self.screen.blit(win,(width/4,height/4))
        textFont = pygame.font.SysFont(self.font,15)
        text1 = textFont.render("REPLAY",1,self.white)
        self.screen.blit(text1,(width/4,height/2))
        
class Button(MahjongSolitare):
    #draws the Button for the game 
    def __init__(self):
        #initial information needed to draw Button       
       super(Button,self).__init__()
       self.buttonWidth = 70
       self.buttonHeight = 40
       self.drawWidth = self.width - (self.buttonWidth*1.5)
       self.drawHeight = self.height - (self.buttonHeight *2)
       self.margin = 5 
       self.black = (0,0,0)
       self.white = (255,255,255)
       self.buttonFont = self.font
       self.fontSize = 24 

    def drawButton(self,width,height):
        #draw the button on to the board
        numOfbutton = 4
        ratio = 10 
        for height2 in xrange (0,numOfbutton):
            whiteRight = self.drawWidth - ratio
            whiteTop = self.drawHeight - height2*(self.buttonHeight*2)
            whiteLeft = self.buttonWidth + ratio
            whiteBottom = self.buttonHeight + self.margin
            pygame.draw.rect(self.screen,self.white,(whiteRight,
                whiteTop,whiteLeft,whiteBottom))
        for height in xrange (0,numOfbutton):
            rectRight = self.drawWidth + self.margin/2 - ratio
            rectLeft = self.buttonWidth - self.margin + ratio
            rectTop = (self.drawHeight - height*(self.buttonHeight*2) +
            self.margin/2)
            rectBottom = self.buttonHeight
            pygame.draw.rect(self.screen,self.black,(rectRight,
            rectTop,rectLeft,rectBottom))
        self.drawInformation(width,height)

    def drawInformation(self,width,height):
        #draw the button itself onto the game screen 
        ratio = 10 
        buttonFont = pygame.font.SysFont(self.buttonFont,self.fontSize)
        text = buttonFont.render("HINT",1,self.white)
        self.screen.blit(text,(self.drawWidth+self.margin/2 -ratio/2,
                        self.drawHeight+self.margin/2))
        menuFont = pygame.font.SysFont(self.buttonFont,self.fontSize)
        text2 = menuFont.render("MENU",1,self.white)
        self.screen.blit(text2,(self.drawWidth + self.margin/2-ratio,
                self.drawHeight - self.buttonHeight*2 + self.margin/2))
        stopFont = pygame.font.SysFont(self.buttonFont,self.fontSize-ratio/2)
        text3 = stopFont.render("PAUSE",1,self.white)
        self.screen.blit(text3,(self.drawWidth + self.margin/2 -ratio/2,
                self.drawHeight - 2*(self.buttonHeight*2) + self.margin/2))
        reFont = pygame.font.SysFont(self.buttonFont,self.fontSize-(ratio-2))
        text4 = reFont.render("RESTART",1,self.white)
        self.screen.blit(text4,(self.drawWidth + self.margin/2-ratio,
                self.drawHeight - 3 *(self.buttonHeight*2) + self.margin/2))
        

class GameOver(MahjongSolitare):
    #draw GameOver Sign 
    def __init__(self):
        #initial information needed to display game over
        super(GameOver,self).__init__()
        self.gameX = self.width/4
        self.gameY = self.height/3
        self.gameWidth = self.width/2 
        self.gameHeight = self.height/4
        self.buttonWidth =150
        self.smallButtonX = self.gameWidth/8
        self.smallButtonY = self.gameY + self.gameHeight/2
        self.buttonHeight = 40 
        self.black = (0,0,0)
        self.buttonFont = self.gameFont
        
    def drawGameButton(self,width,height):
        #draw the Game Button onto the game
        pygame.draw.rect(self.screen,self.black,(self.gameX,self.gameY,
                    self.gameWidth,self.gameHeight))
        pygame.draw.rect(self.screen,self.white,(self.gameX +
                                                 self.smallButtonX,
                    self.smallButtonY,2*self.smallButtonX,self.buttonHeight))
        pygame.draw.rect(self.screen,self.white,(self.gameX +
                                                 5*self.smallButtonX,
                    self.smallButtonY,2*self.smallButtonX,self.buttonHeight))
        buttonFontAgain = pygame.font.SysFont(self.buttonFont,20)
        textAgain = buttonFontAgain.render("PLAY AGAIN?",1,self.black)
        self.screen.blit(textAgain,(self.gameX+self.smallButtonX,
                                    self.smallButtonY))
        shuffle = buttonFontAgain.render("SHUFFLE",1,self.black)
        self.screen.blit(shuffle,(self.gameX+5*self.smallButtonX + 5,
                                  self.smallButtonY))
        buttonFont = pygame.font.SysFont(self.buttonFont,80)
        text = buttonFont.render("GAMEOVER",1,self.white)
        self.screen.blit(text,(self.gameX + 10,self.gameY))

    def clickButtons(self,event):
        #clicks the button if the mouse is clikced on the button
        (clickA,clickB) = event
        reRight = self.gameX + self.smallButtonX
        reLeft = reRight + 2 * self.smallButtonX
        reTop = self.smallButtonY
        reBottom = reTop + self.buttonHeight
        shuffleRight = self.gameX + 5*self.smallButtonX
        shuffleLeft = shuffleRight + 2 * self.smallButtonX
        if (reRight < clickA <reLeft) and (reTop < clickB < reBottom):
            return "redraw"
        if (shuffleRight < clickA <shuffleLeft) and (reTop < clickB < reBottom):
            return "shuffle"
    
class Score(MahjongSolitare):
    #draw Score sign 
    def __init__(self):
        #initial ifnormation needed for the score class 
        super(Score,self).__init__()
        self.scorePoint = 0
        self.scoreX = self.width/1.38 #estimated good amount 
        self.scoreY = 100
        self.scoreFont = self.font
        self.yellow = (255,165,0)
        self.count = 0 

    def findScore(self,scoreTile):
        #find the Score for the game
        for scores in self.scoreList:
            for tile in self.scoreList[scores]:
                #print scoreTile, tile 
                if str(tile) == str(scoreTile):
                    if self.count < 1:
                        self.count += 1 
                        self.scorePoint += 1
        self.count = 0

    def drawScore(self,width,height):
        #draw score board onto the game 
        scoreFont = pygame.font.SysFont(self.scoreFont,40)
        scoreText = scoreFont.render("SCORE: " + str(self.scorePoint),1,
                                     self.yellow)
        self.screen.blit(scoreText,(self.width/1.38,self.score))

class Timer(MahjongSolitare):
    #d for the game 
    def __init__(self):
        #inital information needed for timer class 
        super(Timer,self).__init__()
        self.TimerX = self.width/1.38 #estimated good amount 
        self.TimerY = 50
        self.second = 59
##        self.minute = 1
        self.milli = 10
        self.timerFont = self.font
        self.yellow = (255,165,0)


    def timerIncrease(self,minute):
        #increases the time in minutes & seconds
        self.minute = minute
        tempSecond = 0
        tempMilli = 0
        tempMinute = 0 
        if self.tileStart == True:
            if self.minute > 0:
                self.milli -= 1
                if self.milli == 0:
                    self.second -= 1
                    tempSecond = self.second
                    self.milli = 10 
                if self.second == 0:
                    self.minute -= 1
                    tempMinunte = self.minute
                    if self.minute == 0:
                        self.second = 0
                    else:
                        self.second  = 60
            else:
                self.minute = minute
                self.second = tempSecond 
                self.GameOver = True

    def drawTimer(self,width,height):
        #draw timer board onto the game 
        timerFont = pygame.font.SysFont(self.timerFont,40)
        timerText = timerFont.render("TIMER " + str(self.minute)+ ":" +
                                     str(self.second),1,self.yellow)
        self.screen.blit(timerText,(self.width/1.38,50))


class OpeningPage(MahjongSolitare):
    #draw the Opening Page for the game 
    def __init__(self):
        #initial information needed to draw the opening page 
        super(OpeningPage,self).__init__()
        self.titleX = self.width/2
        self.titleY = self.height/2
        self.startButtonX = self.width/2 - self.width/4
        self.startButtonY = self.height/2 
        self.InstructionButton = self.width/2 - (self.titleX)/2
        self.imageX = self.width/10
        self.imageY = self.height/10
        self.titleFont = "LiquidCrystal"
        self.helpX = self.width/6
        self.helpY = self.height/6
        self.helpWidth = self.width/2
        self.helpHeight = self.height/2
        self.instruction = [
            "Mahjong Solitaire is a matching game that uses sets of mahjong",
            "tiles instead of using cards. There is 144 tiles arranged in",
            "speical pattern. A tile is said to be 'open' if it can be moved",
            "either right or left without disturbing other tiles",
            "The goal of this game is to match open pairs of identical tiles",
            "and remove them from the board.",
            "The game can be ended if you remove all the tiles from the board",
            "or there is no open tiles available for you to remove.",
            "ENJOY THE GAME!!!"]

    def drawTitle(self,width,height):
        #draw the title for the game
        #Citation: http://www.imagebrowse.com/cool-backgrounds-wallpapers/
        openingBackground = pygame.image.load("start.jpg")
        openingBackground = pygame.transform.scale(openingBackground,
                                                   (self.width,self.height))
        self.screen.blit(openingBackground,(0,0))
        titleFont = pygame.font.SysFont(self.titleFont,50)
        titleText = titleFont.render("MAHJONG SOLITARE",1,self.black)
        self.screen.blit(titleText,(self.width/2,self.height/3))

    def drawHelpPage(self,width,height):
        #draws the help page with the instructions 
        ratio = 3
        self.blue = (32,178,170)
        pygame.draw.rect(self.screen,self.black,(self.helpX,self.helpY,
                    self.helpX + self.helpWidth,self.helpY + self.helpHeight))
        hintFont = pygame.font.SysFont(self.titleFont,50)
        hintText = hintFont.render("INSTRUCTIONS",1,self.white)
        self.screen.blit(hintText,(self.width/3 + 20,self.height/6 + 10))
        instructionFont = pygame.font.SysFont(self.titleFont,25)
        for text in xrange (0,len(self.instruction)):
            instructionText = instructionFont.render(self.instruction[text],1,
                                                     self.white)
            self.screen.blit(instructionText,(self.width/5,
                                              self.height/6 + 20*(text+3)))
        startFont = pygame.font.SysFont(self.titleFont,50)
        startText = startFont.render("MENU",1,self.white)
        pygame.draw.rect(self.screen,self.blue,(self.helpX+20,
                        self.helpY + self.helpHeight +10,self.helpX/1.5,
                                                self.helpY/2))
        self.screen.blit(startText,(self.helpX + 20,
                                    self.helpY + self.helpHeight + 20))

    def clickHelpPage(self,event):
        #go back to the menu from the help Page 
        (clickA,clickB) = event
        helpRight = self.helpX + 20 
        helpTop = self.helpY + self.helpHeight + 10 
        helpBottom = helpTop + self.helpY/2
        helpLeft = helpRight + self.helpX/1.5
        if (helpRight < clickA < helpLeft) and (helpTop < clickB <
                helpBottom):
            return "menu"
        
    def drawPlayButton(self,width,height):
        #image credit: Power by Jardson A. from The Noun Project
        ratio = 3
        font = 50 
        start = pygame.image.load("icon_17738.png")
        start = pygame.transform.scale(start,(self.width/10,self.height/10))
        startFont = pygame.font.SysFont(self.titleFont,font)
        startText = startFont.render("START",1,self.black)
        self.screen.blit(startText,(self.startButtonX + self.imageX,
                                    self.startButtonY+self.imageY/3))
        self.screen.blit(start,(self.startButtonX,self.startButtonY))
        helpFont = pygame.font.SysFont(self.titleFont,font)
        helpText = helpFont.render("HELP",1,self.black)
        self.screen.blit(helpText,(self.startButtonX + self.imageX,
                self.startButtonY + ratio/2*(self.imageY)+ self.imageY/ratio))
        helpButton = pygame.image.load("icon_61692.png")
        helpButton = pygame.transform.scale(helpButton,
                                            (self.imageX,self.imageY))
        self.screen.blit(helpButton,(self.startButtonX,
                                     self.startButtonY+ratio/2*(self.imageY)))

    def choiceClicked(self,event):
        #click on the tile that is shown on the opening page 
        (clickA,clickB) = event 
        ratio = 3 
        buttonRight = self.startButtonX 
        buttonTop = self.startButtonY 
        buttonLeft = buttonRight + self.imageX
        buttonBottom = buttonTop + self.imageY
        hintRight = self.startButtonX 
        hintTop = self.startButtonY + ratio/2*(self.imageY)
        hintLeft = hintRight + self.imageX
        hintBottom = hintTop + self.imageY
        if (buttonRight < clickA < buttonLeft) and (buttonTop < clickB <
                buttonBottom):
            return "start"
        if (hintRight < clickA <hintLeft) and (hintTop < clickB < hintBottom):
            return "help"
        
class DifferentLevel(MahjongSolitare):
    def __init__(self):
        #initial information to draw the different levels 
        super(DifferentLevel,self).__init__()
        self.boxWidth = self.width/5
        self.boxHeight = self.height/3
        self.boxStart = self.width/5
        self.margin = self.width/8
        self.font =  "comicsansms"

    def drawLevel(self,width,height):
        #image citation: http://www.imagebrowse.com/cool-backgrounds-wallpapers/
        #image citation: Paul F. from The Noun Project 
        openingBackground = pygame.image.load("start.jpg")
        openingBackground = pygame.transform.scale(openingBackground,
                                                   (self.width,self.height))
        self.screen.blit(openingBackground,(0,0))
        levelImage = ["icon_11332.png","icon_11334.png","icon_11333.png"]
        levelTitle = ["  Easy","Medium","  Hard"]
        for box in xrange (0,3):
            self.Right = self.margin/2 + (self.boxStart + self.margin) * box 
            self.Top = self.boxHeight
            self.bottom = self.boxHeight
            self.Left = self.boxWidth
            levels = pygame.image.load(levelImage[box])
            levels = pygame.transform.scale(levels,
                                            (self.boxWidth,self.boxHeight))
            self.screen.blit(levels,(self.Right,self.Top))
            levelFont = pygame.font.SysFont(self.font,50)
            levelText = levelFont.render(levelTitle[box],1,self.black)
            self.screen.blit(levelText,(self.Right,self.Top + self.bottom + 20))

    def clickLevel(self,event):
        #indicate that the different level has been chosen 
        (clickA,clickB) = event
        self.EasyRight = self.margin/2 + (self.boxStart + self.margin)*0
        self.EasyLeft = self.EasyRight + self.boxWidth
        self.MediumRight = self.margin/2 + (self.boxStart + self.margin) * 1
        self.MediumLeft = self.MediumRight + self.boxWidth
        self.hardRight = self.margin/2 + (self.boxStart + self.margin)*2
        self.hardLeft = self.hardRight + self.boxWidth
        self.Top = self.boxHeight
        self.bottom = self.Top + self.boxWidth
        if ((self.EasyRight < clickA < self.EasyLeft) and
                        (self.Top <clickB <self.bottom)):
            return "Easy"
        if ((self.MediumRight < clickA < self.MediumLeft) and
                    (self.Top < clickB < self.bottom)):
            return "Medium"
        if ((self.hardRight < clickA < self.hardLeft) and
                    (self.Top < clickB < self.bottom)):
            return "hard"

        
if __name__ == '__main__':
    mahjongSolitaire = MahjongSolitare()
    mahjongSolitaire.run()

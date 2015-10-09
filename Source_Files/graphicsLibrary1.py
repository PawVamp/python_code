#GRAPHICS LIBRARY
#received advise from Lucy Tai
#Mahjong Tile image citation: http://www.ultimate-mahjong.com/images/points.jpg

import pygame,sys

class graphicsLibrary(object):
    def __init__(self):
        self.initBamboo()
        self.initSeasons()
        self.initDragon()
        self.initWind()
        self.initCircle()
        self.initCharacter()
        self.initFlower()

    def initBamboo(self):
        self.bamboo1 = point1(1)
        self.bamboo2 = point1(2)
        self.bamboo3 = point1(3)
        self.bamboo4 = point1(4)
        self.bamboo5 = point1(5)
        self.bamboo6 = point1(6)
        self.bamboo7 = point1(7)
        self.bamboo8 = point1(8)
        self.bamboo9 = point1(9)

    def initCharacter(self):
        self.character1 = point2(1)
        self.character2 = point2(2)
        self.character3 = point2(3)
        self.character4 = point2(4)
        self.character5 = point2(5)
        self.character6 = point2(6)
        self.character7 = point2(7)
        self.character8 = point2(8)
        self.character9 = point2(9)

    def initCircle(self):
        self.circle1 = point3(1)
        self.circle2 = point3(2)
        self.circle3 = point3(3)
        self.circle4 = point3(4)
        self.circle5 = point3(5)
        self.circle6 = point3(6)
        self.circle7 = point3(7)
        self.circle8 = point3(8)
        self.circle9 = point3(9)

    def initDragon(self):
        self.dragon1 = point4(1)
        self.dragon2 = point4(2)
        self.dragon3 = point4(3)

    def initWind(self):
        self.wind1 = point5(1)
        self.wind2 = point5(2)
        self.wind3 = point5(3)
        self.wind4 = point5(4)

    def initSeasons(self):
        self.season1 = point7(1)
        self.season2 = point7(2)
        self.season3 = point7(3)
        self.season4 = point7(4)

    def initFlower(self):
        self.flower1 = point6(1)
        self.flower2 = point6(2)
        self.flower3 = point6(3)
        self.flower4 = point6(4)
    

class tiles(object):
    def __init__(self):
        self.basicPath="./Week 1/graphics/"

class point6(tiles):
    def __init__(self,number):
        super(point6,self).__init__()
        self.basicPath += "6/points 6-" + str(number) +".jpg"
        self.image = pygame.image.load(self.basicPath)

class point5(tiles):
    def __init__(self,number):
        super(point5,self).__init__()
        self.basicPath += "5/points 5-" + str(number) + ".jpg"
        self.image = pygame.image.load(self.basicPath)

class point4(tiles):
    def __init__(self,number):
        super(point4,self).__init__()
        self.basicPath += "4/points 4-" + str(number) + ".jpg"
        self.image = pygame.image.load(self.basicPath)

class point3(tiles):
    def __init__(self,number):
        super(point3,self).__init__()
        self.basicPath += "3/points 3-" + str(number) + ".jpg"
        self.image = pygame.image.load(self.basicPath)

class point2(tiles):
    def __init__(self,number):
        super(point2,self).__init__()
        self.basicPath += "2/points 2-" + str(number) + ".jpg"
        self.image = pygame.image.load(self.basicPath)
        
class point1(tiles):
    def __init__(self,number):
        super(point1,self).__init__()
        self.basicPath += "1/points 1-" + str(number) + ".jpg"
        self.image = pygame.image.load(self.basicPath)

class point7(tiles):
    def __init__(self,number):
        super(point7,self).__init__()
        self.basicPath += "7/points 7-" + str(number) +".jpg"
        self.image = pygame.image.load(self.basicPath)

d = graphicsLibrary()

       
    

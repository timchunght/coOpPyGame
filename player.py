import pygame

class Player():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.up = False
        self.down = False

    def setImg(self, image):
        self.image = pygame.image.load(image)

    def setSize(self, width, height):
        self.blockSize = pygame.transform.scale(self.image, (width, height))

    def setShape(self, x, y, width, height):
        self.blockShape = pygame.Rect(x, y, width, height)

class Obstacle():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moving = False

    def setImg(self, image):
        self.image = pygame.image.load(image)

    def setSize(self, width, height):
        self.blockSize = pygame.transform.scale(self.image, (width, height))

    def setShape(self, x, y, width, height):
        self.x = x
        self.y = y
        self.blockShape = pygame.Rect(x, y, width, height)



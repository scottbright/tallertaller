import pygame
from pygame.locals import *

class Ball(object):

    def __init__(self, radius, color, pos):
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color
        self.sel = 1

    def render(self, surface):
        pos = (self.sel*int(self.x),int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

    def change(self, newsel):
    	self.sel = newsel

#########################################
class Bar(object):


    def __init__(self, color,pos):
        self.width = 5 # should be 5
        self.color = color
        self.heigh = 150
        self.level = 1
        self.pos = pos

    def update(self):
    	if self.width > 5:
    		self.width -= 0.02+(0.01*self.level)
    	if self.width < 5:
    		self.width = 5
        if self.width > 350:
            self.width = 350

    def spacebar(self):
        self.width += 10

    def render(self, surface):
        pygame.draw.rect(surface,
                         self.color,
                         pygame.Rect(self.pos,470-self.width,self.heigh,self.width),0)
    def checkWidth(self):
        return self.width

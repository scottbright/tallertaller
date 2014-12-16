import pygame
from pygame.locals import *
import gamelib
from elements import *
from MySound import MySound

class SpaceGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(SpaceGame, self).__init__('Space', SpaceGame.BLACK)
        self.themeSound = MySound("unity.ogg")
        self.themeSound.play()
        self.select = 1
        self.level = 1
        self.button = 0
        self.score = 1000
        self.totalscore = 0
        self.time = 45
        self.ball = Ball(radius=10,
                         color=SpaceGame.WHITE,
                         pos=(200,
                              500))
        self.bar1 = Bar((200,200,0),pos=125)
        self.bar2 = Bar((0,200,200),pos=325)
        self.bar3 = Bar((200,0,200),pos=525)

    def init(self):
        super(SpaceGame, self).init()
        self.render_level()

    def update(self):
        if self.is_key_pressed(K_RIGHT):
            self.button+=1
            if(self.select<3 and self.button == 1):
                self.select+=1
                self.ball.change(self.select)
        elif self.is_key_pressed(K_LEFT):
            self.button+=1
            if(self.select>1 and self.button == 1):
                self.select-=1
                self.ball.change(self.select)
        elif self.is_key_pressed(K_SPACE):
            self.button += 1
            if self.select == 1 and self.button == 1:
                self.bar1.spacebar()
            if self.select == 2 and self.button == 1:
                self.bar2.spacebar()
            if self.select == 3 and self.button == 1:
                self.bar3.spacebar()
        elif self.is_key_pressed(K_g):
            if self.select == 1:
                self.bar1.spacebar()
            if self.select == 2:
                self.bar2.spacebar()
            if self.select == 3:
                self.bar3.spacebar()
        else:
            self.button = 0
        self.render_level()
        self.bar1.update()
        self.bar2.update()
        self.bar3.update()
        self.check_level()
          
    def check_level(self):
        if self.bar1.width > 320 and self.bar2.width > 320 and self.bar3.width > 320 :
            self.changeL()
            self.resetW()

    def changeL(self):
        self.level += 1
        self.bar1.level += 1
        self.bar2.level += 2
        self.bar3.level += 3

    def resetW(self):
        self.bar1.width = 5
        self.bar2.width = 5
        self.bar3.width = 5 
            
    def render_level(self):
        self.level_image = self.font.render("Level = %d" % self.level, 0, SpaceGame.WHITE)

    def render(self, surface):
        self.ball.render(surface)
        self.bar1.render(surface)
        self.bar2.render(surface)
        self.bar3.render(surface)
        surface.blit(self.level_image, (15,15))

def main():
    game = SpaceGame()
    game.run()

if __name__ == '__main__':
    main()

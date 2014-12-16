import pygame
from pygame.locals import *


class MySound():

	def __init__(self,path):
		pygame.init()
		self.sound = pygame.mixer.Sound(path)
		self.soundPlay = False

	def setVolume(self,volume):
		self.sound.set_volume(volume)

	def play(self):
		self.sound.play()
		self.soundPlay = True

	def loop(self):
		self.sound.play(-1)
		self.soundPlay = True

	def stop(self):
		self.sound.stop()
		self.soundPlay = False

	def isPlay(self):
		if self.soundPlay == True:
			return True
		else:
			return False
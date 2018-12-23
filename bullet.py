import pygame
import random

from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ship,bucket,score):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('ball1.bmp')
        if score%10 == random.randint(0,9):
            self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
    #    print(self.rect)
        self.screen_rect = screen.get_rect()
        self.rect.centerx = ship.topCenterx
        self.rect.bottom = ship.top+self.rect[3]
        self.downBucket = bucket.rect.bottom
     #   print(self.rect.bottom)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.rect.bottom +=1
        if self.rect.bottom > self.screen_rect.bottom+self.rect[3]:
            return True


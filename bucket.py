import pygame
import random

class Bucket():
    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load('bucket.bmp')
        self.rect = self.image.get_rect()
    #    print(self.rect)
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.bullet = False
        self.add = False
        self.t = 0

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self,ai_settings):

     #   if self.moving_left == False and self.moving_right == False:
     #       if self.t == 50:
     #           self.t = random.randint(0,100)
     #       if self.t>=50:
     #           self.moving_left = True
     #           self.t -= 1
     #       else:
     #           self.moving_right = True
     #           self.t += 1
     #       print(self.t)
        if self.moving_right and self.rect.centerx<self.screen_rect.centerx*2 - self.rect[2]/2 :
            self.rect.centerx += ai_settings.bucket_right
         #   print('right',self.t)
        elif self.moving_left and self.rect.centerx > self.rect[2]/2:
            self.rect.centerx -= ai_settings.bucket_left
         #   if self.moving_up and self.rect.bottom>self.rect[3]:
         #      self.rect.bottom -= 1
         #  elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
         #      self.rect.bottom += 1
         # if self.love :
         #   self.image = pygame.image.load('2.bmp')
         # else:
         #  self.image = pygame.image.load('plane1.bmp')

         # self.top = self.rect.bottom
         # self.topCenterx = self.rect.centerx

import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load('plane1.bmp')
        self.image = pygame.transform.rotozoom(self.image,0,0.5)
        self.rect = self.image.get_rect()
        print(self.rect)
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.rect.bottom
        self.bullet = False
        self.add = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self,ai_settings):
        if self.moving_stop == False:
            if self.moving_right and self.rect.centerx<self.screen_rect.centerx*2 - self.rect[2]/2 :
                self.rect.centerx += ai_settings.ship_right
            elif self.moving_left and self.rect.centerx > self.rect[2]/2:
                self.rect.centerx -= ai_settings.ship_left
            if self.moving_up and self.rect.bottom>self.rect[3]:
                self.rect.bottom -= ai_settings.ship_up
            elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
                self.rect.bottom += ai_settings.ship_down
        if self.love :
            self.image = pygame.image.load('2.bmp')
        else:
            self.image = pygame.image.load('plane1.bmp')
            self.image = pygame.transform.rotozoom(self.image,0 ,0.5)

        self.top = self.rect.bottom
        self.topCenterx = self.rect.centerx

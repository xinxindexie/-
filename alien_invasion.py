import sys
import time
import random
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from bullet import Bullet
from bucket import Bucket
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
    bucket = Bucket(screen)
    bullets = Group()
    lastT = 0
    score = 0
    scale = 50
    pygame.display.set_caption("alien Invasion")
    print(pygame.font.get_fonts())
    while True:
        text = pygame.font.SysFont("simsunnsimsun", 100)
        text_fmt_old = text.render(u'开始游戏', 1, (255, 0, 0),(0,255,255))
     #   print(text_fmt.get_size())
        print(scale)
        if scale == 50:
            scale = random.randint(0,1)*100

        if scale > 50:
            pygame.display.update()
            text_fmt = text.render(u'开始游戏', 1, (0,255,255),(255,0,0))

            scale -= 1
        else:
            text_fmt = text_fmt_old
            scale += 1
        screen.blit(text_fmt, (ai_settings.screen_width/2-text_fmt.get_size()[0]/2,ai_settings.screen_height/2-text_fmt.get_size()[1]/2))
     #   print(ai_settings.screen_width,ai_settings.screen_height)
        pygame.display.flip()
        enter = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               enter = True
        if enter:
            break
    # game loop
    while True:
        gf.check_event(ship,bucket)
      #  gf.update_screen(ai_settings, screen, ship)
        ship.update()
        bucket.update()
        if ship.add:
            if pygame.time.get_ticks()-lastT>500:
                new_bullet = Bullet(screen,ship,bucket,score)
                bullets.add(new_bullet)
                ship.bullet = True
                lastT = pygame.time.get_ticks()
               # print(lastT)
        if ship.bullet :
            score = gf.update_screen(ai_settings, screen, ship,bullets,bucket,score)
        else:
            gf.update_screen1(ai_settings, screen, ship,bucket)
run_game()
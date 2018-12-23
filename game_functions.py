import sys
import pygame
import random

from bullet import Bullet
'''
def check_event(ship):
    # respond to  keyboard and mouse item
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move right
                ship.moving_stop = False
                ship.moving_right = True
                ship.moving_left =False
            elif event.key == pygame.K_LEFT:
                ship.moving_stop = False
                ship.moving_left = True
                ship.moving_right = False
            if event.key == pygame.K_UP:
                # move right
                ship.moving_stop = False
                ship.moving_up = True
                ship.moving_down =False
            elif event.key == pygame.K_DOWN:
                ship.moving_stop = False
                ship.moving_down = True
                ship.moving_up = False
            if event.key == pygame.K_SPACE:
                ship.moving_stop = True
        else:
            ship.moving_stop =True
            ship.moving_left = False
            ship.moving_right = False


'''
def check_event_begin_game(ai_settings,text_bucket,text_plant,text_all):
    temp = (ai_settings.screen_width - text_plant.get_size()[0] - text_bucket.get_size()[0] - text_all.get_size()[
        0]) / (ai_settings.begin_game_text_number + 1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #   ai_settings.begin_game_num = True
            if event.key == pygame.K_1:
                ai_settings.begin_game_num = 1
            elif event.key == pygame.K_2:
                ai_settings.begin_game_num = 2
            elif event.key == pygame.K_3:
                ai_settings.begin_game_num = 3
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            #   print("x=%d,y=%d",x,y)
            if x > temp and x < temp + text_bucket.get_size()[ 0] and y > ai_settings.screen_height / 2 and \
                    y < ai_settings.screen_height / 2 + text_bucket.get_size()[1]:
                ai_settings.begin_game_num = 1
            elif x > temp * 2 + text_bucket.get_size()[0] and x < temp * 2 + text_bucket.get_size()[0] + \
                    text_plant.get_size()[0] and y > ai_settings.screen_height / 2 and y < ai_settings.screen_height / 2 + \
                    text_bucket.get_size()[1]:
                ai_settings.begin_game_num = 2
            elif x > temp * 3 + text_bucket.get_size()[0] + text_plant.get_size()[0] and x < \
                    temp * 3 + text_bucket.get_size()[0] + text_plant.get_size()[0] + text_all.get_size()[0] and \
                    y > ai_settings.screen_height / 2 and y < ai_settings.screen_height / 2 + \
                text_bucket.get_size()[1]:
                ai_settings.begin_game_num = 3



def check_event(ship,bucket):
    # respond to  keyboard and mouse item
    pressed_key =pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pressed_key[pygame.K_SPACE] :
        ship.moving_stop = True
    else:
        ship.moving_stop = False
    if pressed_key[pygame.K_UP]:
        ship.moving_up = True
    else:
        ship.moving_up = False
    if pressed_key[pygame.K_DOWN] :
        ship.moving_down = True
    else:
        ship.moving_down = False
    if pressed_key[pygame.K_LEFT]:
        ship.moving_left = True
    else:
        ship.moving_left = False
    if pressed_key[pygame.K_RIGHT]:
        ship.moving_right = True
    else:
        ship.moving_right = False
    if pressed_key[pygame.K_RIGHT] & pressed_key[pygame.K_LEFT]:
        ship.moving_left = False
        ship.moving_right = False
    if pressed_key[pygame.K_DOWN] & pressed_key[pygame.K_UP]:
        ship.moving_down = False
        ship.moving_up = False
    if pressed_key[pygame.K_a] :
        ship.attack = True
    else:
        ship.attack = False
    if pressed_key[pygame.K_l] :
        ship.love = True
    else:
        ship.love = False
    if pressed_key[pygame.K_RETURN]:
        ship.add = True
    else:
        ship.add = False
    if pressed_key[pygame.K_a]:
        bucket.moving_left = True
    else:
        bucket.moving_left = False
    if pressed_key[pygame.K_d]:
        bucket.moving_right = True
    else:
        bucket.moving_right = False
    if pressed_key[pygame.K_ESCAPE]:
        sys.exit()



def update_screen(ai_settings,screen,ship,bullets,bucket):
    # fill color
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        if bullet.update(ai_settings):
            bullets.remove(bullet)
        bullet.image = pygame.transform.rotate(bullet.image,90)
        bullet.blitme()
    #   print(bullet.rect.bottom,bucket.rect.bottom-bucket.rect[3],bullet.rect.centerx,bucket.rect.centerx-bucket.rect[2],bucket.rect.centerx+bucket.rect[2] )
        if bullet.rect.bottom == bucket.rect.bottom-bucket.rect[3] and bullet.rect.centerx > bucket.rect.centerx-bucket.rect[2] and bullet.rect.centerx<bucket.rect.centerx+bucket.rect[2]:
            ai_settings.score+=1
            print(bullet.image.get_size())
            if bullet.image.get_size()[0]>=50:
                ai_settings.score+=4
    #print(score)
    ship.blitme()
    bucket.blitme()
    text = pygame.font.SysFont('宋体',100)
    text_fmt = text.render(str(ai_settings.score),1,(255,255,0))
    screen.blit(text_fmt,(0,0))



    # visualiaze the window
    pygame.display.flip()


def update_screen1(ai_settings,screen,ship,bucket):
    # fill color
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    bucket.blitme()
    # visualiaze the window
    pygame.display.flip()

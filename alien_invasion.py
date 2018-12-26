import sys
import time
import random
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from bullet import Bullet
from bucket import Bucket
from bird import Bird
import game_functions as gf


def begin_game(ai_settings,screen):
    while True:
        text = pygame.font.SysFont(ai_settings.begin_game_textFont, ai_settings.begin_game_textSize)
        text_fmt_old = text.render(ai_settings.begin_game_text, 1, ai_settings.begin_game_textColor,ai_settings.begin_game_textBgColor)
     #   print(text_fmt.get_size())
     #   print(ai_settings.scale)
        if ai_settings.scale == 0:
        #    ai_settings.scale = random.randint(0,1)*ai_settings.begin_game_textSize
            ai_settings.scale = ai_settings.begin_game_textSize
        if ai_settings.scale > ai_settings.begin_game_textSize/2:
            pygame.display.update()
            text_fmt = text.render(ai_settings.begin_game_text, 1, ai_settings.begin_game_textBgColor,ai_settings.begin_game_textColor)
            ai_settings.scale -= 1
        else:
            text_fmt = text_fmt_old
            ai_settings.scale -= 1
        screen.blit(text_fmt, (ai_settings.screen_width/2-text_fmt.get_size()[0]/2,ai_settings.screen_height/2-text_fmt.get_size()[1]*1.5))
     #   print(ai_settings.screen_width,ai_settings.screen_height)
        # 选择控制无人机还是控制竹篮还是两个都选择
        #显示可以选择项
        text = pygame.font.SysFont(ai_settings.begin_game_textFont, ai_settings.begin_game_textSize_choose)
        text_plant = text.render(ai_settings.begin_game_text_plant, 1, ai_settings.begin_game_textBgColor,
                               ai_settings.begin_game_textColor)
        text_bucket = text.render(ai_settings.begin_game_text_bucket, 1, ai_settings.begin_game_textBgColor,
                                 ai_settings.begin_game_textColor)
        text_all = text.render(ai_settings.begin_game_text_all, 1, ai_settings.begin_game_textBgColor,
                                 ai_settings.begin_game_textColor)
        #显示画面

        screen.blit(text_bucket, ((ai_settings.screen_width  - text_plant.get_size()[0] - text_bucket.get_size()[0]-text_all.get_size()[0])/
                                  (ai_settings.begin_game_text_number+1),
                                  ai_settings.screen_height / 2 ))
        screen.blit(text_plant, ((ai_settings.screen_width  - text_plant.get_size()[0] - text_bucket.get_size()[0]-text_all.get_size()[0])/
                                  (ai_settings.begin_game_text_number+1)*2+text_bucket.get_size()[0],
                                 ai_settings.screen_height / 2))
        screen.blit(text_all, ((ai_settings.screen_width  - text_plant.get_size()[0] - text_bucket.get_size()[0]-text_all.get_size()[0])/
                                  (ai_settings.begin_game_text_number+1)*3+text_bucket.get_size()[0]+text_plant.get_size()[0],
                                 ai_settings.screen_height / 2))
     #   print((ai_settings.screen_width  - text_plant.get_size()[0] - text_bucket.get_size()[0]-text_all.get_size()[0])/(ai_settings.begin_game_text_number+1)*3+text_bucket.get_size()[0]+text_plant.get_size()[0])

        pygame.display.flip()
     #   pygame.time.delay(100000)
        gf.check_event_begin_game(ai_settings,text_bucket,text_plant,text_all)
     #   print(ai_settings.begin_game_num)
        if ai_settings.begin_game_num>0:
            break

def over_game(ai_settings,screen,WOL):

    text = pygame.font.SysFont(ai_settings.over_game_textFont, ai_settings.over_game_textSize)
    if WOL:
        text_over_game = text.render(ai_settings.over_game_win_text, 1, ai_settings.over_game_textColor,
                                     ai_settings.over_game_textBgColor)
    else:
        text_over_game = text.render(ai_settings.over_game_loss_text, 1, ai_settings.over_game_textColor,
                                     ai_settings.over_game_textBgColor)
    screen.blit(text_over_game,(ai_settings.screen_width/2 - text_over_game.get_size()[0]/2,ai_settings.screen_height/2 - text_over_game.get_size()[1]/2))
    pygame.display.flip()
    pygame.time.delay(3000)
    run_game()
def run_game():
    # 初始化pygame
    pygame.init()
    #初始化页面
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
    bucket = Bucket(screen)
    bird = Bird(screen)
    birds = Group()
    bullets = Group()
    pygame.display.set_caption(ai_settings.title)
    # print(pygame.font.get_fonts())
    # 进入游戏页面
    begin_game(ai_settings,screen)
    # game loop
    while True:
        gf.check_event(ship,bucket)
      #  gf.update_screen(ai_settings, screen, ship)
    #如果选择的模式只操作一个的话，那么另外一个的物品会自己运动
        if ai_settings.begin_game_num == 1:
            ship.moving_down = False
            ship.moving_up = False
            ship.moving_left = False
            ship.moving_right = False


            if ai_settings.game_ship_UD == 50:
                ship.add = True
                ai_settings.game_ship_UD = random.randint(0,100)
            elif ai_settings.game_ship_UD > 50 :
                ship.moving_up = True
                ai_settings.game_ship_UD -= 1
            elif ai_settings.game_ship_UD < 50:
                ship.moving_down = True
                ai_settings.game_ship_UD += 1
            if ai_settings.game_ship_LR == 50:
                ai_settings.game_ship_LR = random.randint(0,100)
            elif ai_settings.game_ship_LR > 50 :
                ship.moving_left = True
                ai_settings.game_ship_LR -= 1
            elif ai_settings.game_ship_LR < 50:
                ship.moving_right = True
                ai_settings.game_ship_LR += 1
        if ai_settings.begin_game_num == 2:
            bucket.moving_right = False
            bucket.moving_left = False
            if ai_settings.game_bucket_LR == 50:
                ai_settings.game_bucket_LR = random.randint(0,100)
            elif ai_settings.game_bucket_LR > 50:
                bucket.moving_right = True
                ai_settings.game_bucket_LR -=1
            elif ai_settings.game_bucket_LR <50:
                bucket.moving_left = True
                ai_settings.game_bucket_LR +=1

        ship.update(ai_settings)
        bucket.update(ai_settings)
        if ship.add:
            if pygame.time.get_ticks()-ai_settings.ball_lastT>ai_settings.ball_interval:
                print(pygame.time.get_ticks())
                new_bullet = Bullet(screen,ship,bucket,ai_settings.score)
                bullets.add(new_bullet)
                ship.bullet = True
                ai_settings.ball_lastT = pygame.time.get_ticks()
               # print(ai_settings.ball_lastT)
        if random.randint(0,3) == 1:
            if pygame.time.get_ticks()-ai_settings.bird_lastT>ai_settings.bird_interval:
                new_bird = Bird(screen)
                birds.add(new_bird)
                ai_settings.bird_lastT = pygame.time.get_ticks()
        gf.update_screen(ai_settings, screen, ship, bullets, bucket, birds)
    #    if ship.bullet :
    #        gf.update_screen(ai_settings, screen, ship,bullets,bucket,birds)
    #    else:
    #        gf.update_screen1(ai_settings, screen, ship,bucket,birds)

        if ai_settings.score >= ai_settings.winScore:
            over_game(ai_settings,screen,True)
        if ai_settings.health_point <=0 :
            over_game(ai_settings,screen,False)
run_game()
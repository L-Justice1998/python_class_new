# Creator:justice 廖振谊
# Creat time:2022/6/14 20:17
from plane_war_class import *
import time
import pygame

class Plane_War(object):
    def __init__(self):
        print("Game initialazation")
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        self.__create_sprite()

        # 设置定时器事件 - 创建敌机　设定敌机的刷新时间
        # 英雄子弹事件的刷新频率
        pygame.time.set_timer(ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,700)

    def __create_sprite(self):
        bg1=BackGround()
        bg2=BackGround(True)

        self.back_group=pygame.sprite.Group(bg1,bg2)
        self.enemy_group=pygame.sprite.Group()
        self.hero=Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("Game starts right now")

        while True:
            self.clock.tick(FRAME_FREQUENCE)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               Plane_War.__game_over()
            elif event.type==ENEMY_EVENT:
                enemy=Enemy()
                self.enemy_group.add(enemy)

            elif event.type==HERO_FIRE_EVENT:
                self.hero.fire()

            # 使用键盘提供的方法获取键盘按键 - 按键元组
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 5
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -5
            else:
                self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        enemies=pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        if len(enemies)>0:
            self.hero.kill()
            m="./sound/use_bomb.wav"
            pygame.mixer.music.load(m)
            pygame.mixer.music.play()
            time.sleep(1)

            Plane_War.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("The game is over")

        pygame.quit()
        exit()  # 进程结束

if __name__ == '__main__':
        # 创建游戏对象
        pygame.init()
        game = Plane_War()

        # 启动游戏
        game.start_game()

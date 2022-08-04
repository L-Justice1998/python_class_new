# Creator:justice 廖振谊
# Creat time:2022/6/14 19:01
import random
import pygame
#设置屏幕大小常量 (x,y,width,height)
SCREEN_RECT=pygame.Rect(0,0,480,750)
#设置刷新频率
FRAME_FREQUENCE=30

# 创建敌机的定时器常量，为事件定义不同名字的常量，从而能够区分，从24算起
ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件，为事件定义不同名字的常量，从而能够区分
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):#终极父类 所有飞机和敌人等对象都需继承于此
    def __init__(self,image_name,speed=1):
        super().__init__()
        #初始化图像大小 尺寸 速度
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
        self.speed=speed

    def update(self):
        """
        每次更新y轴上的位置
        :return:
        """
        self.rect.y+=self.speed

class BackGround(GameSprite):
    def __init__(self,is_alt=False):
        super().__init__("./images/background.png")
        #若为交替图像 则设置初始位置（最上面的位置）
        if is_alt:
            self.rect.y=-self.rect.height

    def update(self):
        super().update()

        if self.rect.y>self.rect.height:
            self.rect.y=-self.rect.height

class Enemy(GameSprite):
    def __init__(self):
        i=str(random.randint(1,3))
        super().__init__("./images/enemy1.png")
        self.speed=random.randint(1,10)
        #定义初始位置，注意原点在左上角
        self.rect.y=-self.rect.height
        max_range=SCREEN_RECT.width-self.rect.width
        self.rect.x=random.randint(1,max_range)

    def update(self):
        super().update()
        if self.rect.y>SCREEN_RECT.height:
            self.kill()

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-5)

    def update(self):
        super().update()
        if self.rect.y<0:
            self.kill()



class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png")
        self.rect.bottom=SCREEN_RECT.bottom-10
        self.rect.centerx=SCREEN_RECT.centerx

        self.bullets=pygame.sprite.Group()

    def update(self):
        self.rect.x+=self.speed
        if self.rect.x>SCREEN_RECT.right:
            self.rect.x=SCREEN_RECT.right
        if self.rect.x<0:
            self.rect.x=0

    def fire(self):
        bullet=Bullet()

        bullet.rect.centerx=self.rect.centerx
        bullet.rect.bottom=self.rect.top-10

        self.bullets.add(bullet)


import random
import pygame
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FREAM_PER_SECOND = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_BOTTOM_PADDING = 80


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = 1

    def update(self):
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("images/background.png")
        if is_alt:
            self.rect.y = self.rect.height

    def update(self):
        super().update()

        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("images/enemy1.png")
        self.speed = random.randint(1, 3)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.bottom = 0

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super().__init__("images/me1.png")
        self.speed = 0
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - HERO_BOTTOM_PADDING
        self.bulletGroup = pygame.sprite.Group()

    def fire(self):
        self.bulletGroup.add(Bullet(self.rect.centerx, self.rect.y))

    def super_fire(self):
        self.bulletGroup.add(Bomb(self.rect.centerx, self.rect.y))
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width
        if self.rect.x < 0:
            self.rect.x = 0
    

class Bullet(GameSprite):
    def __init__(self, centerx, bottom):
        super().__init__("images/bullet1.png")
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speed = -2

    def update(self):
        super().update()
        if self.rect.y <= 0:
            self.kill()


class Bomb(GameSprite):
    def __init__(self, centerx, bottom):
        super().__init__("images/bomb.png")
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speed = -2

    def update(self):
        super().update()
        if self.rect.y <= 0:
            self.kill()

import pygame
from plan_sprites import *


class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        bg1 = BackgroundSprite()
        bg2 = BackgroundSprite(True)
        self.backgroundGroup = pygame.sprite.Group(bg1, bg2)
        self.enemyGroup = pygame.sprite.Group()
        self.hero = Hero()
        self.HeroGroup = pygame.sprite.Group(self.hero)

    def __create_enemy(self):
        enemy = Enemy()
        self.enemyGroup.add(enemy)

    def __event_handler(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == CREATE_ENEMY_EVENT:
                self.__create_enemy()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.hero.fire()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                self.hero.super_fire()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __update_sprites(self):
        screen = self.screen
        self.backgroundGroup.update()
        self.backgroundGroup.draw(screen)
        self.enemyGroup.update()
        self.enemyGroup.draw(screen)
        self.HeroGroup.update()
        self.HeroGroup.draw(screen)
        self.hero.bulletGroup.update()
        self.hero.bulletGroup.draw(screen)

    def __check_collide(self):
        enemyGroup = self.enemyGroup
        bullteGroup = self.hero.bulletGroup
        hero = self.hero
        pygame.sprite.groupcollide(enemyGroup, bullteGroup, True, True)
        enemies = pygame.sprite.spritecollide(hero, enemyGroup, True)
        if len(enemies) > 0:
            self.quit_game()

    def start_game(self):
        while True:
            self.clock.tick(FREAM_PER_SECOND)
            self.__event_handler()
            self.__update_sprites()
            self.__check_collide()
            pygame.display.update()

    @staticmethod
    def quit_game():
        pygame.quit()
        exit()

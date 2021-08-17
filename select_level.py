import os
import time
import pygame
from settings import *
from enemy.enemy import EnemyGroup

bg = pygame.transform.scale(pygame.image.load(os.path.join("images/unnamed.png")), (WIN_WIDTH, WIN_HEIGHT))
easy_btn = pygame.transform.scale(pygame.image.load(os.path.join("images/Easy_btn.png")), (350, 150))
hard_btn = pygame.transform.scale(pygame.image.load(os.path.join("images/Hard_btn.png")), (350, 150))


class Button:
    def __init__(self, image, name: str, x: int, y: int):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False

    @property
    def response(self):
        return self.name


class SelectLevel:
    def __init__(self):
        self.select_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.easy_btn = Button(easy_btn, "easy", 256, 300)
        self.hard_btn = Button(hard_btn, "hard", 768, 300)
        self.button = []
        self.quit = False

    def run(self):
        run = True
        while run:
            x, y = pygame.mouse.get_pos()
            self.select_win.blit(bg, (0, 0))
            self.select_win.blit(easy_btn, (112, 200))
            self.select_win.blit(hard_btn, (562, 200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.quit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy_btn.clicked(x, y):
                        self.button.append("easy")
                        return self.button
                    if self.hard_btn.clicked(x, y):
                        self.button.append("hard")
                        return self.button
            pygame.display.update()


from __future__ import annotations
import pygame
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE, POPULARITY_IMAGE, CALENDER_IMAGE
from settings import Thumbnail, Thumbnail_WIDTH, Thumbnail_HEIGHT, VACANCY, PRESIDENT_IMAGE ,SUCCESSFUL_IMAGE ,DEFECT_IMAGE
from color_settings import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from enemy.enemy import EnemyGroup
    from tower.tower_factory import Tower, Vacancy
    from menu.menus import Menu
    from game.model import GameModel


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.SysFont("arial", 28)

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    def draw_stop(self, stop_button):
        self.win.blit(stop_button.image, stop_button.rect)
        x, y = pygame.mouse.get_pos()
        stop_button.create_frame(x, y)
        if stop_button.frame is not None:
            pygame.draw.rect(self.win, BLACK, stop_button.frame, 7)

    def draw_enemies(self, enemies: EnemyGroup):
        for en in enemies.get():
            self.win.blit(en.image, en.rect)
            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(self.win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def draw_towers(self, towers: list):
        # draw tower
        for tw in towers:
            self.win.blit(tw.image, tw.rect)

    def draw_range(self, selected_tower: Tower):
        # draw tower range
        if selected_tower is not None:
            tw = selected_tower
            # create a special surface that is able to render semi-transparent image
            surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
            transparency = 120
            pygame.draw.circle(surface, (128, 128, 128, transparency), tw.rect.center, tw.range)
            self.win.blit(surface, (0, 0))

    def draw_menu(self, menu: Menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_plots(self, plots: list):
        for pt in plots:
            self.win.blit(pt.image, pt.rect)

    def draw_money(self, money: int):
        self.font = pygame.font.SysFont("arial", 28)
        text = self.font.render(f"Money: {money}", True, BLACK)
        self.win.blit(text, (900, 0))

    '''def draw_wave(self, wave: int):
        self.font = pygame.font.SysFont("arial", 28)
        text = self.font.render(f"Wave: {wave}", True, BLACK)
        self.win.blit(text, (900, 10))'''

    def draw_popularity(self, support: int, notsupport: int):
        self.win.blit(POPULARITY_IMAGE, (800, 150))
        self.font = pygame.font.SysFont("arial", 50)
        text = self.font.render(f"{support}%", True, GREEN)
        self.win.blit(text, (810, 220))
        text = self.font.render(f"{notsupport}%", True, RED)
        self.win.blit(text, (905, 220))

    def draw_year_month(self, year: int, month: int, date: int, max_date: int):
        self.win.blit(CALENDER_IMAGE, (900, 290))
        self.font = pygame.font.SysFont("arial", 28)
        text = self.font.render(f"{year} / {month}", True, BLACK)
        self.win.blit(text, (928, 290))
        # draw date bar
        bar_height = 7
        bar_length = 100 * (max_date-date)/max_date
        pygame.draw.rect(self.win, GRAY, [800, 310, 100, bar_height])
        pygame.draw.rect(self.win, BLACK, [800, 300, bar_length, bar_height])

    def draw_thumbnail(self, menu: Menu):
        # create semi-transparent surface
        transparent_surface = pygame.Surface((Thumbnail_WIDTH + 20, Thumbnail_HEIGHT + 20), pygame.SRCALPHA)
        transparency = 50  # define transparency: 0~255, 0 is fully transparent
        # draw the rectangle on the transparent surface
        pygame.draw.rect(transparent_surface, (100, 100, 100, transparency),
                         [0, 0, Thumbnail_WIDTH + 20, Thumbnail_HEIGHT + 20])
        self.win.blit(transparent_surface, (140, 430))
        for i in range(12):
            if menu.rect.center == VACANCY[i]:
                self.win.blit(Thumbnail[i], (150, 440))

    def draw_Number(self, menu: Menu, tower: Tower, plot: Vacancy):
        x, y = pygame.mouse.get_pos()
        for btn in menu.buttons:
            if btn.rect.collidepoint(x, y):
                money = 100
                if btn.name == "sell":
                    money = tower.get_cost()
                if btn.name == "upgrade" and tower.level < 5:
                    money = tower.get_upgrade_cost()
                if plot is not None:
                    if btn.name == "mask":
                        money = 150
                    if btn.name == "injection":
                        money = 300
                    if btn.name == "alcohol":
                        money = 400
                    if btn.name == "foreheadgun":
                        money = 200

                font = pygame.font.SysFont("arial", 50)
                text = font.render(f"{money}", True, (0,0,0))
                self.win.blit(text, (x, y))

    def draw_game_result(self, support: int, notsupport: int):
        #pygame.draw.rect(self.win, BLACK, [100, 100, 640, 375])
        #pygame.draw.rect(self.win, WHITE, [115, 115, 610, 345])
        if support > notsupport:
            self.win.blit(SUCCESSFUL_IMAGE, (120, 120))
        else:
            self.win.blit(DEFECT_IMAGE, (120, 120))
        #self.font = pygame.font.SysFont("arial", 50)
        #text = self.font.render(f"NCKU president Su", True, BLACK)
        #self.win.blit(text, (210, 350))
        #text = self.font.render(f"Re-elected successfully !!", True, BLACK)
        #self.win.blit(text, (210, 400))


    '''def draw_hp(self, lives):
        # draw_lives
        hp_rect = HP_IMAGE.get_rect()
        for i in range(10):
            self.win.blit(HP_GRAY_IMAGE, (WIN_WIDTH // 2 - hp_rect.w * (2.5 - i % 5), hp_rect.h * (i // 5)))
        for i in range(lives):
            self.win.blit(HP_IMAGE, (WIN_WIDTH // 2 - hp_rect.w * (2.5 - i % 5), hp_rect.h * (i // 5)))'''



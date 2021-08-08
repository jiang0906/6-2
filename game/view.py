import pygame
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE, POPULARITY_IMAGE, CALENDER_IMAGE
from settings import Thumbnail, Thumbnail_WIDTH, Thumbnail_HEIGHT, VACANCY
from color_settings import *


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.SysFont("comicsans", 30)

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    def draw_enemies(self, enemies):
        for en in enemies.get():
            self.win.blit(en.image, en.rect)
            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health)
            max_bar_width = en.rect.w
            bar_height = 5
            pygame.draw.rect(self.win, RED, [en.rect.x, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, GREEN, [en.rect.x, en.rect.y - 10, bar_width, bar_height])

    def draw_towers(self, towers):
        # draw tower
        for tw in towers:
            self.win.blit(tw.image, tw.rect)

    def draw_range(self, selected_tower):
        # draw tower range
        if selected_tower is not None:
            tw = selected_tower
            # create a special surface that is able to render semi-transparent image
            surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
            transparency = 120
            pygame.draw.circle(surface, (128, 128, 128, transparency), tw.rect.center, tw.range)
            self.win.blit(surface, (0, 0))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_plots(self, plots):
        for pt in plots:
            self.win.blit(pt.image, pt.rect)

    def draw_money(self, money: int):
        """ (Q2.1)render the money"""
        text = self.font.render(f"Money: {money}", True, BLACK)
        self.win.blit(text, (900, 30))

    def draw_wave(self, wave: int):
        """(Q2.2)render the wave"""
        text = self.font.render(f"Wave: {wave}", True, BLACK)
        self.win.blit(text, (900, 15))

    def draw_popularity(self, support: int, notsupport: int):
        self.win.blit(POPULARITY_IMAGE, (800, 150))
        self.font = pygame.font.SysFont("comicsans", 50)
        text = self.font.render(f"{support}%", True, GREEN)
        self.win.blit(text, (830, 220))
        text = self.font.render(f"{notsupport}%", True, RED)
        self.win.blit(text, (930, 220))

    def draw_year_month(self, year: int, month: int, date: int, max_date: int):
        self.win.blit(CALENDER_IMAGE, (900, 290))
        self.font = pygame.font.SysFont("comicsans", 30)
        text = self.font.render(f"{year} / {month}", True, BLACK)
        self.win.blit(text, (930, 298))
        # draw date bar
        bar_height = 7
        pygame.draw.rect(self.win, GRAY, [800, 310, max_date*1.5, bar_height])
        pygame.draw.rect(self.win, BLACK, [800, 300, (max_date-date)*1.5, bar_height])

    def draw_thumbnail(self, menu):
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

    '''def draw_hp(self, lives):
        # draw_lives
        hp_rect = HP_IMAGE.get_rect()
        for i in range(10):
            self.win.blit(HP_GRAY_IMAGE, (WIN_WIDTH // 2 - hp_rect.w * (2.5 - i % 5), hp_rect.h * (i // 5)))
        for i in range(lives):
            self.win.blit(HP_IMAGE, (WIN_WIDTH // 2 - hp_rect.w * (2.5 - i % 5), hp_rect.h * (i // 5)))'''



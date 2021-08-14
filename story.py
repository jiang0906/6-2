import pygame
from settings import *

class Story:
    def __init__(self):
        self.story_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.stories = [story_1, story_2, story_3, story_4, story_5, story_6, story_7]
        self.story_btn = Clicked(0, 0, WIN_WIDTH, WIN_HEIGHT)
        self.skip_btn = Clicked(900, 0, 100, 50)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        n = 0
        while run:
            clock.tick(FPS)
            x, y = pygame.mouse.get_pos()
            self.story_win.blit(skip_btn, (900, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.story_btn.is_clicked(x, y) and n < 7:
                        self.story_win.blit(self.stories[n], (0, 0))
                        n += 1
                        run = True
                    else:
                        run = False
                    if self.skip_btn.is_clicked(x, y):
                        run = False
            pygame.display.update()
        pygame.mixer.music.stop()


class Clicked:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = None

    def is_clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False




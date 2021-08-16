import pygame
from settings import *


class Story:
    def __init__(self, story_win):
        self.win = story_win
        '''self.stories = [story_1, story_2, story_3, story_4, story_5, story_6, story_7]'''
        self.__stories = []
        for i in range(4):
            self.__stories.append(Picture(500, 500, DIALOGUE_IMAGE[i]))
        for i in range(3):
            self.__stories.append(Picture(WIN_WIDTH/2, WIN_HEIGHT/2, ALARM_IMAGE[i]))
        self.skip_btn = Picture(980, 580, skip_btn)
        self.quit = False

    def run(self):
        run = True
        clock = pygame.time.Clock()
        n = 0
        while run:
            clock.tick(FPS)
            x, y = pygame.mouse.get_pos()
            self.skip_btn.draw(self.win)
            self.__stories[n].draw(self.win)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.quit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.skip_btn.clicked(x, y) or n == 6:
                        if n < 4:
                            pygame.mixer.music.load("./sound/sound_in_game.wav")
                            pygame.mixer.music.set_volume(0.2)
                            pygame.mixer.music.play(-1)
                        run = False
                    if self.__stories[n].clicked(x, y) and n < 6:
                        n += 1
                        run = True
                    if n == 4:
                        pygame.mixer.music.load("./sound/sound_in_game.wav")
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.play(-1)

            pygame.display.update()

        '''pygame.mixer.music.stop()'''


class Picture:
    def __init__(self, x: int, y: int, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x: int, y: int) -> bool:
        return True if self.rect.collidepoint(x, y) else False

    def draw(self, win):
        win.blit(self.image, self.rect)






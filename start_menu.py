import pygame
import os
from game.game import Game
from story import Story
from color_settings import *
from settings import *


pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()


class StartMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("images", "start_ncku_new.jpg")), (WIN_WIDTH, WIN_HEIGHT))
        # button
        self.start_btn = Buttons(349, 315, 338, 101)  # x, y, width, height
        self.sound_btn = Buttons(845, 19, 80, 70)
        self.mute_btn = Buttons(935, 19, 80, 70)
        self.buttons = [self.sound_btn,
                        self.mute_btn]
        # music and sound
        self.sound = pygame.mixer.Sound("./sound/sound_in_game.wav")


    ''''def play_music(self):
        pygame.mixer.music.load("./sound/sound_start.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.2)'''

    def menu_run(self):
        run = True
        clock = pygame.time.Clock()
        pygame.display.set_caption("成大安全 學校有錢")
        #self.play_music()
        pygame.mixer.music.load("./sound/sound_start.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.sound.set_volume(0.2)
        while run:
            clock.tick(FPS)
            self.menu_win.blit(self.bg, (0, 0))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.start_btn.clicked(x, y):
                        story = Story()
                        story.run()
                        # pygame.mixer.music.stop() 移到story裡面 不然會有初始化的問題
                        self.sound.play()
                        game = Game()
                        game.run()
                        run = False
                    """(Q1.1) music on/off according to the button"""
                    # (hint) pygame.mixer.music.pause/unpause
                    #如果有點擊則撥放聲音
                    if self.sound_btn.clicked(x, y):
                        pygame.mixer.music.unpause()
                    if self.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()

            """(Q1.2) create button frame and draw"""
            # while cursor is moving (not click)
            # (hint) use a for loop to go through all the buttons, create the frame, and draw it.
            #看使用者將滑鼠移至目標上,則顯示白色框框
            for btn in self.buttons:
                btn.create_frame(x, y)
                btn.draw_frame(self.menu_win)
            self.start_btn.create_frame(x, y)
            self.start_btn.draw_frame_start(self.menu_win)
            pygame.display.update()
        pygame.quit()


class Buttons:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = None

    def clicked(self, x: int, y: int) -> bool:
        if self.rect.collidepoint(x, y):
            return True
        return False

    def create_frame(self, x: int, y: int):
        """if cursor position is on the button, create button frame"""
        if self.clicked(x, y):
            x, y, w, h = self.rect
            self.frame = pygame.Rect(x - 5, y - 5, w + 10, h + 10)
        else:
            self.frame = None

    def draw_frame(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, BLACK, self.frame, 7)

    def draw_frame_start(self, win):
        if self.frame is not None:
            pygame.draw.rect(win, WHITE, self.frame, 10)


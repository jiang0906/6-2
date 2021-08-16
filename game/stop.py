import pygame
from settings import WIN_WIDTH, WIN_HEIGHT, STOP_IMAGE, BLACK


class Stop:
    def __init__(self, x: int, y: int):
        self.image = STOP_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.is_stop = False
        self.frame = None

    def is_stopped(self):
        if self.is_stop:
            pygame.mixer.music.pause()
            return True
        else:
            pygame.mixer.music.unpause()
            return False

    def clicked(self, x: int, y: int) -> bool:
        return True if self.rect.collidepoint(x, y) else False

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

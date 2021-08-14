import pygame
import os

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600

# image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "NCKU.png")), (WIN_WIDTH, WIN_HEIGHT))
STOP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "stop.png")), (30, 30))
POPULARITY_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "popularity.png")), (210, 140))
CALENDER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "calendar.png")), (30, 30))
# story
story_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "story1.jpg")), (WIN_WIDTH, WIN_HEIGHT))
story_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "story2.jpg")), (WIN_WIDTH, WIN_HEIGHT))
story_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "story3.jpg")), (WIN_WIDTH, WIN_HEIGHT))
story_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "story4.jpg")), (WIN_WIDTH, WIN_HEIGHT))
story_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "story5.jpg")), (WIN_WIDTH, WIN_HEIGHT))
story_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "story6.jpg")), (WIN_WIDTH, WIN_HEIGHT))
story_7 = pygame.transform.scale(pygame.image.load(os.path.join("images", "story7.jpg")), (WIN_WIDTH, WIN_HEIGHT))
skip_btn = pygame.transform.scale(pygame.image.load(os.path.join("images", "skip_btn.png")), (100, 50))

Thumbnail_WIDTH = 204
Thumbnail_HEIGHT = 136
Thumbnail = []
for i in range(12):
    Thumbnail.append(pygame.transform.scale(pygame.image.load(f"images/background_{i}.jpg"), (Thumbnail_WIDTH, Thumbnail_HEIGHT)))

PRESIDENT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "president.png")), (600, 340))
SUCCESSFUL_IMAGE=pygame.transform.scale(pygame.image.load(os.path.join("images", "game_over_successful.jpg")), (600, 340))
DEFECT_IMAGE=pygame.transform.scale(pygame.image.load(os.path.join("images", "game_over_defect.jpg")), (600, 340))

# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)

PATH_1 = [(35, 431), (98, 380), (420, 380), (420, 537)]
PATH_2 = [(419, 28), (419, 110), (657, 110), (657, 349), (582, 380), (420, 380), (420, 537)]
PATH_3 = [(417, 28), (418, 107), (98, 106), (97, 170), (138, 221), (418, 218), (420, 536)]
VACANCY = [(110, 448), (331, 444), (179, 160), (291, 157), (417, 163), (338, 296), (233, 295), (142, 292), (496, 294), (584, 167), (498, 444), (582, 297)]
# enemy path
'''# 打開txt檔
fileObject = open("paths/path_1.txt ", 'r')
# 讀取一行內容
line = fileObject.readline()
# 將內容append進[]
PATH_1 = []
while line:
    PATH_1.append(eval(line))
    line = fileObject.readline()
# 關閉txt檔
fileObject.close()

# 打開txt檔
fileObject = open("paths/path_2.txt ", 'r')
# 讀取一行內容
line = fileObject.readline()
# 將內容append進[]
PATH_2 = []
while line:
    PATH_2.append(eval(line))
    line = fileObject.readline()
# 關閉txt檔
fileObject.close()

# 打開txt檔
fileObject = open("paths/path_3.txt ", 'r')
# 讀取一行內容
line = fileObject.readline()
# 將內容append進[]
PATH_3 = []
while line:
    PATH_3.append(eval(line))
    line = fileObject.readline()
# 關閉txt檔
fileObject.close()

# 打開txt檔
fileObject = open("paths/vacancy.txt ", 'r')
# 讀取一行內容
line = fileObject.readline()
# 將內容append進[]
VACANCY = []
while line:
    VACANCY.append(eval(line))
    line = fileObject.readline()
# 關閉txt檔
fileObject.close()'''

# base
BASE = pygame.Rect(415, 535, 50, 50)

import pygame
from game.controller import GameControl
from game.model import GameModel
from game.view import GameView
from settings import FPS
from story import Story
from select_level import SelectLevel


class Game:
    def run(self):
        # initialization
        pygame.init()
        game_model = GameModel()  # core of the game (database, game logic...)
        game_view = GameView()  # render everything
        game_control = GameControl(game_model, game_view)  # deal with the game flow and user request


        quit_game = False
        story_done = False
        select_level = False
        while not quit_game:
            pygame.time.Clock().tick(FPS)  # control the frame rate
            game_control.receive_user_input()  # receive user input
            game_control.update_model()  # update the model
            game_control.update_view()  # update the view
            pygame.display.update()
            if story_done is False:
                story = Story(game_view.win)
                story.run()
                story_done = True
                if story.quit is True:
                    break
            if select_level is False:
                select = SelectLevel()
                select.run()
                select_level = True
                if select.quit is True:
                    break

            quit_game = game_control.quit_game

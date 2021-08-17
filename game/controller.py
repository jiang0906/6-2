from __future__ import annotations
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.model import GameModel
    from game.view import GameView


# controller
class GameControl:
    def __init__(self, game_model: GameModel, game_view: GameView):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0]
                       }
        self.request = None  # response of user input

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        if self.model.stop_button.is_stopped() is False:  # 如果暫停了就不update
            self.model.user_request(self.request)
            self.model.call_menu()
            self.model.towers_attack()
            self.model.enemies_advance()
            self.model.condition_update()

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

    def update_view(self):
        # render background
        self.view.draw_bg()
        self.view.draw_stop(self.model.stop_button)
        '''self.view.draw_hp(self.model.hp)'''
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_towers(self.model.towers)
        self.view.draw_range(self.model.selected_tower)
        self.view.draw_plots(self.model.plots)
        """(Q2) Controller request View to render something"""
        if self.model.menu is not None:
            self.view.draw_thumbnail(self.model.menu)
            self.view.draw_menu(self.model.menu)
            self.view.draw_Number(self.model.menu, self.model.selected_tower, self.model.selected_plot)
        # 顯示錢錢跟敵人來了幾波
        self.view.draw_money(self.model.money)
        # self.view.draw_wave(self.model.wave)
        self.view.draw_popularity(self.model.support, self.model.notsupport)
        self.view.draw_year_month(self.model.year, self.model.month, self.model.date, self.model.max_date)
        if self.model.check_game_over() is True:
            self.view.draw_game_result(self.model.support, self.model.notsupport)

    @property
    def quit_game(self):
        return self.events["game quit"]


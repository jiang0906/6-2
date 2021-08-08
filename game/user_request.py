import pygame
import time
from tower.tower_factory import Tower, Vacancy

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        # 第一波敵人會在開始遊戲後3秒出現，之後只要場上為空即會出現
        if time.time() - model.timer >= 3 and model.enemies.is_empty():
            model.enemies.add(10)
            model.wave += 1
            model.timer = time.time()


class TowerSeller:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += model.selected_tower.get_cost()
            model.plots.append(Vacancy(x, y))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """(Bonus.1) upgrade tower"""
        if user_request == "upgrade" and model.selected_tower.level < 5:
            # if the money > upgrade cost of the selected tower , level+1
            # use model.selected_tower to access the selected tower data
            # use model.money to access to money data

            #如果錢達到升級的要求,則塔可升級
            if model.money >= model.selected_tower.get_upgrade_cost():
                model.money -= model.selected_tower.get_upgrade_cost()
                model.selected_tower.level += 1

class TowerFactory:
    def __init__(self, subject):
        subject.register(self)
        self.tower_name = ["mask", "injection", "alcohol", "foreheadgun"]

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                x, y = model.selected_plot.rect.center
                tower_dict = {"mask": Tower.Mask(x, y), "injection": Tower.Injection(x, y),
                              "alcohol": Tower.Alcohol(x, y), "foreheadgun": Tower.Foreheadgun(x, y)}
                new_tower = tower_dict[user_request]
                if model.money >= new_tower.get_cost():
                    model.money -= new_tower.get_cost()
                    model.towers.append(new_tower)
                    model.plots.remove(model.selected_plot)
                    model.selected_plot = None


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()


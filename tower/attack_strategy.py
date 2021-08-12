from __future__ import annotations
import math
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from enemy.enemy import EnemyGroup
    from tower.tower_factory import Tower, Vacancy


def in_range(enemy, tower: Tower):
    x1, y1 = enemy.rect.center
    x2, y2 = tower.rect.center
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance <= tower.range:
        return True
    return False


class AttackStrategy(ABC):
    """Abstract class of attack method"""
    @ abstractmethod
    def attack(self, enemies: EnemyGroup, tower: Tower, cd_count: int):
        raise NotImplementedError("Please implement this method")


class SingleAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies: EnemyGroup, tower: Tower, cd_count: int):
        for en in enemies:
            if in_range(en, tower):
                multiple = en.damage_double_check
                en.health -= tower.damage*multiple
                cd_count = 0
                return cd_count # 跑完第一隻就結束,代表只攻擊一次
        return cd_count

class AOE(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies: EnemyGroup, tower: Tower, cd_count: int):
        for en in enemies:
            if in_range(en, tower):
                multiple = en.damage_double_check
                en.health -= tower.damage * multiple
                cd_count = 0
        # 整個迴圈都跑完,代表整波敵人都會受到攻擊
        return cd_count


class Slowly(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies: EnemyGroup, tower: Tower, cd_count: int):
        for en in enemies:
            # 在攻擊範圍內,給予緩速
            if in_range(en, tower):
                en.stride_revise()
                cd_count = 0
            # 在攻擊範圍外,還原原本速度
            if in_range(en, tower) is False:
                en.stride_revise_getback()
                cd_count = 0
        return cd_count


class Attack_double(AttackStrategy):
    '''make enemy in range get double damage'''
    def attack(self, enemies: EnemyGroup, tower: Tower, cd_count: int):
        for en in enemies:
            # 進範圍,傷害倍數改變
            if in_range(en, tower):
                en.damage_double(tower.level)
                cd_count = 0
            else: # 離開範圍傷害回歸一致
                en.damage_double_back()
                cd_count = 0
        return cd_count

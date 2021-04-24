from abc import ABC

from cold_ray_norilsk.src.game_model.entity.base_entity import BEntity


class BPerson(BEntity, ABC):

    __slots__ = [
        'x_pos',
        'y_pos',
        'health'
    ]

    def __init__(self, x: float = 0.0, y: float = 0.0, health: float = 100.0):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.health = health

from abc import ABC

from cold_ray_norilsk.src.game_model.entity.base_entity import BEntity


class BObject(BEntity, ABC):

    __slots__ = [
        'x_pos'
        'y_pos',
        'x_velocity',
        'y_velocity',
        'x_acceleration',
        'y_acceleration'
    ]

    def __init__(self,
                 x: float = 0.0,
                 y: float = 0.0,
                 v_x: float = 0.0,
                 v_y: float = 0.0,
                 a_x: float = 0.0,
                 a_y: float = 0.0):
        super().__init__()
        self.x_pos = x
        self.y_pos = y

        self.x_velocity = v_x
        self.y_velocity = v_y

        self.x_acceleration = a_x
        self.y_acceleration = a_y

    def tick(self, dt: float):
        self.x_pos += dt * self.x_velocity
        self.y_pos += dt * self.y_velocity

        self.x_velocity += dt * self.x_acceleration
        self.y_velocity += dt * self.y_velocity

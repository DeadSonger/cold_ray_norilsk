from abc import ABC, abstractmethod

from cold_ray_norilsk.src.game_model.mechanics.collision.base_shape import BShape


class ICollisionable(ABC):

    @abstractmethod
    @property
    def shape(self) -> BShape:
        pass

    @abstractmethod
    def on_collision(self, other: 'ICollisionable'):
        pass

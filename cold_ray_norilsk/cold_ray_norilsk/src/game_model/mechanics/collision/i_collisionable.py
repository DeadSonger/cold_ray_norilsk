from abc import ABC, abstractmethod

from cold_ray_norilsk.src.game_model.mechanics.collision.base_shape import BShape


class ICollisionable(ABC):

    @abstractmethod
    @property
    def shape(self) -> BShape:
        """Get shape of the collisionable object."""
        pass

    @abstractmethod
    def on_collision(self, other: 'ICollisionable'):
        """Actions to be performed on collision with other."""
        pass

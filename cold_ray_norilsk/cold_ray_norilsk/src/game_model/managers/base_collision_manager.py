from abc import ABC, abstractmethod
from typing import List, NamedTuple

from cold_ray_norilsk.src.game_model.mechanics.collision.i_collisionable import ICollisionable


CollisionInfo = NamedTuple('CollisionInfo',
                           first=ICollisionable,
                           second=ICollisionable)


class BCollisionManager(ABC):

    @abstractmethod
    def add(self, obj: ICollisionable):
        pass

    @abstractmethod
    def remove(self, obj: ICollisionable):
        pass

    @abstractmethod
    def find_collisions(self) -> List[CollisionInfo]:
        pass

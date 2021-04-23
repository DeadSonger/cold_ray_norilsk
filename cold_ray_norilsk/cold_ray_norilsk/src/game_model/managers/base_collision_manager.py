from abc import ABC, abstractmethod
from typing import Type, List, NamedTuple, Tuple

from cold_ray_norilsk.src.game_model.mechanics.collision.i_collisionable import ICollisionable


CollisionInfo = NamedTuple('CollisionInfo',
                           first=Type[ICollisionable],
                           second=Type[ICollisionable],
                           intersection=List[Tuple[float, float]])


class BCollisionManager(ABC):

    @abstractmethod
    def add(self, obj: Type[ICollisionable]):
        pass

    @abstractmethod
    def find_collisions(self) -> List[CollisionInfo]:
        pass

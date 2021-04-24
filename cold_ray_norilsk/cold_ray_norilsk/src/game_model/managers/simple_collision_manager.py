from typing import List

from cold_ray_norilsk.src.game_model.managers.base_collision_manager import BCollisionManager
from cold_ray_norilsk.src.game_model.mechanics.collision.i_collisionable import (
    ICollisionable, CollisionInfo
)


class SimpleCollisionManager(BCollisionManager):

    def __init__(self):
        super.__init__()
        self.objects: List[ICollisionable] = list()

    def add(self, obj: ICollisionable):
        self.objects.append(obj)

    def remove(self, obj: ICollisionable):
        self.objects.remove(obj)

    def find_collisions(self) -> List[CollisionInfo]:
        collisions = list()
        for idx, obj in enumerate(self.objects):
            for other in self.objects[idx + 1:]:
                if obj.shape.intersect_with(other.shape):
                    collisions.append((obj, other))
        return collisions

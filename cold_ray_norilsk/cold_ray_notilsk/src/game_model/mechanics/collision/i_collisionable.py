from abc import ABC, abstractmethod
from typing import Type, List, Tuple

from cold_ray_notilsk.src.game_model.mechanics.collision.base_shape import BShape


class ICollisionable(ABC):

    @abstractmethod
    @property
    def shape(self) -> Type[BShape]:
        pass

    @abstractmethod
    def on_collision(self, other: Type['ICollisionable'], intersection: List[Tuple[float, float]]):
        pass

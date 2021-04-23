from abc import ABC, abstractmethod
from typing import Type

from cold_ray_norilsk.src.game_model.entity.base_entity import BEntity


class IInteractable(ABC):

    @abstractmethod
    @property
    def interact_distance(self) -> float:
        pass

    @abstractmethod
    def interact(self, interaction_type: int, by: Type[BEntity]):
        pass

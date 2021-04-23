from abc import ABC, abstractmethod
from typing import Type, List

from cold_ray_norilsk.src.game_model.mechanics.interaction.i_interactable import IInteractable


class BInteractionManager(ABC):

    @abstractmethod
    def add(self, obj: Type[IInteractable]):
        pass

    @abstractmethod
    def find_nearest(self, x: float, y: float) -> List[IInteractable]:
        pass

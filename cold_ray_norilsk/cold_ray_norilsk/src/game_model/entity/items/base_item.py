from abc import ABC, abstractmethod

from cold_ray_norilsk.src.game_model.entity.base_entity import BEntity


class BItem(BEntity, ABC):
    """Base abstract class of all items."""

    @abstractmethod
    def use(self):
        """Interact with item."""
        pass

from abc import ABC, abstractmethod

from cold_ray_norilsk.src.game_model.entity.base_entity import BEntity


class BItem(BEntity, ABC):

    @abstractmethod
    def use(self):
        pass

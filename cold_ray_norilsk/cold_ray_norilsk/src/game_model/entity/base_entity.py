from abc import ABC, abstractmethod


class BEntity(ABC):

    id_counter = 0

    def __init__(self):
        super().__init__()
        self._id = BEntity.id_counter
        BEntity.id_counter += 1

    @abstractmethod
    @property
    def type(self) -> str:
        pass

    @property
    def id(self) -> int:
        self._id

    @abstractmethod
    def tick(self, dt: float):
        pass

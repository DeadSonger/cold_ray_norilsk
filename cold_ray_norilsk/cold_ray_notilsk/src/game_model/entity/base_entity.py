from abc import ABC, abstractmethod


class BEntity(ABC):

    @abstractmethod
    @property
    def type(self) -> str:
        pass

    @abstractmethod
    @property
    def id(self) -> int:
        pass

    @abstractmethod
    def tick(self, dt: float):
        pass

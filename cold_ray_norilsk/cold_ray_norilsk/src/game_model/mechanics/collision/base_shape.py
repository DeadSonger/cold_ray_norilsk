from abc import ABC, abstractmethod
from typing import Type, Union, List, Tuple


class BShape(ABC):

    @abstractmethod
    @property
    def diameter(self) -> float:
        pass

    @abstractmethod
    def intersect_with(self, other: Type['BShape']) -> Union[None, List[Tuple[float, float]]]:
        pass

from abc import ABC, abstractmethod
from typing import Tuple


class BShape(ABC):

    __slots__ = ['x', 'y', 'angle']

    def __init__(self, x: float, y: float, angle: float = 0.0):
        super().__init__()
        self.x = x
        self.y = y
        self.angle = angle

    @property
    @abstractmethod
    def diameter(self) -> float:
        pass

    @abstractmethod
    def intersect_with(self, other: 'BShape') -> bool:
        pass

    def move(self, d_x: float, d_y: float) -> Tuple[float, float]:
        self.x += d_x
        self.y += d_y
        return (self.x, self.y)

    def move_to(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def rotate(self, angle: float) -> None:
        self.angle += angle

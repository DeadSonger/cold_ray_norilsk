from math import sqrt

from cold_ray_norilsk.src.game_model.mechanics.collision.base_shape import BShape
from cold_ray_norilsk.src.game_model.mechanics.collision.circle import Circle
from cold_ray_norilsk.src.game_model.mechanics.collision.helper import (
    do_polygons_intersect, rect_to_polygon, do_circle_intersect_polygon
)


class Rect(BShape):

    __slots__ = ['w', 'h']

    def __init__(self, x: float, y: float, w: float, h: float, angle: float = 0.0):
        super().__init__(x=x, y=y, angle=angle)
        self.w = w
        self.h = h

    @property
    def diameter(self) -> float:
        return sqrt(self.w**2 + self.h**2)

    def intersect_with(self, other: BShape) -> bool:
        d_x = self.x - other.x
        d_y = self.y - other.y
        if d_x ** 2 + d_y ** 2 > (self.r + other.diameter / 2) ** 2:
            return False
        if isinstance(other, Circle):
            return do_circle_intersect_polygon(
                (other.x, other.y),
                other.r,
                rect_to_polygon(self)
            )
        elif isinstance(other, Rect):
            return do_polygons_intersect(
                rect_to_polygon(self),
                rect_to_polygon(other)
            )
        assert False, f"Rect intersection with {type(other)} is not supported"

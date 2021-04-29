from cold_ray_norilsk.src.game_model.mechanics.collision.base_shape import BShape


class Circle(BShape):
    """Base circle shape."""

    __slots__ = ['r']

    def __init__(self, x: float, y: float, r: float, angle: float = 0.0):
        super().__init__(x=x, y=y, angle=angle)
        self.r = r

    @property
    def diameter(self) -> float:
        return self.r * 2

    def intersect_with(self, other: BShape) -> bool:
        from cold_ray_norilsk.src.game_model.mechanics.collision.rect import Rect
        from cold_ray_norilsk.src.game_model.mechanics.collision.helper import (
            rect_to_polygon, do_circle_intersect_polygon
        )
        d_x = self.x - other.x
        d_y = self.y - other.y
        if d_x ** 2 + d_y ** 2 > (self.r + other.diameter / 2) ** 2:
            return False
        if isinstance(other, Circle):
            return True
        elif isinstance(other, Rect):
            return do_circle_intersect_polygon(
                (self.x, self.y),
                self.r,
                rect_to_polygon(other)
            )
        assert False, f"Circle intersection with {type(other)} is not supported"

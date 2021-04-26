from cold_ray_norilsk.src.game_model.entity.objects.base_object import BObject
from cold_ray_norilsk.src.game_model.mechanics.collision.base_shape import BShape
from cold_ray_norilsk.src.game_model.mechanics.collision.circle import Circle
from cold_ray_norilsk.src.game_model.mechanics.collision.i_collisionable import ICollisionable


class Barrel(BObject, ICollisionable):

    def __init__(self, x: float, y: float, r: float, angle: float = 0.0):
        super().__init__(x=x, y=y)
        self._shape = Circle(x=x, y=y, r=r, angle=angle)

    def tick(self, dt: float):
        super().tick(dt)
        self._shape.x = self.x_pos
        self._shape.y = self.y_pos

    def on_collision(self, _: ICollisionable):
        pass

    @property
    def shape(self) -> BShape:
        return self._shape

    @property
    def type(self) -> str:
        return "Barrel"

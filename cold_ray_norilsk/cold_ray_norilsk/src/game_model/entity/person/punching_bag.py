from cold_ray_norilsk.src.game_model.entity.person.base_person import BPerson
from cold_ray_norilsk.src.game_model.mechanics.collision.base_shape import BShape
from cold_ray_norilsk.src.game_model.mechanics.collision.circle import Circle
from cold_ray_norilsk.src.game_model.mechanics.collision.i_collisionable import ICollisionable


class PunchingBag(BPerson, Circle, ICollisionable):

    def __init__(self, x: float = 0.0, y: float = 0.0, health: float = 100.0):
        super().__init__(x, y, health)

    @property
    def x(self) -> float:
        return self.x_pos

    @x.setter
    def x(self, value):
        self.x_pos = value

    @property
    def y(self) -> float:
        return self.y_pos

    @y.setter
    def y(self, value):
        self.y_pos = value

    @property
    def r(self) -> float:
        return 10.0

    def tick(self, dt: float):
        self.health += 10.0 * dt
        self.health = max(self.health, 100.0)

    def on_collision(self, _: ICollisionable):
        pass

    @property
    def shape(self) -> BShape:
        return self

    @property
    def type(self) -> str:
        return "PunchingBag"

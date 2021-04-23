from abc import ABC
from typing import Type

from cold_ray_norilsk.src.graphics.base_tile import BTile
from cold_ray_norilsk.src.graphics.base_texture import BTexture


class BAnimatedTile(BTile, ABC):

    def change_texture(self, new_texture: Type[BTexture]):
        self.texture = new_texture

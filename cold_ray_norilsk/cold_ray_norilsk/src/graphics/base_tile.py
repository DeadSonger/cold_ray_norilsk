from abc import ABC
from typing import Type

from cold_ray_norilsk.src.graphics.i_drawable import IDrawable
from cold_ray_norilsk.src.graphics.base_texture import BTexture


class BTile(IDrawable, ABC):

    __slots__ = [
        'texture',
        'x',
        'y',
        'width',
        'height'
    ]

    def __init__(self, texture: Type[BTexture],
                 x: float, y: float,
                 width: float, height: float):
        self.texture = texture
        self.x = x
        self.y = y
        self.width = width
        self.height = height

from cold_ray_norilsk.src.game_model.mechanics.collision.circle import Circle
from cold_ray_norilsk.src.game_model.mechanics.collision.rect import Rect


def test_circle_rect_collision():
    test_rect = Rect(0, 0, 1, 1)

    test_circle_1 = Circle(0, 0, 2)
    assert test_circle_1.intersect_with(test_rect)

    test_circle_2 = Circle(0, 0, 0.5)
    assert test_circle_2.intersect_with(test_rect)

    test_circle_3 = Circle(2, 2, 1)
    assert not test_circle_3.intersect_with(test_rect)

    test_circle_4 = Circle(2.4230769230769, 0, 3.948224852071)
    assert test_circle_4.intersect_with(test_rect)

    test_circle_5 = Circle(-1, 0.8, 0.34)
    assert test_circle_5.intersect_with(test_rect)

    test_circle_6 = Circle(-1, 0.8, 0.32)
    assert not test_circle_6.intersect_with(test_rect)


def rect_circle_collision():
    test_circle = Circle(0, 0, 1)

    test_rect_1 = Rect(0.85, 0, 1, 0.8)
    assert test_rect_1.intersect_with(test_circle)

    test_rect_2 = Rect(1, 1, 0.8, 0.4)
    assert test_rect_2.intersect_with(test_circle)

    test_rect_3 = Rect(-1.1, 0, 0.6, 1.2)
    assert test_rect_3.intersect_with(test_circle)

    test_rect_4 = Rect(1, 1, 0.7, 0.4)
    assert not test_rect_4.intersect_with(test_circle)

    test_rect_5 = Rect(1, 1, 0.8, 0.3)
    assert not test_rect_5.intersect_with(test_circle)

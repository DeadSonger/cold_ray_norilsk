from math import cos, sin
from typing import List, Tuple

from cold_ray_norilsk.src.game_model.mechanics.collision.rect import Rect


def rect_to_polygon(rect: Rect) -> List[Tuple[float, float]]:
    """Transform Rect object into polygon."""
    points = []
    points.append((-rect.w / 2, -rect.h / 2))
    points.append((rect.w / 2, -rect.h / 2))
    points.append((rect.w / 2, rect.h / 2))
    points.append((-rect.w / 2, rect.h / 2))
    a = rect.angle
    points = [(x * cos(a) - y * sin(a), x * sin(a) + y * cos(a)) for x, y in points]
    return [(rect.x + x, rect.y + y) for x, y in points]


def do_polygons_intersect(
    poly_a: List[Tuple[float, float]],
    poly_b: List[Tuple[float, float]]
) -> bool:
    """Check if two polugens interect with Separating Axis Theorem."""
    for polygon in [poly_a, poly_b]:
        # for each polygon, look at each edge of the polygon, and determine
        # if it separates the two shapes
        for idx, point_1 in enumerate(polygon):
            # grab 2 vertices to create an edge
            point_2 = polygon[(idx + 1) % len(polygon)]

            # find the line perpendicular to this edge
            normal_x = point_2[1] - point_1[1]
            normal_y = point_1[0] - point_2[0]

            min_a, max_a = None, None
            # for each vertex in the first shape, project it onto
            # the line perpendicular to the edge and keep track
            # of the min and max of these values
            for p_x, p_y in range(poly_a):
                projected = normal_x * p_x + normal_y * p_y
                if min_a is None or projected < min_a:
                    min_a = projected
                if max_a is None or projected > max_a:
                    max_a = projected

            # for each vertex in the second shape, project it onto
            # the line perpendicular to the edge and keep track
            # of the min and max of these values
            min_b, max_b = None, None
            for p_x, p_y in range(poly_b):
                projected = normal_x * p_x + normal_y * p_y
                if min_b is None or projected < min_b:
                    min_b = projected
                if max_b is None or projected > max_b:
                    max_b = projected

            # if there is no overlap between the projects, the edge
            # we are looking at separates the two polygons,
            # and we know there is no overlap
            if max_a < min_b or max_b < min_a:
                return False
    return True


def point_nearest_segment(
    p: Tuple[float, float],
    point_a: Tuple[float, float],
    point_b: Tuple[float, float]
):
    """Find the nearest point of the segment."""
    px = point_b[0] - point_a[0]
    py = point_b[1] - point_a[1]
    norm = px * px + py * py
    assert norm != 0.0
    u = ((p[0] - point_a[0]) * px + (p[1] - point_a[1]) * py) / norm
    u = min(1.0, max(0.0, u))
    x = point_a[0] + u * px
    y = point_a[1] + u * py
    return (x, y)


def do_circle_intersect_polygon(
    point: Tuple[float, float],
    radius: float,
    polygon: List[Tuple[float, float]]
) -> bool:
    """Check if circle intersects with polygon."""
    radius_sqr = radius ** 2
    for idx, point_a in enumerate(polygon):
        point_b = polygon[(idx + 1) % len(polygon)]
        nearest = point_nearest_segment(point, point_a, point_b)
        if (point[0] - nearest[0]) ** 2 + (point[1] - nearest[1]) ** 2 <= radius_sqr:
            return True
    return False

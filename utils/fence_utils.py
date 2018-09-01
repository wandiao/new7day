# -*- coding: utf-8 -*-
import json
import math
import utm
from collections import namedtuple


class LocationsTooLittle(ValueError):
    pass


class JsonMixin():
    @property
    def json(self):
        return json.dumps(self.serializable_representation)


Point = namedtuple("Point", ["x", "y"])


class Location(JsonMixin):
    """Location class"""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.easting, self.northing, self.zone_number, self.zone_letter = (
            utm.from_latlon(self.latitude, self.longitude)
        )

    @property
    def x(self):
        return self.longitude

    @property
    def y(self):
        return self.latitude

    @property
    def serializable_representation(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    @classmethod
    def from_json_string(cls, string):
        container = json.loads(string)
        assert isinstance(container, dict)
        return cls(**container)

    def __eq__(self, another):
        if (self.latitude == another.latitude
                and self.longitude == another.longitude):
            return True
        return False

    def __repr__(self):
        return "Location(latitude={latitude}, longitude={longitude})".format(
            latitude=self.latitude, longitude=self.longitude
        )

    __str__ = __repr__


class Line():
    """Line class"""

    def __init__(self, endpoint_a, endpoint_b):
        """
        Init a line segments with endpoint_a and endpoint_b

        :param endpoint_a: one endpoint of line
        :type endpoint_a: Location
        :param endpoint_b: another endpoint of line
        :type endpoint_b: Location
        """
        self.endpoint_a = endpoint_a
        self.endpoint_b = endpoint_b

    @property
    def length(self):
        """
        Return length(meter) of the line

        :return: length(meter) of the line
        :rtype: float
        """
        return math.sqrt(
            (self.endpoint_a.northing - self.endpoint_b.northing) ** 2 +
            (self.endpoint_a.easting - self.endpoint_b.easting) ** 2
        )

    def __repr__(self):
        return "Line({a}, {b})".format(
            a=self.endpoint_a, b=self.endpoint_b
        )

    __str__ = __repr__


class Polyline():
    """Polyline class"""

    def __init__(self, locations):
        """
        Init a polyline with locations

        :param locations: locations of ployline
        :type locations: list[Location]
        """
        if len(locations) < 2:
            raise LocationsTooLittle("Requires three or more vertices to form "
                                     "a polygon")
        self.locations = locations

    @property
    def length(self):
        """
        Calculate total length of the polyline

        :return: total length in meters
        :rtype: float
        """
        total_length = 0
        for location_a, location_b in zip(
                self.locations[:-1], self.locations[1:]):
            total_length += Line(location_a, location_b).length
        return total_length

    def __repr__(self):
        return "Polyline({})".format(self.points)

    __str__ = __repr__


class Region(JsonMixin):
    """Region class"""

    def __init__(self, vertices):
        """
        Init a region with vertices

        :param vertices: vertices of region
        :type vertices: list[Location]
        """
        if len(vertices) < 3:
            raise LocationsTooLittle("Requires three or more vertices to form "
                                     "a polygon")
        self.vertices = vertices

    def __contains__(self, location):
        assert isinstance(location, Location)
        return is_inside(location, self)

    @property
    def serializable_representation(self):
        return [l.serializable_representation for l in self.vertices]

    @classmethod
    def from_json_string(cls, string):
        container = json.loads(string)
        assert isinstance(container, list)
        vertices = [Location(**location) for location in container]
        return cls(vertices)

    def __eq__(self, another):
        if self.vertices == another.vertices:
            return True
        return False

    def __repr__(self):
        return "Region({})".format(self.vertices)

    __str__ = __repr__


def on_segment(point_p, point_q, point_r):
    """
    Given three colinear points p, q, r, the function checks if point q
    lies on line segment "pr"

    :param point_p:
    :type point_p: models.Point
    :param point_q:
    :type point_q: models.Point
    :param point_r:
    :type point_r: models.Point
    :return: if point r on line segment "pr"
    :rtype: bool
    """
    if (point_q.x <= max(point_p.x, point_r.x)
            and point_q.x >= min(point_p.x, point_r.x)
            and point_q.y <= max(point_p.y, point_r.y)
            and point_q.y >= min(point_p.y, point_r.y)):
        return True
    return False


def orientation(point_p, point_q, point_r):
    """
    To find orientation of ordered triplet (p, q, r).

    :param point_p:
    :type point_p: models.Point
    :param point_q:
    :type point_q: models.Point
    :param point_r:
    :type point_r: models.Point
    :return: 0: p, q and r are colinear
             1: clockwise
             2: counterclockwise
    :rtype: int
    """
    # Set https://www.geeksforgeeks.org/orientation-3-ordered-points/
    # for details of below formula.
    r = ((point_q.y - point_p.y) * (point_r.x - point_q.x) -
         (point_q.x - point_p.x) * (point_r.y - point_q.y))
    if r == 0:
        return 0
    return 1 if r > 0 else 2


def is_intersect(line_a, line_b):
    """
    Determine if lina_a intersect with line_b

    :param lina_a:
    :type lina_a: models.Line
    :param lina_b:
    :type line_b: models.Line
    :return:
    :rtype: bool
    """
    # Find the four orientations needed for general and special cases
    orientation_1 = orientation(line_a.endpoint_a, line_a.endpoint_b,
                                line_b.endpoint_a)
    orientation_2 = orientation(line_a.endpoint_a, line_a.endpoint_b,
                                line_b.endpoint_b)
    orientation_3 = orientation(line_b.endpoint_a, line_b.endpoint_b,
                                line_a.endpoint_a)
    orientation_4 = orientation(line_b.endpoint_a, line_b.endpoint_b,
                                line_a.endpoint_b)

    # General case
    if (orientation_1 != orientation_2 and orientation_3 != orientation_4):
        return True

    # Special cases
    if (orientation_1 == 0 and on_segment(line_a.endpoint_a, line_b.endpoint_a,
                                          line_a.endpoint_b)):
        return True
    if (orientation_2 == 0 and on_segment(line_a.endpoint_a, line_b.endpoint_b,
                                          line_a.endpoint_b)):
        return True
    if (orientation_3 == 0 and on_segment(line_b.endpoint_a, line_a.endpoint_a,
                                          line_b.endpoint_b)):
        return True
    if (orientation_4 == 0 and on_segment(line_b.endpoint_a, line_a.endpoint_b,
                                          line_b.endpoint_b)):
        return True

    return False


def is_inside(point, region):
    """
    Detemine if point is in region

    :param point:
    :type point: models.Point
    :param region:
    :type region: Region
    """
    points = region.vertices
    extrame = Point(x=1000000, y=point.y)

    points = points + [points[0]]
    intersect_count = 0
    for i in range(len(points) - 1):
        if is_intersect(Line(point, extrame),
                        Line(points[i], points[i+1])):
            intersect_count += 1
    return intersect_count % 2 == 1


if __name__ == "__main__":
    pass

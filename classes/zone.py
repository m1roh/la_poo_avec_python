from .position import Position


class Zone:

    EARTH_RADIUS_KILOMETERS = 6371
    HEIGHT_DEGREES = 1
    MAX_LATITUDE_DEGREES = 90
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MIN_LONGITUDE_DEGREES = -180
    WIDTH_DEGREES = 1
    ZONES = []

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []

    @classmethod
    def _initialize(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)

    @classmethod
    def find_zone_that_contains(cls, position):
        if not cls.ZONES:
            # Initialize zones automatically if necessary
            cls._initialize()

        # Compute the index in the ZONES array that contains the given position
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES) / cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        zone_index = latitude_index * longitude_bins + longitude_index

        # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone

    @property
    def population(self):
        return len(self.inhabitants)

    @property
    def width(self):
        return abs((self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS)

    @property
    def height(self):
        return abs((self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS)

    @property
    def area(self):
        # Compute the zone area, in square kilometers
        return self.height * self.width

    def population_density(self):
        # Population density of the zone, (people / km2)
        return self.population / self.area

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(self.corner1.latitude, self.corner2.latitude)

    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants])

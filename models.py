"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional),
    diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name, diameter, hazardous):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the
        constructor.
        """
        self.designation = str(designation)

        self.name = str(name)
        if name == '':
            self.name = None

        # self.diameter = float('nan')
        if diameter == '':
            self.diameter = float('nan')
        else:
            self.diameter = float(diameter)

        self.hazardous = bool(hazardous)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name is None:
            return f'{self.designation}'
        else:
            return f'{self.designation} ({self.name})'

    def __str__(self):
        """Return `str(self)`."""
        hazard = ''
        if self.hazardous is False:
            hazard = 'not potentially hazardous'
        if self.hazardous is not False:
            hazard = 'potentially hazardous'
        return (f"NEO {self.fullname} has a diameter of"
                f"{self.diameter} km and is {hazard}")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable
        string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r},"
                f"name={self.name!r}, "
                f"diameter={self.diameter:.3f},"
                f"hazardous={self.hazardous!r})")

    @property
    def serialize(self):
        """Return a dictionary containing relevant
        attributes for CSV or JSON serialization."""
        dictionary = {'designation': self.designation, 'name': self.name,
                      'diameter_km': self.diameter, 'potentially_hazardous':
                      self.hazardous}

        return dictionary


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about
    the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest
    approach, the nominal
    approach distance in astronomical units, and the
    relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, _designation, time, distance, velocity):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments
        supplied to the constructor.
        """
        self._designation = str(_designation)
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this
        `CloseApproach`'s approach time.

        The value in `self.time` should be a Python
        `datetime` object. While a
        `datetime` object has a string representation,
        the default representation
        includes seconds - significant figures that don't
        exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime`
        object to a
        formatted string that can be used in human-readable
        representations and
        in serialization to CSV and JSON files.
        """
        time = datetime_to_str(self.time)
        return f'{time}'

    def __str__(self):
        """Return `str(self)`."""
        return (f"On {self.time_str} {self.neo.fullname} approaches Earth"
                f"at a distance of {self.distance} au and a velocity of"
                f"{self.velocity} km/s.")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable
        string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r},"
                f"distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    @property
    def serialize(self):
        """Return a dictionary containing relevant
        attributes for CSV or JSON serialization."""
        dictionary = {'datetime_utc': datetime_to_str(self.time),
                      'distance_au': self.distance,
                      'velocity_km_s': self.velocity}

        return dictionary

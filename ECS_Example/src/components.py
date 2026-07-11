from dataclasses import dataclass

@dataclass
class Position:
    x: float
    y: float

@dataclass
class Velocity:
    x: float
    y: float

@dataclass
class BoidMarker:
    """An empty component to label an entity as a boid."""
    pass

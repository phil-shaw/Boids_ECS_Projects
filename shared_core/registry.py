class ECSRegistry:
    def __init__(self):
        self._next_id = 0
        # Storage pools for components
        self.positions = {}
        self.velocities = {}
        self.boids = {}

    def create_entity(self) -> int:
        entity_id = self._next_id
        self._next_id += 1
        return entity_id

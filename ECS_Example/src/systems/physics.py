from shared_core.registry import ECSRegistry

def flocking_logic_system(registry: ECSRegistry):
    """
    This is where Craig Reynolds' rules live.
    It reads all positions and velocities, calculates steering forces,
    and updates an entity's acceleration data.
    """
    for entity_id in registry.boids:
        pos = registry.positions[entity_id]
        vel = registry.velocities[entity_id]

        # 1. Look at all *other* boids in the registry
        # 2. Calculate separation, alignment, and cohesion vectors
        # 3. Apply those forces to an Acceleration component
        pass


def movement_system(registry: ECSRegistry, dt: float):
    """Updates position components based on velocity, and velocity based on acceleration."""
    for entity_id, pos in registry.positions.items():
        if entity_id in registry.velocities:
            vel = registry.velocities[entity_id]

            # (Optional) If you add an Acceleration component later:
            # vel.x += acc.x * dt
            # vel.y += acc.y * dt

            # Frame-rate independent movement
            pos.x += vel.x * dt
            pos.y += vel.y * dt

            # Basic screen wrap-around boundary logic so they don't fly away forever
            if pos.x < 0:
                pos.x = 800
            elif pos.x > 800:
                pos.x = 0
            if pos.y < 0:
                pos.y = 600
            elif pos.y > 600:
                pos.y = 0

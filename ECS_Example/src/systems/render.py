import pygame
from shared_core.registry import ECSRegistry


def render_system(screen: pygame.Surface, registry: ECSRegistry):
    """Draws entities onto the screen canvas."""
    for entity_id, pos in registry.positions.items():
        # Check if the entity is categorized as a boid
        if entity_id in registry.boids:
            # Draw a simple circle for the boid placeholder
            pygame.draw.circle(screen, (139, 0, 0), (pos.x, pos.y), 5)
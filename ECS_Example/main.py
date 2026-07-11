from doctest import Example

import pygame
import random
from shared_core.registry import ECSRegistry
from ECS_Example.src.components import Position, Velocity, BoidMarker
from ECS_Example.src.systems.physics import movement_system
from ECS_Example.src.systems.render import render_system


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Initialize our central data storage
    registry = ECSRegistry()

    for _ in range(100):
        entity = registry.create_entity()

        # Spawn randomly across the screen space
        random_x = random.uniform(50.0, 750.0)
        random_y = random.uniform(50.0, 550.0)
        registry.positions[entity] = Position(random_x, random_y)

        # Give each boid a unique starting velocity direction
        random_vx = random.uniform(-100.0, 100.0)
        random_vy = random.uniform(-100.0, 100.0)
        registry.velocities[entity] = Velocity(random_vx, random_vy)

        registry.boids[entity] = BoidMarker()

    running = True
    while running:
        # Tick the clock (returns milliseconds since last frame, convert to seconds)
        dt = clock.tick(60) / 1000.0

        # 1. Handle Input (The Controller role)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Run Logic Systems (The Model update)
        movement_system(registry, dt)

        # 3. Run Graphic Systems (The View rendering)
        screen.fill((245, 245, 245))  # Clean background
        render_system(screen, registry)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

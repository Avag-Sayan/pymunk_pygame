import pygame
from pygame.locals import QUIT
import pymunk
import pymunk.pygame_util

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ֆիզիկայի անիմացիա")

# Set up Pygame clock
clock = pygame.time.Clock()

# Create a pymunk space
space = pymunk.Space()
space.gravity = (0, 600)  # Set gravity

# Create a static ground segment
ground = pymunk.Segment(space.static_body, (0, height - 20), (width, height - 20), 1)
ground.friction = 1.0
space.add(ground)

# Create a dynamic ball
mass = 1
radius = 20
moment = pymunk.moment_for_circle(mass, 0, radius)
ball_body = pymunk.Body(mass, moment)
ball_shape = pymunk.Circle(ball_body, radius)
ball_body.position = width // 2, height // 2
space.add(ball_body, ball_shape)

# Pygame drawing functions for Pymunk objects
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update physics
    space.step(1 / 60.0)

    # Draw everything
    screen.fill((255, 255, 255))
    space.debug_draw(draw_options)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()

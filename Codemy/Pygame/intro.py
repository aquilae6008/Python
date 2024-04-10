import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Pygame Intro')
clock = pygame.time.Clock()
running = True

dt: float = 0
player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # Pull Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen Color
    screen.fill("Gold")

    # Render
    pygame.draw.circle(screen, "Red", player_position, 45)

    # Controls
    keys = pygame.key.get_pressed()

    # Up and Down Control
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_position.y -= 300 * dt
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_position.y += 300 * dt

    # Right and Left Control
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_position.x -= 300 * dt
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_position.x += 300 * dt

    # End Control
    if keys[pygame.K_ESCAPE]:
        running = False

    # Display Flip to Render
    pygame.display.flip()

    # Set clock
    dt = clock.tick(60) / 1000

pygame.quit()

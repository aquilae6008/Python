import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Pygame Mouse')
clock = pygame.time.Clock()
running = True

dt: float = 0
player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    global position_up, position_down
    # Pull Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen Color
    screen.fill("Gold")

    # Render
    pygame.draw.circle(screen, "black", player_position, 5)

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

    # Mouse Control
    if event.type == pygame.MOUSEBUTTONDOWN:
        position = pygame.mouse.get_pos()
        button = pygame.mouse.get_pressed()
        if button[0]:
            player_position.x = position[0]
            player_position.y = position[1]
        elif button[2]:
            pygame.draw.circle(screen, "Red", player_position, 65)

    if pygame.mouse.get_pressed()[0]:
        position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            player_position.x = position[0]
            player_position.y = position[1]

    if event.type == pygame.MOUSEBUTTONUP:
        position = pygame.mouse.get_pos()
        button = pygame.mouse.get_pressed()[0]
        if button:
            player_position.x = position[0]
            player_position.y = position[1]

    pygame.draw.rect(screen, color="Grey", rect=(265, 135, 270, 235), border_radius=30)
    pygame.draw.line(screen, color='Blue', start_pos=(400 - 90, 250 + 90), end_pos=(400 + 90, 250 - 90), width=5)
    pygame.draw.line(screen, color='Blue', start_pos=(400 + 90, 250 - 90), end_pos=(400 + 90 - 200, 250 - 90), width=3)
    pygame.draw.line(screen, color='Blue', start_pos=(400 + 90 - 200, 250 - 90), end_pos=(400 - 75, 250), width=3)
    pygame.draw.line(screen, color='Blue', start_pos=(400 - 90 + 200, 250 + 90), end_pos=(400 - 90, 250 + 90), width=3)
    pygame.draw.line(screen, color='Blue', start_pos=(400 - 90 + 200, 250 + 90), end_pos=(400 + 75, 250), width=3)
    pygame.draw.circle(screen, color='Black', center=(400, 250), radius=75, width=10, draw_top_right=True,
                       draw_bottom_left=True)
    pygame.draw.circle(screen, color='green', center=(400, 250), radius=75, width=5, draw_top_left=True,
                       draw_bottom_right=True)

    # if event.type == pygame.MOUSEMOTION:
    #     position = pygame.mouse.get_pos()
    #     player_position.x = position[0]
    #     player_position.y = position[1]

    # Display Flip to Render
    pygame.display.flip()

    # Set clock
    dt = clock.tick(60) / 1000

pygame.quit()

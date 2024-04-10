import pygame

# Initialize Pygame
pygame.init()
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 500
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Pygame Mouse')
clock = pygame.time.Clock()
running = True

dt: float = 0
player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
eagle = pygame.image.load("assets/eagle.png")
hyena = pygame.image.load("assets/hyena.png")

# Image entities
eagle_entity = eagle.get_rect()
hyena_entity = hyena.get_rect()
hyena_entity.topright = (800, 0)

# Position Entities


while running:
    global position_up, position_down
    # Pull Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen Color
    screen.fill("Gold")

    # Render
    screen.blit(eagle, eagle_entity)
    screen.blit(hyena, hyena_entity)

    # Controls
    keys = pygame.key.get_pressed()

    # Up and Down Control - Eagle
    if keys[pygame.K_w]:
        eagle_entity.y -= 300 * dt
    elif keys[pygame.K_s]:
        eagle_entity.y += 300 * dt

    # Right and Left Control - Eagle
    if keys[pygame.K_a]:
        eagle_entity.x -= 300 * dt
    elif keys[pygame.K_d]:
        eagle_entity.x += 300 * dt

    # Up amd Down Control - Hyena
    if keys[pygame.K_UP]:
        hyena_entity.y -= 300 * dt
    elif keys[pygame.K_DOWN]:
        hyena_entity.y += 300 * dt

    # Right and Left Control - Hyena
    if keys[pygame.K_LEFT]:
        hyena_entity.x -= 300 * dt
    elif keys[pygame.K_RIGHT]:
        hyena_entity.x += 300 * dt

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

    # if event.type == pygame.MOUSEMOTION:
    #     position = pygame.mouse.get_pos()
    #     player_position.x = position[0]
    #     player_position.y = position[1]

    # Display Flip to Render
    pygame.display.flip()

    # Set clock
    dt = clock.tick(60) / 1000

pygame.quit()

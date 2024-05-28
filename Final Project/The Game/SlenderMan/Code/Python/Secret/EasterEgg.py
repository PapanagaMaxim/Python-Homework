import pygame
import os
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Set fullscreen mode
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Slenderman Game")

# Load images
current_path = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
image_path = os.path.join(current_path, 'Slenderman', 'Images')

player_image = pygame.image.load(os.path.join(image_path, 'Player', 'PlayerIdle.gif')).convert_alpha()
background_image = pygame.image.load(os.path.join(image_path, 'EasterEgg', 'Sigmoid.jpg')).convert()

# Resize background image to 50x50 pixels
background_tile = pygame.transform.scale(background_image, (50, 50))

# Set up game variables
min_distance = 400
player_x = random.randint(0, screen_width)
player_y = random.randint(0, screen_height)
player_speed = 5

cake_image = pygame.image.load(os.path.join(image_path, 'EasterEgg', 'Cake.png')).convert_alpha()
cake_x = random.randint(0, screen_width)
cake_y = random.randint(0, screen_height)
cake_rect = cake_image.get_rect(topleft=(cake_x, cake_y))

while True:
    player_x = random.randint(0, screen_width)
    player_y = random.randint(0, screen_height)
    cake_x = random.randint(0, screen_width)
    cake_y = random.randint(0, screen_height)
    distance = math.sqrt((player_x - cake_x)**2 + (player_y - cake_y)**2)
    if distance >= min_distance:
        break

cake_rect = cake_image.get_rect(topleft=(cake_x, cake_y))

# Set up font for text
font_path = os.path.join(image_path, 'Menu', 'font.ttf')
font = pygame.font.Font(font_path, 30)

clock = pygame.time.Clock()
running = True

color_timer = 0
current_color = (255, 255, 255)

# Confetti effect variables
confetti_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
confetti_particles = []
confetti_spawn_rate = 30  # Number of confetti particles spawned per second
confetti_speed = 5

show_text = False

# Function to calculate angle between two points
def angle_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    angle = math.atan2(y2 - y1, x2 - x1)
    return math.degrees(angle)

# Main game loop
while running:
    # Reset the camera position to center on the player
    camera_x = player_x - screen_width // 2 + player_image.get_width() // 2
    camera_y = player_y - screen_height // 2 + player_image.get_height() // 2

    # Fill the background with tiles
    for y in range(-50, screen_height + 50, 50):
        for x in range(-50, screen_width + 50, 50):
            screen.blit(background_tile, (x - camera_x % 50, y - camera_y % 50))

    # Calculate angle between player and cake
    angle_to_cake = angle_between_points((player_x, player_y), (cake_x, cake_y))

    # Draw the player at the center of the screen
    screen.blit(player_image, (screen_width // 2 - player_image.get_width() // 2, screen_height // 2 - player_image.get_height() // 2))

    # Draw arrow pointing towards cake with rotation
    arrow_image = pygame.Surface((40, 20), pygame.SRCALPHA)
    pygame.draw.polygon(arrow_image, (255, 0, 0), [(0, 0), (40, 10), (0, 20)])
    arrow_image_rotated = pygame.transform.rotate(arrow_image, -angle_to_cake)
    screen.blit(arrow_image_rotated, (screen_width // 2 - arrow_image_rotated.get_width() // 2, screen_height // 2 + player_image.get_height() // 2))

    # Draw spinning text in the center if the cake is clicked
    if show_text:
        text_surface = font.render("Sigmoid THE BEST!!!111!!!", True, current_color)
        text_rect = text_surface.get_rect(center=(cake_x - camera_x, cake_y - camera_y))
        screen.blit(text_surface, text_rect)

    # Draw Minecraft cake relative to camera
    screen.blit(cake_image, (cake_x - camera_x, cake_y - camera_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cake_rect.collidepoint(event.pos[0] + camera_x, event.pos[1] + camera_y):  # Check if cake is clicked
                show_text = True
                for _ in range(20):  # Spawn confetti particles
                    x = random.randint(0, screen_width)
                    y = random.randint(0, screen_height // 2)
                    color = random.choice(confetti_colors)
                    confetti_particles.append([x, y, color])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Update and draw confetti particles
    for particle in confetti_particles:
        particle[1] += confetti_speed
        pygame.draw.circle(screen, particle[2], (particle[0], particle[1]), 5)
        if particle[1] > screen_height:
            confetti_particles.remove(particle)

    # Change text color every 0.5 seconds
    color_timer += clock.get_time()
    if color_timer >= 500:
        color_timer = 0
        current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Update cake rect for collision detection
    cake_rect.topleft = (cake_x, cake_y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
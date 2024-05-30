import pygame
import os
import random
import math
import subprocess

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Set fullscreen mode
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Slenderman Game")

# Load music
music_path = 'SlenderMan/Sfx/EasterEgg/Happy.mp3'
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)

# Load images
player_image = pygame.image.load('SlenderMan/Images/Player/PlayerIdle01.png')
player_image = pygame.transform.scale(player_image, (200, 200))
background_image = pygame.image.load('SlenderMan/Images/EasterEgg/Sigmoid.jpg')
background_tile = pygame.transform.scale(background_image, (50, 50))
cake_image = pygame.image.load('SlenderMan/Images/EasterEgg/Cake.png')

# Set up game variables
min_distance = 400
player_speed = 5

def get_random_position():
    return random.randint(0, screen_width), random.randint(0, screen_height)

player_x, player_y = get_random_position()
cake_x, cake_y = get_random_position()

while math.sqrt((player_x - cake_x)**2 + (player_y - cake_y)**2) < min_distance:
    player_x, player_y = get_random_position()
    cake_x, cake_y = get_random_position()

cake_rect = cake_image.get_rect(topleft=(cake_x, cake_y))

# Set up font for text and button
font_path = os.path.join('SlenderMan/Images/Menu/font.ttf')
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

# Define the "X" button
button_text = "X"
button_color = (255, 0, 0)
button_font = pygame.font.Font(font_path, 40)
button_surface = button_font.render(button_text, True, button_color)
button_rect = button_surface.get_rect()
button_rect.topright = (screen_width - 10, 10)

def angle_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    angle = math.atan2(y2 - y1, x2 - x1)
    return math.degrees(angle)

def draw_background(camera_x, camera_y):
    for y in range(-50, screen_height + 50, 50):
        for x in range(-50, screen_width + 50, 50):
            screen.blit(background_tile, (x - camera_x % 50, y - camera_y % 50))

def spawn_confetti():
    for _ in range(20):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height // 2)
        color = random.choice(confetti_colors)
        confetti_particles.append([x, y, color])

# Main game loop
while running:
    camera_x = player_x - screen_width // 2 + player_image.get_width() // 2
    camera_y = player_y - screen_height // 2 + player_image.get_height() // 2

    draw_background(camera_x, camera_y)

    angle_to_cake = angle_between_points((player_x, player_y), (cake_x, cake_y))

    screen.blit(player_image, (screen_width // 2 - player_image.get_width() // 2, screen_height // 2 - player_image.get_height() // 2))

    arrow_image = pygame.Surface((40, 20), pygame.SRCALPHA)
    pygame.draw.polygon(arrow_image, (255, 0, 0), [(0, 0), (40, 10), (0, 20)])
    arrow_image_rotated = pygame.transform.rotate(arrow_image, -angle_to_cake)
    screen.blit(arrow_image_rotated, (screen_width // 2 - arrow_image_rotated.get_width() // 2, screen_height // 2 + player_image.get_height() // 2))

    if show_text:
        text_surface = font.render("Sigmoid THE BEST!!!111!!!", True, current_color)
        text_rect = text_surface.get_rect(midbottom=(cake_x - camera_x + cake_rect.width // 2, cake_y - camera_y))
        screen.blit(text_surface, text_rect)

    screen.blit(cake_image, (cake_x - camera_x, cake_y - camera_y))

    screen.blit(button_surface, button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cake_rect.collidepoint(event.pos[0] + camera_x, event.pos[1] + camera_y):
                show_text = True
                spawn_confetti()
            elif button_rect.collidepoint(event.pos):
                pygame.quit()
                subprocess.Popen(["python", "SlenderMan/Code/Python/Menu/Menu.py"])
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    for particle in confetti_particles[:]:
        particle[1] += confetti_speed
        pygame.draw.circle(screen, particle[2], (particle[0], particle[1]), 5)
        if particle[1] > screen_height:
            confetti_particles.remove(particle)

    color_timer += clock.get_time()
    if color_timer >= 500:
        color_timer = 0
        current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
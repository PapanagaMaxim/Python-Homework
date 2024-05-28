import pygame
import sys
import os
import subprocess
import math
import random

# Initialize Pygame
pygame.init()

# Set up the screen in fullscreen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Level Hard")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BUTTON_COLOR = (196, 12, 12)  # Hex #C40C0C converted to RGB

# Get screen dimensions
screen_width, screen_height = screen.get_size()

# Player attributes
player_width = 50
player_height = 50
player_speed = 5

# Player rect
player_rect = pygame.Rect(
    (screen_width - player_width) // 2,
    (screen_height - player_height) // 2,
    player_width,
    player_height
)

# Load font for the "EXIT" button
font_path = os.path.join("SlenderMan", "Images", "Menu", "font.ttf")
if not os.path.exists(font_path):
    print(f"Font file not found at {font_path}, using default font.")
    font = pygame.font.Font(None, 36)
else:
    font = pygame.font.Font(font_path, 36)

# Slenderman attributes for animation
slenderman_radius = 20
slenderman_color = WHITE
slenderman_x = screen_width // 4
slenderman_y = screen_height // 4
slenderman_speed = 2

# Movement for Slenderman
waypoint = None
last_known_player_pos = None
change_waypoint_time = 0
stop_duration = 1000  # Stop for 1 second at each waypoint
is_stopping = False

# Flag to control the visibility of the "EXIT" button
show_exit_button = False

def draw_player(screen, player_rect):
    pygame.draw.rect(screen, RED, player_rect)

def generate_waypoint(center_x, center_y, radius):
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(0, radius)
    waypoint_x = center_x + distance * math.cos(angle)
    waypoint_y = center_y + distance * math.sin(angle)
    return waypoint_x, waypoint_y

def move_slenderman_towards_waypoint():
    global slenderman_x, slenderman_y, waypoint, is_stopping, change_waypoint_time
    
    if waypoint:
        distance = math.hypot(waypoint[0] - slenderman_x, waypoint[1] - slenderman_y)
        if distance < 5:  # Close enough to waypoint
            is_stopping = True
            change_waypoint_time = pygame.time.get_ticks()
            waypoint = None
        else:
            dx, dy = waypoint[0] - slenderman_x, waypoint[1] - slenderman_y
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist  # Normalize the direction vector
            slenderman_x += dx * slenderman_speed
            slenderman_y += dy * slenderman_speed

def draw_slenderman(screen):
    global slenderman_x, slenderman_y, waypoint, is_stopping, change_waypoint_time, last_known_player_pos
    
    # Calculate distance to player
    distance_to_player = math.hypot(player_rect.centerx - slenderman_x, player_rect.centery - slenderman_y)
    
    # Convert 30 meters to in-game units (30 meters * 50 units/meter = 1500 units)
    patrol_radius = 30 * 50
    
    # Convert 5 meters to in-game units (5 meters * 50 units/meter = 250 units)
    follow_distance = 5 * 50
    
    current_time = pygame.time.get_ticks()
    
    if distance_to_player <= follow_distance:
        # Follow player
        dx, dy = player_rect.centerx - slenderman_x, player_rect.centery - slenderman_y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  # Normalize the direction vector
        slenderman_x += dx * slenderman_speed
        slenderman_y += dy * slenderman_speed
        last_known_player_pos = (player_rect.centerx, player_rect.centery)
        waypoint = None
    elif last_known_player_pos:
        # Move towards the last known position of the player
        dx, dy = last_known_player_pos[0] - slenderman_x, last_known_player_pos[1] - slenderman_y
        distance_to_last_known = math.hypot(dx, dy)
        if distance_to_last_known < 5:  # Reached last known position
            last_known_player_pos = None
        else:
            dx, dy = dx / distance_to_last_known, dy / distance_to_last_known
            slenderman_x += dx * slenderman_speed
            slenderman_y += dy * slenderman_speed
    else:
        # Patrol within the radius
        if is_stopping:
            if current_time - change_waypoint_time > stop_duration:
                is_stopping = False
                change_waypoint_time = current_time
        else:
            if not waypoint or distance_to_player > patrol_radius:
                waypoint = generate_waypoint(player_rect.centerx, player_rect.centery, patrol_radius)
            move_slenderman_towards_waypoint()
    
    # Draw slenderman
    pygame.draw.circle(screen, slenderman_color, (int(slenderman_x), int(slenderman_y)), slenderman_radius)

def draw_exit_button(screen, font):
    mouse_pos = pygame.mouse.get_pos()
    button_text = "EXIT"
    exit_button = font.render(button_text, True, BUTTON_COLOR)
    exit_button_rect = exit_button.get_rect(center=(screen_width // 2, screen_height // 2))
    
    if exit_button_rect.collidepoint(mouse_pos):
        exit_button = font.render(button_text, True, WHITE)

    screen.blit(exit_button, exit_button_rect)
    return exit_button_rect

def handle_events():
    global running, show_exit_button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_exit_button = not show_exit_button
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check left mouse button click
            if show_exit_button and exit_button_rect.collidepoint(event.pos):
                running = False
                # Open Menu.py file
                menu_file_path = os.path.join("SlenderMan", "Code", "Python", "Menu", "Menu.py")
                try:
                    subprocess.Popen(["python", menu_file_path])  # Open Menu.py using subprocess
                except Exception as e:
                    print(f"Failed to open {menu_file_path}: {e}")

def move_player(keys):
    global player_rect
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
    
    # Boundary check
    player_rect.clamp_ip(screen.get_rect())

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    handle_events()
    
    keys = pygame.key.get_pressed()
    move_player(keys)

    # Clear the screen
    screen.fill(BLUE)
    
    # Draw the player
    draw_player(screen, player_rect)
    
    # Draw Slenderman animation
    draw_slenderman(screen)
    
    # Draw the "EXIT" button if the flag is set
    if show_exit_button:
        exit_button_rect = draw_exit_button(screen, font)
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display for fullscreen
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = win.get_size()
pygame.display.set_caption("Level Easy")

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
run_speed = 10

# Load textures
ground_texture = pygame.image.load('SlenderMan/Images/Environment/Grass.png')
player_idle_texture = pygame.image.load('SlenderMan/Images/Player/PlayerIdle.png')
player_walk_texture = pygame.image.load('SlenderMan/Images/Player/PlayerWalks.png')
player_run_texture = pygame.image.load('SlenderMan/Images/Player/PlayerRun.png')

# Tree textures
regular_tree_texture = pygame.image.load('SlenderMan/Images/Environment/TreeRegular.png')
tree_with_note_texture = pygame.image.load('SlenderMan/Images/Environment/TreeWithNote.png')

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Background music
music_path = 'SlenderMan/Sfx/Environment/Night.mp3'
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

def update_player_position():
    global player_x, player_y, current_texture, last_movement_direction
    keys = pygame.key.get_pressed()
    
    # Determine player movement and texture
    if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
        if keys[pygame.K_LSHIFT]:
            current_texture = pygame.transform.flip(player_run_texture, keys[pygame.K_a], False) if keys[pygame.K_a] else player_run_texture
            speed = run_speed
        else:
            current_texture = pygame.transform.flip(player_walk_texture, keys[pygame.K_a], False) if keys[pygame.K_a] else player_walk_texture
            speed = player_speed
    else:
        current_texture = pygame.transform.flip(player_idle_texture, last_movement_direction == "left", False)
        speed = 0

    # Move player
    if keys[pygame.K_a]:
        player_x -= speed
        last_movement_direction = "left"
    if keys[pygame.K_d]:
        player_x += speed
        last_movement_direction = "right"
    if keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_s]:
        player_y += speed

# Initialize last movement direction
last_movement_direction = "right"

def draw():
    # Calculate the drawing coordinates for the player
    player_draw_x = (WIDTH // 2) - (player_idle_texture.get_width() // 2)
    player_draw_y = (HEIGHT // 2) - (player_idle_texture.get_height() // 2)

    # Calculate the position of the background image relative to the player's position
    background_offset_x = player_x % ground_texture.get_width()
    background_offset_y = player_y % ground_texture.get_height()

    # Draw the background images to cover the entire map
    for x in range(-1, (WIDTH // ground_texture.get_width()) + 1):
        for y in range(-1, (HEIGHT // ground_texture.get_height()) + 1):
            tile_x = x * ground_texture.get_width() - background_offset_x
            tile_y = y * ground_texture.get_height() - background_offset_y
            win.blit(ground_texture, (tile_x, tile_y))

    # Draw the player at the center of the screen
    win.blit(current_texture, (player_draw_x, player_draw_y))

    pygame.display.flip()


# Main game loop
running = True
current_texture = player_idle_texture
tree_list = []

# Start the main game loop
while running:
    handle_events()
    update_player_position()
    draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


import pygame
import sys
import random
import subprocess
from Player import player_idle_animation, player_run_animation, player_walk_animation, glitch_animation

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
player_speed = 10
run_speed = 20

# Environment:
# Load Ground textures
regular_tree_texture = pygame.image.load('SlenderMan/Images/Environment/TreeRegular.png')
regular_tree_texture = pygame.transform.scale(regular_tree_texture, (200, 500))

tree_with_note_texture = pygame.image.load('SlenderMan/Images/Environment/ScoreTree.png')
tree_with_note_texture = pygame.transform.scale(tree_with_note_texture, (200, 500))

# Load Gift texture
Gift_texture = pygame.image.load('SlenderMan/Images/Items/Gift.png')
Gift_texture = pygame.transform.scale(Gift_texture, (200, 200))

ground_texture_1 = pygame.image.load('SlenderMan/Images/Environment/Grass1.png')
ground_texture_1 = pygame.transform.scale(ground_texture_1, (200, 200))

ground_texture_2 = pygame.image.load('SlenderMan/Images/Environment/Grass2.png')
ground_texture_2 = pygame.transform.scale(ground_texture_2, (200, 200))

ground_texture_3 = pygame.image.load('SlenderMan/Images/Environment/Grass3.png')
ground_texture_3 = pygame.transform.scale(ground_texture_3, (200, 200))

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Background music
music_path = 'SlenderMan/Sfx/Environment/Night.mp3'
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Load footsteps sound
footsteps_sound_path = 'SlenderMan/Sfx/Player/Footsteps.mp3'
footsteps_sound = pygame.mixer.Sound(footsteps_sound_path)
footsteps_sound.set_volume(0.5)  # Adjust the volume as needed

# Load the point collection sound
point_sound_path = 'Slenderman/Sfx/Player/Page.mp3'
point_sound = pygame.mixer.Sound(point_sound_path)

def handle_events():
    global running, score, collected_notes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                subprocess.Popen(["python", "SlenderMan/Code/Python/Menu/Menu.py"])
            elif event.key == pygame.K_p:
                # Cheat command: Pressing "P" awards 100 points
                score += 100
                # Check if the player has 10 points or more to trigger win condition
                if score >= 10:
                    collected_notes = 10

def update_player_position():
    global player_x, player_y, current_texture, last_movement_direction, is_walking
    keys = pygame.key.get_pressed()
    
    # Determine player movement and texture
    if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
        if keys[pygame.K_LSHIFT]:
            current_texture = pygame.transform.flip(player_run.get_frame(), keys[pygame.K_a], False) if keys[pygame.K_a] else player_run.get_frame()
            speed = run_speed
            if footsteps_sound.get_num_channels() > 0:
                footsteps_sound.stop()  # Stop footsteps sound when sprinting
        else:
            current_texture = pygame.transform.flip(player_walk.get_frame(), keys[pygame.K_a], False) if keys[pygame.K_a] else player_walk.get_frame()
            speed = player_speed
            if footsteps_sound.get_num_channels() == 0:
                footsteps_sound.play(-1)  # Play footsteps sound when walking
        is_walking = True
    else:
        current_texture = pygame.transform.flip(player_idle.get_frame(), last_movement_direction == "left", False)
        speed = 0
        if is_walking:
            footsteps_sound.stop()  # Stop footsteps sound when not moving
            is_walking = False

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

# Initialize last movement direction and walking state
last_movement_direction = "right"
is_walking = False

# Dictionary to store the ground textures for each tile
ground_textures = {}

def get_random_texture():
    texture_choice = random.choice([ground_texture_1, ground_texture_2, ground_texture_3])
    if random.choice([True, False]):
        texture_choice = pygame.transform.flip(texture_choice, True, False)  # Flip horizontally
    return texture_choice

# Function to spawn trees outside the player's screen area
def spawn_trees():
    global trees
    trees = []
    while len(trees) < 10:
        tree_texture = tree_with_note_texture
        if random.choice([True, False]):
            tree_texture = pygame.transform.flip(tree_texture, True, False)  # Randomly flip texture
        # Generate tree coordinates outside of the player's screen area
        tree_x = random.choice([-WIDTH, WIDTH * 2])
        tree_y = random.randint(-HEIGHT, HEIGHT * 2)
        new_tree = {'rect': pygame.Rect(tree_x, tree_y, 200, 200), 'texture': tree_texture, 'collected': False}
        # Check if the new tree is far enough from existing trees
        if all(pygame.math.Vector2(new_tree['rect'].center).distance_to(tree['rect'].center) >= 200 for tree in trees):
            trees.append(new_tree)

# Function to check if player is near a tree
def is_near_tree(player_rect):
    for tree in trees:
        if not tree['collected'] and player_rect.colliderect(tree['rect']):
            return tree
    return None

def draw():
    # Calculate the drawing coordinates for the player
    player_draw_x = (WIDTH // 2) - (current_texture.get_width() // 2)
    player_draw_y = (HEIGHT // 2) - (current_texture.get_height() // 2)

    # Calculate the position of the background image relative to the player's position
    background_offset_x = player_x % ground_texture_1.get_width()
    background_offset_y = player_y % ground_texture_1.get_height()

    # Calculate the visible range of tiles
    start_x = (player_x - WIDTH // 2) // ground_texture_1.get_width()
    end_x = (player_x + WIDTH // 2) // ground_texture_1.get_width() + 1
    start_y = (player_y - HEIGHT // 2) // ground_texture_1.get_height()
    end_y = (player_y + HEIGHT // 2) // ground_texture_1.get_height() + 1

    # Draw the background images to cover the entire map
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if (x, y) not in ground_textures:
                ground_textures[(x, y)] = get_random_texture()
            tile_x = x * ground_texture_1.get_width() - player_x + (WIDTH // 2)
            tile_y = y * ground_texture_1.get_height() - player_y + (HEIGHT // 2)
            win.blit(ground_textures[(x, y)], (tile_x, tile_y))

    # Draw the player at the center of the screen
    win.blit(current_texture, (player_draw_x, player_draw_y))

    # Draw trees
    for tree in trees:
        if not tree['collected']:
            win.blit(tree['texture'], (tree['rect'].x - player_x + WIDTH // 2, tree['rect'].y - player_y + HEIGHT // 2))

    pygame.display.flip()

# Define Slenderman's properties
slenderman_speed = 5
slenderman_texture = pygame.image.load('Slenderman/Images/Monster/Slenderman.png')
slenderman_texture = pygame.transform.scale(slenderman_texture, (200, 500))
slenderman_x = 0  # Starting position (will be updated)
slenderman_y = 0

# Function to update Slenderman's position
def update_slenderman_position():
    global slenderman_x, slenderman_y
    # Slenderman follows the player
    if player_x < slenderman_x:
        slenderman_x -= slenderman_speed
    elif player_x > slenderman_x:
        slenderman_x += slenderman_speed
    if player_y < slenderman_y:
        slenderman_y -= slenderman_speed
    elif player_y > slenderman_y:
        slenderman_y += slenderman_speed

close_distance = 200

# Function to draw Slenderman
def draw_slenderman():
    win.blit(slenderman_texture, (slenderman_x - player_x + WIDTH // 2, slenderman_y - player_y + HEIGHT // 2))

# Function to check if Slenderman is close to the player
def is_slenderman_close():
    distance = pygame.math.Vector2(slenderman_x - player_x, slenderman_y - player_y).length()
    return distance < close_distance

# Function to play the "Away" sound when Slenderman is close
def play_away_sound():
    print("Slenderman is close!")
    away_sound_path = 'Slenderman/Sfx/Monster/Away.mp3'
    pygame.mixer.music.load(away_sound_path)
    pygame.mixer.music.play()

# Function to overlay the glitch animation over the player's current animation
def overlay_glitch_animation():
    if is_slenderman_close():
        current_texture.blit(player_glitch.get_frame(), (0, 0))

# Function to stop the "Away" sound
def stop_away_sound():
    pygame.mixer.music.stop()

# Function to clear the glitch animation
def clear_glitch_animation():
    current_texture

# Function to overlay the glitch animation all over the screen
def overlay_glitch_screen():
    for x in range(0, WIDTH, player_size):
        for y in range(0, HEIGHT, player_size):
            win.blit(player_glitch.get_frame(), (x, y))

# Function to handle player's death
def player_death():
    # Pause the game
    paused = True

    # Remove all audio
    pygame.mixer.music.stop()
    pygame.mixer.stop()

    # Fill the screen with red
    win.fill((255, 0, 0))  # Red color

    # Overlay the glitch animation all over the screen
    overlay_glitch_screen()
    pygame.display.flip()

    # Display Slenderman's texture in the center of the screen
    slenderman_death_texture = slenderman_texture
    win.blit(slenderman_death_texture, ((WIDTH - slenderman_death_texture.get_width()) // 2, (HEIGHT - slenderman_death_texture.get_height()) // 2))
    pygame.display.flip()

    # Play the "Close" sound
    close_sound_path = 'Slenderman/Sfx/Monster/Close.mp3'
    pygame.mixer.music.load(close_sound_path)
    pygame.mixer.music.play()

    # Wait for the sound to finish
    pygame.time.delay(5000)  # 5 seconds

    # Remove Slenderman's texture and fill the screen with black
    win.fill((0, 0, 0))  # Black color
    pygame.display.flip()

    # Wait for 2 seconds
    pygame.time.delay(2000)

    # Overlay the glitch animation all over the screen
    overlay_glitch_screen()
    pygame.display.flip()

    # Play the "SMAttack" sound
    sm_attack_sound_path = 'Slenderman/Sfx/Monster/SMAttack.mp3'
    pygame.mixer.music.load(sm_attack_sound_path)
    pygame.mixer.music.play()

    # Display the text "I found you" in red
    font = pygame.font.Font(font_path, 36)
    text_surface = font.render("I found you", True, (255, 0, 0))  # Red color
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    win.blit(text_surface, text_rect)
    pygame.display.flip()

    # Keep the text for 5 seconds
    pygame.time.delay(5000)

    # Close the game
    pygame.quit()
    subprocess.Popen(["python", "SlenderMan/Code/Python/Menu/Menu.py"])

# Main game loop
running = True
player_idle = player_idle_animation()
player_run = player_run_animation()
player_walk = player_walk_animation()
player_glitch = glitch_animation()
current_texture = player_idle.get_frame()

# Initialize score and collected notes
score = 0
collected_notes = 0
paused = False

# Load the font for displaying text
font_path = 'SlenderMan/Images/Menu/font.ttf'
font = pygame.font.Font(font_path, 36)


# Start the main game loop
while running:
    handle_events()
    update_player_position()
    update_slenderman_position()

    # Check if Slenderman is close
    if is_slenderman_close():
        play_away_sound()
        overlay_glitch_animation()
        # Check if Slenderman touches the player
        if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(pygame.Rect(slenderman_x, slenderman_y, 200, 500)):
            player_death()

    else:
        stop_away_sound()

    # Spawn trees
    if not ground_textures:  # Only spawn trees once
        spawn_trees()

    # Check if player is near a tree and press "E" to collect
    if not paused:
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        tree = is_near_tree(player_rect)
        if tree and pygame.key.get_pressed()[pygame.K_e]:
            if not tree['collected']:
                score += 1
                collected_notes += 1
                tree['texture'] = regular_tree_texture  # Change tree texture to regular after collecting
                tree['collected'] = True
                point_sound.play()

    # Draw the game elements
    draw()
    draw_slenderman()

    # Display the score and collected notes
    score_text = font.render(f'Collected Notes: {collected_notes}', True, (255, 255, 255))
    win.blit(score_text, (10, 10))
    pygame.display.flip()

    # Check if all notes are collected
if collected_notes == 10:
    paused = True
    survived_text = font.render('Survived!', True, (255, 0, 0))  # Red color (255, 0, 0)
    win.blit(survived_text, (WIDTH // 2 - survived_text.get_width() // 2, HEIGHT // 2 - survived_text.get_height() // 2))
    pygame.display.flip()
    # Get the current time in milliseconds
    start_time = pygame.time.get_ticks()
    # Wait for 5 seconds
    while pygame.time.get_ticks() - start_time < 5000:
        pass
    # Close the game
    pygame.quit()
    subprocess.Popen(["python", "SlenderMan/Code/Python/Menu/Menu.py"])

    clock.tick(60)

pygame.quit()
sys.exit()
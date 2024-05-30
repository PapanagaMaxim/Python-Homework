import pygame
import sys
from Button import Button
import subprocess
import threading

pygame.init()

# Get the screen size
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

# Initial screen size
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Set up the display
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Menu")

# Load assets
Logo = pygame.image.load('SlenderMan/Images/Menu/Logo.png')
Logo = pygame.transform.scale(Logo, (150, 150))

Gift_texture = pygame.image.load('SlenderMan/Images/Items/Gift.png')
Gift_texture = pygame.transform.scale(Gift_texture, (200, 250))

BG = pygame.image.load("SlenderMan/Images/Menu/Background.jpg")
BG = pygame.transform.scale(BG, SCREEN_SIZE)

pygame.mixer.init()
music_path_1 = 'SlenderMan/Sfx/Lobby/MusicBox1.mp3'
music_path_2 = 'SlenderMan/Sfx/Lobby/MusicBox2.mp3'
button_sound_path = 'SlenderMan/Sfx/Lobby/ButtonClick.mp3'

button_sound = pygame.mixer.Sound(button_sound_path)

def get_font(size):
    return pygame.font.Font("SlenderMan/Images/Menu/font.ttf", size)

def toggle_screen_size():
    global SCREEN_SIZE, SCREEN

    if SCREEN_SIZE == (SCREEN_WIDTH, SCREEN_HEIGHT):
        SCREEN_SIZE = (int(SCREEN_WIDTH * 0.8), int(SCREEN_HEIGHT * 0.8))
    else:
        SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    SCREEN = pygame.display.set_mode(SCREEN_SIZE)

def play_music():
    while True:
        pygame.mixer.music.load(music_path_1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.load(music_path_2)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

def handle_button_click(button, pos):
    if button.checkForInput(pos):
        button_sound.play()
        pygame.time.delay(100)  # Small delay to ensure sound plays before the next action
        return True
    return False

def handle_gift_click(pos):
    gift_rect = Gift_texture.get_rect(topleft=(10, SCREEN_SIZE[1] - Gift_texture.get_height() - 10))
    if gift_rect.collidepoint(pos):
        button_sound.play()
        pygame.time.delay(100)
        pygame.quit()
        subprocess.Popen(["python", "Slenderman/Code/Python/Secret/EasterEgg.py"])
        return True
    return False

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(100).render("The Woods", True, "#DC0000")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 3))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        EASY_BUTTON = Button(image=None, pos=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2), 
                            text_input="Easy Mode", font=get_font(75), base_color="#C40C0C", hovering_color="White")
        MEDIUM_BUTTON = Button(image=None, pos=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2 + 100), 
                            text_input="Medium Mode", font=get_font(75), base_color="#C40C0C", hovering_color="White")
        HARD_BUTTON = Button(image=None, pos=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2 + 200), 
                            text_input="Hard Mode", font=get_font(75), base_color="#C40C0C", hovering_color="White")
        BACK_BUTTON = Button(image=None, pos=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] * 9 // 10), 
                            text_input="BACK", font=get_font(75), base_color="#DC0000", hovering_color="White")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        # Draw the gift image at the bottom-left corner
        SCREEN.blit(Gift_texture, (10, SCREEN_SIZE[1] - Gift_texture.get_height() - 10))

        # Draw the logo in the top right corner
        SCREEN.blit(Logo, (SCREEN_SIZE[0] - Logo.get_width() - 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if handle_button_click(EASY_BUTTON, PLAY_MOUSE_POS):
                    pygame.quit()  # Shut down the current Pygame window
                    subprocess.Popen(["python", "SlenderMan/Code/Python/Levels/Easy/Easy.py"])
                    return  # Exit the function to prevent further updates
                if handle_button_click(MEDIUM_BUTTON, PLAY_MOUSE_POS):
                    pygame.quit()  # Shut down the current Pygame window
                    subprocess.Popen(["python", "SlenderMan/Code/Python/Levels/Medium/Medium.py"])
                    return  # Exit the function to prevent further updates
                if handle_button_click(HARD_BUTTON, PLAY_MOUSE_POS):
                    pygame.quit()  # Shut down the current Pygame window
                    subprocess.Popen(["python", "SlenderMan/Code/Python/Levels/Hard/Hard.py"])
                    return  # Exit the function to prevent further updates
                if handle_button_click(BACK_BUTTON, PLAY_MOUSE_POS):
                    button_sound.play()
                    main_menu()
                    return  # Exit the function to prevent further updates
                if handle_gift_click(PLAY_MOUSE_POS):
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    toggle_screen_size()

        pygame.display.update()

def main_menu():
    # Start playing music in a separate thread when entering the main menu
    music_thread = threading.Thread(target=play_music)
    music_thread.daemon = True
    music_thread.start()

    while True:
        # Blit the scaled background image to fill the screen
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Change "Main Menu" text to "The Woods" and use red color
        MENU_TEXT = get_font(100).render("The Woods", True, "#DC0000")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 3))

        BUTTON_HEIGHT = SCREEN_SIZE[1] // 6  # Height for each button
        BUTTON_Y = SCREEN_SIZE[1] // 2  # Y position for buttons

        PLAY_BUTTON = Button(image=pygame.image.load("Slenderman/Images/Menu/Play Rect.png"), pos=(SCREEN_SIZE[0] // 2, BUTTON_Y), 
                            text_input="PLAY", font=get_font(75), base_color="#C40C0C", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Slenderman/Images/Menu/Quit Rect.png"), pos=(SCREEN_SIZE[0] // 2, BUTTON_Y + BUTTON_HEIGHT), 
                            text_input="QUIT", font=get_font(75), base_color="#C40C0C", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        # Draw the gift image at the bottom-left corner
        SCREEN.blit(Gift_texture, (10, SCREEN_SIZE[1] - Gift_texture.get_height() - 10))

        # Draw the logo in the top right corner
        SCREEN.blit(Logo, (SCREEN_SIZE[0] - Logo.get_width() - 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if handle_button_click(PLAY_BUTTON, MENU_MOUSE_POS):
                    play()
                if handle_button_click(QUIT_BUTTON, MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if handle_gift_click(MENU_MOUSE_POS):
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    toggle_screen_size()

        pygame.display.update()

main_menu()
#pip install numpy
#pip install pygame
import pygame
import sys
from Button import Button
import subprocess

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

# Load and scale the background image
BG = pygame.image.load("Slenderman/Images/Menu/Background.jpg")
BG = pygame.transform.scale(BG, SCREEN_SIZE)

def get_font(size):
    return pygame.font.Font("Slenderman/Images/Menu/font.ttf", size)

def toggle_screen_size():
    global SCREEN_SIZE

    # If the screen size is the same as the initial size, make it smaller
    if SCREEN_SIZE == (SCREEN_WIDTH, SCREEN_HEIGHT):
        SCREEN_SIZE = (int(SCREEN_WIDTH * 0.8), int(SCREEN_HEIGHT * 0.8))
    else:
        SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Set the screen size
    SCREEN = pygame.display.set_mode(SCREEN_SIZE)

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()  # Shut down the current Pygame window
                    subprocess.Popen(["python", "SlenderMan/Code/Python/Levels/Easy/Easy.py"])
                    return  # Exit the function to prevent further updates
                if MEDIUM_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()  # Shut down the current Pygame window
                    subprocess.Popen(["python", "SlenderMan/Code/Python//Levels/Medium/Medium.py"])
                    return  # Exit the function to prevent further updates
                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()  # Shut down the current Pygame window
                    subprocess.Popen(["python", "SlenderMan/Code/Python/Levels/Hard/LevelHard.py"])
                    return  # Exit the function to prevent further updates
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                    return  # Exit the function to prevent further updates
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    toggle_screen_size()

        pygame.display.update()

def main_menu():
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
        QUIT_BUTTON = Button(image=pygame.image.load("Slenderman/Images/Menu//Quit Rect.png"), pos=(SCREEN_SIZE[0] // 2, BUTTON_Y + BUTTON_HEIGHT), 
                            text_input="QUIT", font=get_font(75), base_color="#C40C0C", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    toggle_screen_size()

        pygame.display.update()

main_menu()

#Slenderman/Images/Player
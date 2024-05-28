import pygame
import sys
from Player import Player
from Slenderman import Slenderman
from Visual import Visual
from Settings import Settings
import os
import subprocess

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self, screen, settings, visual, font):  # Pass the font object to the constructor
        self.screen = screen
        self.settings = settings
        self.visual = visual
        self.player = Player(100, 5, 50, 50, settings)
        self.slenderman = Slenderman(settings)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = font  # Store the font object
        self.show_exit_button = False  # Initialize the flag
        self.exit_button_rect = None  # Initialize the exit button rect

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_exit_button = not self.show_exit_button
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check left mouse button click
                if self.show_exit_button and self.exit_button_rect.collidepoint(event.pos):
                    self.running = False
                    # Open Menu.py file
                    menu_file_path = os.path.join("SlenderMan", "Code", "Python", "Menu", "Menu.py")
                    try:
                        subprocess.Popen(["python", menu_file_path])  # Open Menu.py using subprocess
                    except Exception as e:
                        print(f"Failed to open {menu_file_path}: {e}")

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.slenderman.move_slenderman_towards_waypoint()
            self.screen.fill((0, 0, 255))
            self.visual.draw_visual_elements(self.player.rect)
            if self.show_exit_button:
                self.exit_button_rect = self.visual.draw_exit_button()

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    font_path = os.path.join("SlenderMan", "Images", "Menu", "font.ttf")
    if not os.path.exists(font_path):
        print(f"Font file not found at {font_path}, using default font.")
        font = pygame.font.Font(None, 36)
    else:
        font = pygame.font.Font(font_path, 36)
    screen = pygame.display.set_mode((800, 600))
    settings = Settings()
    slenderman = Slenderman(settings)
    visual = Visual(screen, slenderman, font)
    # Load font for the "EXIT" button

    game = Game(screen, settings, visual, font)  # Pass the font object
    game.run()

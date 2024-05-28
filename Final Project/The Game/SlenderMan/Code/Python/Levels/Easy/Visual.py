import pygame


class Visual:
    def __init__(self, screen, slenderman, font):
        self.screen = screen
        self.font = font
        self.slenderman = slenderman

    def draw_exit_button(self):
        mouse_pos = pygame.mouse.get_pos()
        button_text = "EXIT"
        exit_button = self.font.render(button_text, True, (196, 12, 12))
        exit_button_rect = exit_button.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

        if exit_button_rect.collidepoint(mouse_pos):
            exit_button = self.font.render(button_text, True, (255, 255, 255))

        self.screen.blit(exit_button, exit_button_rect)
        return exit_button_rect

    def draw_player(self, player_rect):
        pygame.draw.rect(self.screen, (255, 0, 0), player_rect)

    def draw_visual_elements(self,player_rect):
        self.draw_player(player_rect)
        self.slenderman.draw_slenderman(self.screen, player_rect)
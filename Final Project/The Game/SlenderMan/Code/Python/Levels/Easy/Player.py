import pygame

class Player:
    def __init__(self, x, y, width, height, settings):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = settings.PLAYER_SPEED

    def move(self, keys):
        if keys[pygame.K_a]:  # 'A' key
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # 'D' key
            self.rect.x += self.speed
        if keys[pygame.K_w]:  # 'W' key
            self.rect.y -= self.speed
        if keys[pygame.K_s]:  # 'S' key
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
import pygame
import math
import random


class Slenderman:
    def __init__(self, settings):
        self.radius = 20
        self.color = (255, 255, 255)
        self.x = 0
        self.y = 0
        self.speed = settings.SLENDERMAN_SPEED
        self.waypoint = None
        self.last_known_player_pos = None
        self.change_waypoint_time = 0
        self.stop_duration = 1000
        self.is_stopping = False

    def generate_waypoint(self, center_x, center_y, radius):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, radius)
        waypoint_x = center_x + distance * math.cos(angle)
        waypoint_y = center_y + distance * math.sin(angle)
        return waypoint_x, waypoint_y

    def move_slenderman_towards_waypoint(self):
        if self.waypoint:
            distance = math.hypot(self.waypoint[0] - self.x, self.waypoint[1] - self.y)
            if distance < 5:
                self.is_stopping = True
                self.change_waypoint_time = pygame.time.get_ticks()
                self.waypoint = None
            else:
                dx, dy = self.waypoint[0] - self.x, self.waypoint[1] - self.y
                dist = math.hypot(dx, dy)
                dx, dy = dx / dist, dy / dist
                self.x += dx * self.speed
                self.y += dy * self.speed

    def draw_slenderman(self, screen, player_rect):
        distance_to_player = math.hypot(player_rect.centerx - self.x, player_rect.centery - self.y)
        patrol_radius = 30 * 50
        follow_distance = 5 * 50
        current_time = pygame.time.get_ticks()

        if distance_to_player <= follow_distance:
            dx, dy = player_rect.centerx - self.x, player_rect.centery - self.y
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist
            self.x += dx * self.speed
            self.y += dy * self.speed
            self.last_known_player_pos = (player_rect.centerx, player_rect.centery)
            self.waypoint = None
        elif self.last_known_player_pos:
            dx, dy = self.last_known_player_pos[0] - self.x, self.last_known_player_pos[1] - self.y
            distance_to_last_known = math.hypot(dx, dy)
            if distance_to_last_known < 5:
                self.last_known_player_pos = None
            else:
                dx, dy = dx / distance_to_last_known, dy / distance_to_last_known
                self.x += dx * self.speed
                self.y += dy * self.speed
        else:
            if self.is_stopping:
                if current_time - self.change_waypoint_time > self.stop_duration:
                    self.is_stopping = False
                    self.change_waypoint_time = current_time
            else:
                if not self.waypoint or distance_to_player > patrol_radius:
                    self.waypoint = self.generate_waypoint(player_rect.centerx, player_rect.centery, patrol_radius)
                self.move_slenderman_towards_waypoint()

        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
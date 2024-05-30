import pygame

class Animation:
    def __init__(self, frames, speed):
        self.frames = frames
        self.speed = speed
        self.index = 0
        self.last_update = pygame.time.get_ticks()

    def get_frame(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.speed:
            self.index = (self.index + 1) % len(self.frames)
            self.last_update = now
        return self.frames[self.index]

# Load and scale images
def load_images(paths, scale):
    return [pygame.transform.scale(pygame.image.load(path), scale) for path in paths]

# Define the player idle animation
def player_idle_animation():
    frames = load_images([
        'SlenderMan/Images/Player/PLayerIdle01.png',
        'SlenderMan/Images/Player/PLayerIdle02.png'
    ], (200, 200))
    return Animation(frames, speed=500)

# Define the player run animation
def player_run_animation():
    frames = load_images([
        'SlenderMan/Images/Player/PLayerRun01.png',
        'SlenderMan/Images/Player/PLayerRun02.png'
    ], (200, 200))
    return Animation(frames, speed=100)

# Define the player walk animation
def player_walk_animation():
    frames = load_images([
        'SlenderMan/Images/Player/PLayerWalks01.png',
        'SlenderMan/Images/Player/PLayerWalks02.png',
        'SlenderMan/Images/Player/PLayerWalks03.png',
        'SlenderMan/Images/Player/PLayerWalks04.png',
        'SlenderMan/Images/Player/PLayerWalks05.png',
        'SlenderMan/Images/Player/PLayerWalks06.png',
        'SlenderMan/Images/Player/PLayerWalks07.png',
        'SlenderMan/Images/Player/PLayerWalks08.png',
        'SlenderMan/Images/Player/PLayerWalks09.png',
        'SlenderMan/Images/Player/PLayerWalks10.png'
    ], (200, 200))
    return Animation(frames, speed=200)

# Define the glitch animation
def glitch_animation():
    frames = load_images([
        'SlenderMan/Images/Monster/Glitch01.png',
        'SlenderMan/Images/Monster/Glitch02.png',
        'SlenderMan/Images/Monster/Glitch03.png',
        'SlenderMan/Images/Monster/Glitch04.png'
    ], (200, 200))
    return Animation(frames, speed=200)
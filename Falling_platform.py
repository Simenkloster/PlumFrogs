from Object import Object
import pygame
from sprite_functions import load_sprite_sheets

class Falling_platform(Object): # 32 x 10
    ANIMATION_DELAY = 3
    GRAVITY = 1

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "falling_platform")
        self.falling_platforms = load_sprite_sheets("Traps","Falling Platforms",width,height)
        self.image = self.falling_platforms["On"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "On"
        self.fall_time = 0
        self.falling = False
        self.fall_count = 0
        self.x = x
        self.y = y
        self.y_vel = 0

    def start_falling(self):
        print("kjører start dallign")
        self.falling = True

    def move(self, dy):
        self.rect.y+=dy
        
    def loop(self):
        self.move(self.y_vel)
        sprites = self.falling_platforms[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        
        if self.fall_time >= 1:
            self.fall_time -= 1
            self.y += 10

        if self.falling:
            self.fall_count+=1
            self.y_vel += min(1, (self.fall_count / 60) * self.GRAVITY)

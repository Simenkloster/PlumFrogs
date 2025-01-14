#64x64
from Object import Object
import pygame
from sprite_functions import load_sprite_sheets


class Checkpoint(Object):
    def __init__(self, x, y, width=64, height=64):
        super().__init__(x, y, width, height, name = "checkpoint")
        self.checkpoint = load_sprite_sheets("Checkpoints", "Checkpoint", width, height)
        self.image = self.checkpoint["CheckpointNoFlag"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.activated = False
        self.animation_name = "CheckpointNoFlag"
        self.ANIMATION_DELAY = 2

    def activate(self):
        if not self.activated:
            self.ANIMATION_DELAY = 1
            self.activated = True
            self.animation_name = "CheckpointActivating"
            self.animation_count = 0

    def makeIdle(self):
        self.ANIMATION_DELAY = 3
        self.animation_name = "CheckpointFlagOut"
        self.animation_count = 0



    def loop(self):
        sprites = self.checkpoint[self.animation_name]
        sprite_index = (self.animation_count//self.ANIMATION_DELAY)%len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1


        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0
            if self.activated:
                self.makeIdle()

                  


        self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
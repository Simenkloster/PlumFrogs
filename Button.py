import pygame
from os import listdir
from os.path import isfile, join
from Object import Object
from sprite_functions import load_sprite_sheets


class Button(Object): #21x22
    def __init__(self, buttonType, x, y, width=21, height=22):
        super().__init__(x, y, width, height)
        self.button_sheet = load_sprite_sheets("Menu", "Buttons", width, height)
        self.image = self.button_sheet[buttonType][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
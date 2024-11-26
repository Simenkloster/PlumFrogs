import pygame
from Player import Player
from Block import Block
from Fire import Fire
from Spike import Spike
from Fan import Fan
from Falling_platform import Falling_platform
from Trampoline import Trampoline
from sprite_functions import *
from movement_functions import *
pygame.init() 


WIDTH, HEIGHT = 1300, 800
block_size = 96

fire = Fire(350, HEIGHT - block_size * 3 - 64, 16, 32)
fire.on()
spike = Spike(600, HEIGHT-block_size-32, 16, 16)
fan = Fan(500, HEIGHT - block_size * 3 - 16, 24, 8)
fan.on()
falling2 = Falling_platform(block_size*23, HEIGHT - block_size*6, 32, 10)
falling_platforms = [Falling_platform(80*i, 350, 32, 10) for i in range(10, 20)]
floor2 = [Block(block_size * i, HEIGHT - block_size*3, block_size) for i in range(-2,20)]
floor3 = [Block(block_size * i, HEIGHT - block_size*6, block_size) for i in range(8,20)]
pillar2 = [Block(-block_size *-8, HEIGHT - block_size*i, block_size) for i in range(1, 7)]
pillar = [Block(-block_size * 2, HEIGHT - block_size * i, block_size) for i in range(1, 8)]
floor4 = [Block(block_size * i, HEIGHT - block_size*6, block_size) for i in range(20,21)]

trampoline = Trampoline(300, HEIGHT - block_size - 56, 28, 28)
    
#Liste med blocks som danner gulvet
floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]

objects = [*floor, fire, *falling_platforms, spike, fan, trampoline, *floor2, *pillar, *floor3, falling2, *pillar2]
loopable = [fan, fire, *falling_platforms, falling2, trampoline]
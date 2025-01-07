import pygame
from Player import Player
from Block import Block
from Fire import Fire
from Spike import Spike
from Fan import Fan
from FallingPlatform import Falling_platform
from Trampoline import Trampoline
from sprite_functions import *
from movement_functions import *
from Checkpoint import Checkpoint
from SpeedPlatform import SpeedPlatform
from Spikehead import Spikehead
pygame.init() 


WIDTH, HEIGHT = 1300, 800
block_size = 96

fire = Fire(950, HEIGHT - block_size * 4 - 250, 16, 32)
fire.on()
spike = Spike(2750, HEIGHT-block_size*6 - 35, 16, 16)
spike2 = Spike(2780, HEIGHT-block_size*6 - 35, 16, 16)
spike3 = Spike(2800, HEIGHT-block_size*6 - 35, 16, 16)
spike4 = Spike(2830, HEIGHT-block_size*6 - 35, 16, 16)
spike5 = Spike(2860, HEIGHT-block_size*6 - 35, 16, 16)
#fan = Fan(500, HEIGHT - block_size * 3 - 16, 24, 8)
#fan.on()
fallingplatform2 = Falling_platform(500, HEIGHT - block_size * 4 - 16, 24, 8)
falling2 = Falling_platform(block_size*23, HEIGHT - block_size*6, 22, 10)
falling_platforms = [Falling_platform(80*i, 350, 32, 10) for i in range(10, 20)]
#floor2 = [Block(block_size * i, HEIGHT - block_size*3, block_size) for i in range(-2,20)]
floor3 = [Block(block_size * i, HEIGHT - block_size*6, block_size) for i in range(8,20)]
floor5 = [Block(block_size * i, HEIGHT - block_size*6, block_size) for i in range(25,32)]
pillar2 = [Block(-block_size *-8, HEIGHT - block_size*i, block_size) for i in range(1, 7)]
pillar = [Block(-block_size * 2, HEIGHT - block_size * i, block_size) for i in range(1, 15)]
floor4 = [Block(block_size * i, HEIGHT - block_size*6, block_size) for i in range(20,21)]
checkpoint1 = Checkpoint(2900, HEIGHT-block_size*6-65, 64, 64)
fire2 = Fire(2650, HEIGHT-block_size*6-65, 16, 32)
fire2.on()
Speedplatform1 = [SpeedPlatform(64*i, HEIGHT-block_size - 128, 32, 8) for i in range(20,30)]

trampoline = Trampoline(300, HEIGHT - block_size - 56, 28, 28)
    
#Liste med blocks som danner gulvet
floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]

objects = [*floor, fire, *falling_platforms, spike, trampoline, *pillar, *floor3, falling2, *pillar2, fallingplatform2, *floor5, spike2,spike3,spike4,spike5,checkpoint1,fire2, *Speedplatform1]
loopable = [fire, *falling_platforms, falling2, trampoline, fallingplatform2, fire2,checkpoint1, *Speedplatform1]
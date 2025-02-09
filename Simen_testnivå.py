from Fire import Fire
from Spike import Spike
from Fan import Fan
from Block import Block
from Player import Player
from FallingPlatform import Falling_platform
from Trampoline import Trampoline
from Fruits.Pineapple import Pineapple
from Fruits.Cherry import Cherry
from Checkpoint import Checkpoint
from SpeedPlatform import SpeedPlatform
from Goal import Goal

WIDTH, HEIGHT = 1000, 800
block_size = 96



#Making stuff that goes into the game
Player1 = Player(100, 100, 50, 50)
fire = Fire(500, HEIGHT - block_size - 64, 16, 32)
fire.on()
spike = Spike(600, HEIGHT-block_size-32, 16, 16)
fan = Fan(200, HEIGHT - block_size - 16, 24, 8)
fan.on()
falling_platforms = [Falling_platform(80*i, 350, 32, 10) for i in range(8, 20)]
trampoline = Trampoline(300, HEIGHT - block_size - 56, 28, 28)
pineapple = Pineapple(700, HEIGHT - block_size - 64, 32, 32)

speedplatforms = [SpeedPlatform(64*i, HEIGHT-block_size - 128, 32, 8) for i in range(20,30)]

checkpoint1 = Checkpoint(2100, HEIGHT-block_size - 128, 64, 64)

checkpoint2 = Checkpoint(-400, HEIGHT - block_size - 128, 64, 64)

#Liste med blocks som danner gulvet
floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, 150)]

cherry = Cherry(1000, HEIGHT-block_size - 64, 32, 32)

goal = Goal(2200, HEIGHT-block_size-128)

#Liste med alle tingene som inngår i spillet
loopable = [fire, fan, pineapple, trampoline, *falling_platforms, cherry, checkpoint1, checkpoint2, *speedplatforms, goal]
objects = [*floor, fire, *falling_platforms, spike, fan, trampoline, pineapple, cherry, checkpoint1, checkpoint2, *speedplatforms, goal]
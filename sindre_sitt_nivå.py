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
from Spikehead import Spikehead

WIDTH, HEIGHT = 1000, 800
block_size = 96

#Making stuff that goes into the game
Player1 = Player(50, 50, 50, 50)
fire = Fire(1100, HEIGHT - block_size - 64, 16, 32)
fire.on()
spike = Spike(15 * block_size, HEIGHT-block_size-32, 16, 16)
fan = Fan(15 * block_size, HEIGHT - block_size - 16, 24, 8)
fan.on()
falling_platforms = [Falling_platform(1000*i, 350, 32, 10) for i in range(8, 10)]
trampoline = Trampoline(10 * block_size, HEIGHT - block_size - 56, 28, 28)
trampoline2 = Trampoline(7 * block_size, HEIGHT - 5.58 * block_size, 28, 28)
pineapple = Pineapple(15 * block_size, HEIGHT - block_size - 64, 32, 32)
cherry = Cherry(1200, HEIGHT-block_size - 64, 32, 32)
speedplatforms = [SpeedPlatform(104*i, HEIGHT-block_size - 128, 32, 8) for i in range(20,30)]
checkpoint1 = Checkpoint(2100, HEIGHT-block_size - 128, 64, 64)
spikehead = Spikehead(15 * block_size, HEIGHT - block_size - 100, 50, 50)

#Liste med blocks som danner gulvet
floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, 100)]
floor2 = [Block(i * block_size, HEIGHT - 6 * block_size, block_size) for i in range(-WIDTH // block_size, 5)]
block = Block(7 * block_size, HEIGHT - 5 * block_size, block_size)
wall = [Block(12 * block_size, HEIGHT - (2 + i) * block_size, block_size) for i in range(7)]

#Liste med alle tingene som inngår i spillet
loopable = [fire, fan, pineapple, trampoline, *falling_platforms, cherry, checkpoint1, *speedplatforms, trampoline2, spikehead]
objects = [*floor, fire, *falling_platforms, spike, fan, trampoline, pineapple, cherry, checkpoint1, *speedplatforms, block, *wall, trampoline2, *floor2, spikehead]
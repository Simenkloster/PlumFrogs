from Fire import Fire
from Spike import Spike
from Fan import Fan
from Block import Block
from Player import Player
from Falling_platform import Falling_platform
from Trampoline import Trampoline
from Pineapple import Pineapple
from Cherry import Cherry

WIDTH, HEIGHT = 1000, 800
block_size = 96



#Making stuff that goes into the game
Player1 = Player(100, 100, 50, 50)
fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
fire.on()
spike = Spike(600, HEIGHT-block_size-32, 16, 16)
fan = Fan(200, HEIGHT - block_size - 16, 24, 8)
fan.on()
falling_platforms = [Falling_platform(80*i, 350, 32, 10) for i in range(8, 20)]
trampoline = Trampoline(300, HEIGHT - block_size - 56, 28, 28)
pineapple = Pineapple(700, HEIGHT - block_size - 64, 32, 32)

#Liste med blocks som danner gulvet
floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]

cherry = Cherry(1000, HEIGHT-block_size - 64, 32, 32)

#Liste med alle tingene som inngår i spillet
loopable = [fire, fan, pineapple, trampoline, *falling_platforms, cherry]
objects = [*floor, fire, *falling_platforms, spike, fan, trampoline, pineapple, cherry]
from Fire import Fire
from Spike import Spike
from Cherry import Cherry
from Fan import Fan
from Falling_platform import Falling_platform
from Trampoline import Trampoline
from Player import Player
from Block import Block

WIDTH, HEIGHT = 1200, 800
block_size = 96


Player1 = Player(100, 100, 50, 50)
fire = Fire(0, HEIGHT - block_size - 64, 16, 32)
fire.on()
spike = Spike(200, HEIGHT-block_size-32, 16, 16)
spike2 = Spike(600,(HEIGHT-block_size*6)-32, 16, 16)
cherry = Cherry(400,(HEIGHT-block_size*6)-32, 32, 32)
fan = Fan(0, HEIGHT - block_size - 16, 24, 8)
fan.on()
falling_platform = Falling_platform(200, (HEIGHT - block_size*8) - 64, 32, 10)

trampoline = Trampoline(300, HEIGHT - block_size - 56, 28, 28)

#Liste med blocks som danner gulvet
floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]
floor2 = [Block((i + 5) * block_size, HEIGHT - 6 * block_size, block_size) for i in range(4)]
floor3 = [Block((i + 5) * block_size, HEIGHT - 4 * block_size, block_size) for i in range(5)]
wallfloor3 = Block(5 * block_size, HEIGHT - 5 * block_size, block_size)
floor2wall = [Block(10*block_size, HEIGHT - (2 + i) * block_size, block_size) for i in range(7)]


#Liste med alle tingene som inngår i spillet
loopable = [fan,cherry,fire,falling_platform,trampoline]
objects = [*floor,*floor2,*floor2wall,*floor3,wallfloor3, fire, falling_platform, spike,spike2, fan, trampoline,cherry]
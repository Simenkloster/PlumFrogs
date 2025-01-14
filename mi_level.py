from Fire import Fire
from Spike import Spike
from Fruits.Cherry import Cherry
from Fan import Fan
from FallingPlatform import Falling_platform
from Trampoline import Trampoline
from Player import Player
from Block import Block
from Checkpoint import Checkpoint
from SpeedPlatform import SpeedPlatform
from Fruits.Pineapple import Pineapple
from Spikehead import Spikehead
from Goal import Goal

WIDTH, HEIGHT = 1200, 800
block_size = 96

def ML_spike(xlist,x,y,length): #1032, 5, 5
    for i in range(length):
        x = x+ 32
        xlist.append(Spike(x,(HEIGHT-block_size*5)-32, 16, 16))

Player1 = Player(100, 100, 50, 50)


fire = Fire(3200, HEIGHT - block_size - 256, 16, 32)
fire.on()
spike = Spike(200, HEIGHT-block_size-32, 16, 16)
spike2 = Spike(600,(HEIGHT-block_size*6)-32, 16, 16)
goal = Goal(3500, HEIGHT-block_size-320)

checkpoint1 = Checkpoint(1300, (HEIGHT-block_size*8) - 128, 64, 64)

cherry = Cherry(570,(HEIGHT-block_size*4.2)-32, 32, 32)
bugcherry = Cherry(1070,(HEIGHT-block_size*3.5)-32,32,32)
pineapple = Pineapple(2200, (HEIGHT - block_size*3) - 64, 32, 32)
spikehead = Spikehead(3300,(HEIGHT-block_size*3.74)-32,54,52)
spikehead2 = Spikehead(2300,(HEIGHT-block_size*3.74)-32,54,52)


fan = Fan(1550, HEIGHT - block_size - 688)
fan.on()
speedplatforms = [SpeedPlatform(2500 + 64*i, HEIGHT-block_size - 192, 32, 8) for i in range(3)]
speedplatforms2 = [SpeedPlatform(2780 + 64*i, HEIGHT-block_size - 192, 32, 8) for i in range(3)]
falling_platform = Falling_platform(2700, (HEIGHT - block_size*2.3) - 64, 32, 10)



trampoline = Trampoline(300, HEIGHT - block_size - 56, 28, 28)

#Liste med blocks som danner gulvet
floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]
floor2 = [Block((i + 5) * block_size, HEIGHT - 6 * block_size, block_size) for i in range(4)]
floor3 = [Block((i + 5) * block_size, HEIGHT - 4 * block_size, block_size) for i in range(5)]
floor4 = [Block((i + 13) * block_size, HEIGHT - 8 * block_size, block_size) for i in range(5)]
floor5 = [Block((i + 11) * block_size, HEIGHT - 5 * block_size, block_size) for i in range(3)]
wallfloor3 = Block(5 * block_size, HEIGHT - 5 * block_size, block_size)
floor2wall = [Block(10*block_size, HEIGHT - (2 + i) * block_size, block_size) for i in range(7)]
floor5wall = [Block(13*block_size, HEIGHT - (6 + i) * block_size, block_size) for i in range(2)]
floor6 = [Block((i + 19) * block_size, HEIGHT - 3 * block_size, block_size) for i in range(7)]
floor7= [Block((i + 31) * block_size, HEIGHT - 3 * block_size, block_size) for i in range(7)]
nwall1 = [Block(18*block_size, HEIGHT - (3 + i) * block_size, block_size) for i in range(6)]


#Liste med alle tingene som inngår i spillet
loopable = [fan,cherry,bugcherry,pineapple,fire,falling_platform,trampoline,checkpoint1,goal,spikehead,spikehead2]
objects = [*floor,*floor2,*floor2wall,*floor3,*floor4,*floor5,*floor6,*floor7,*floor5wall,*nwall1,wallfloor3, fire, falling_platform, spike,spike2, fan, trampoline,cherry,bugcherry,pineapple,checkpoint1,*speedplatforms2,*speedplatforms,goal,spikehead2,spikehead]
ML_spike(objects,1032, 5, 5)



    
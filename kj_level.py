import pygame
from Player import Player
from Block import Block
from Fire import Fire
from Spike import Spike
from Fan import Fan
from FallingPlatform import Falling_platform
from Trampoline import Trampoline
from Checkpoint import Checkpoint
from Goal import Goal
HEIGHT = 800

goals = [Goal(-96*42-16, HEIGHT-96*3-128)]
falling_platforms = [Falling_platform(688, HEIGHT-480), Falling_platform(1072, HEIGHT-96*3), Falling_platform(208, HEIGHT-480)]
trampolines = [Trampoline(96*-13+14, HEIGHT-96*2)]
fires = []
checkpoints = [Checkpoint(-96*34, HEIGHT-224)]
fans = [Fan(-1812, HEIGHT-16), Fan(-96*39+32, HEIGHT-96*3)]
spikes = [Spike(-96*24 +32, HEIGHT-128), Spike(-96*24 +64, HEIGHT-128), Spike(-96*25, HEIGHT-128),
            Spike(-96*25 +32, HEIGHT-128), Spike(-96*28+48, HEIGHT-128), Spike(-96*28+64, HEIGHT-128)
            , Spike(-96*7, HEIGHT-128), Spike(-96*20/3, HEIGHT-128), Spike(-96*19/3, HEIGHT-128)
            , Spike(-96*6, HEIGHT-128), Spike(-96*17/3, HEIGHT-128), Spike(-96*16/3, HEIGHT-128)
            , Spike(-96*5, HEIGHT-128), Spike(-96*14/3, HEIGHT-128), Spike(-96*13/3, HEIGHT-128)
            , Spike(-96*4, HEIGHT-128), Spike(-96*11/3, HEIGHT-128), Spike(-96*10/3, HEIGHT-128)
            , Spike(-96*3, HEIGHT-128), Spike(-96*8/3, HEIGHT-128), Spike(-96*7/3, HEIGHT-128)
            , Spike(-96*2, HEIGHT-128), Spike(-96*5/3, HEIGHT-128), Spike(-96*4/3, HEIGHT-128)
            , Spike(-96*35, HEIGHT-64), Spike(-96*36, HEIGHT-64), Spike(-96*37, HEIGHT-64), Spike(-96*38, HEIGHT-64)
            , Spike(-96*39, HEIGHT-64)
            , Spike(-96*35+32, HEIGHT-64), Spike(-96*36+32, HEIGHT-64), Spike(-96*37+32, HEIGHT-64), Spike(-96*38+32, HEIGHT-64)
            , Spike(-96*39+32, HEIGHT-64)
            , Spike(-96*35+64, HEIGHT-64), Spike(-96*36+64, HEIGHT-64), Spike(-96*37+64, HEIGHT-64), Spike(-96*38+64, HEIGHT-64)
            , Spike(-96*39+64, HEIGHT-64)]
blocks = [Block(96*7, HEIGHT-96), Block(-96*24, HEIGHT-96), Block(-96*25, HEIGHT-96), Block(-96*28, HEIGHT-96)
            , Block(-96, HEIGHT-96*2), Block(-96, HEIGHT-96*3), Block(-96, HEIGHT-96*4), Block(-96, HEIGHT-96*5)
            , Block(-96, HEIGHT-96*6), Block(-96*8, HEIGHT-96), Block(-96*7, HEIGHT-96), Block(-96*6, HEIGHT-96)
            , Block(-96*5, HEIGHT-96), Block(-96*4, HEIGHT-96), Block(96*-3, HEIGHT-96), Block(96*-2, HEIGHT-96)
            , Block(-96, HEIGHT-96), Block(0, HEIGHT-96), Block(96, HEIGHT-96), Block(-96*34, HEIGHT-96)
            , Block(-96*35, HEIGHT-96*4), Block(-96*36, HEIGHT-96*4), Block(-96*37, HEIGHT-96*4), Block(-96*38, HEIGHT-96*4)
            , Block(-96*35, HEIGHT-32), Block(-96*36, HEIGHT-32), Block(-96*37, HEIGHT-32), Block(-96*38, HEIGHT-32)
            , Block(-96*39, HEIGHT-32), Block(-96*39, HEIGHT-96*4), Block(-96*42, HEIGHT-96*3)]
loopable = [*falling_platforms, *fires, *trampolines, *fans, *checkpoints, *goals]
objects = [*loopable, *blocks, *spikes]
player_pos = [100, HEIGHT-146]
player_hp = 1


for fan in fans:
    fan.on()
for fire in fires:
    fire.on()
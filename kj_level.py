import pygame
from Player import Player
from Block import Block
from Fire import Fire
from Spike import Spike
from Fan import Fan
from Falling_platform import Falling_platform
from Trampoline import Trampoline
HEIGHT = 800

falling_platforms = [Falling_platform(688, HEIGHT-480), Falling_platform(1072, HEIGHT-96*3), Falling_platform(208, HEIGHT-480)]
trampolines = [Trampoline(96*-13+14, HEIGHT-96*2)]
fires = []
fans = [Fan(-1812, HEIGHT-16)]
spikes = [Spike(96*-24 +32, HEIGHT-128), Spike(96*-24 +64, HEIGHT-128), Spike(96*-25, HEIGHT-128),
            Spike(96*-25 +32, HEIGHT-128), Spike(96*-28+48, HEIGHT-128), Spike(96*-28+64, HEIGHT-128)
            , Spike(96*-7, HEIGHT-128), Spike(96*-20/3, HEIGHT-128), Spike(96*-19/3, HEIGHT-128)
            , Spike(96*-6, HEIGHT-128), Spike(96*-17/3, HEIGHT-128), Spike(96*-16/3, HEIGHT-128)
            , Spike(96*-5, HEIGHT-128), Spike(96*-14/3, HEIGHT-128), Spike(96*-13/3, HEIGHT-128)
            , Spike(96*-4, HEIGHT-128), Spike(96*-11/3, HEIGHT-128), Spike(96*-10/3, HEIGHT-128)
            , Spike(96*-3, HEIGHT-128), Spike(96*-8/3, HEIGHT-128), Spike(96*-7/3, HEIGHT-128)
            , Spike(96*-2, HEIGHT-128), Spike(96*-5/3, HEIGHT-128), Spike(96*-4/3, HEIGHT-128)]
blocks = [Block(96*7, HEIGHT-96), Block(96*-24, HEIGHT-96), Block(96*-25, HEIGHT-96), Block(96*-28, HEIGHT-96)
            , Block(-96, HEIGHT-96*2), Block(-96, HEIGHT-96*3), Block(-96, HEIGHT-96*4), Block(-96, HEIGHT-96*5)
            , Block(-96, HEIGHT-96*6), Block(96*-8, HEIGHT-96), Block(96*-7, HEIGHT-96), Block(96*-6, HEIGHT-96)
            , Block(96*-5, HEIGHT-96), Block(96*-4, HEIGHT-96), Block(96*-3, HEIGHT-96), Block(96*-2, HEIGHT-96)
            , Block(-96, HEIGHT-96), Block(0, HEIGHT-96), Block(96, HEIGHT-96)]
loopable = [*falling_platforms, *fires, *trampolines, *fans]
objects = [*loopable, *blocks, *spikes]
player_pos = [100, HEIGHT-146]

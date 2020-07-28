# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:29:59 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random 
while True:
    tnt_minecart = random.randrange(407,408)
    x,y,z = mc.player.getTilePos()
    
    mc.setBlock(x,y,z-1,407,tnt_minecart
                )
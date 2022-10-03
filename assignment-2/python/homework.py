'''
Version 0.01
Last Edited: 10/3/2022
Script Description: Launch Maya standalone, X, save Maya file
'''


#Import and launch Maya standalone
import maya.standalone
maya.standalone.initialize()

#Import
import maya.cmds
import argparse

print("Creating a cube...")
maya.cmds.polyCube()
print(maya.cmds.ls(geometry=True))

#Save Maya file

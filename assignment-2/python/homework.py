'''
Version 0.01
Last Edited: 10/3/2022
Script Description: Launch Maya standalone, X, save Maya file
'''


#Import and launch Maya standalone
import maya.standalone
maya.standalone.initialize()

#Import
import maya.cmds as cmds
import argparse
import os

#Maya file
print("Creating a cube...")
maya.cmds.polyCube()
print(maya.cmds.ls(geometry=True))


#Save a Maya file to python script directory
savePath= os.getcwd()
print("Saving to...", savePath)
saveFile = savePath + '\\sis47_as02.ma'
cmds.file(rename=saveFile)
cmds.file(save=True, type="mayaAscii")

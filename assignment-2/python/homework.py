'''
Version 0.01
Last Edited: 10/3/2022
Script Description: Launch Maya standalone, create bouncing ball anim, save Maya file
'''


#Import
import maya.standalone
import maya.cmds as cmds
import argparse
import os

#Get Arguements
parser = argparse.ArgumentParser(description='This program makes a bouncing ball animation')
parser.add_argument('ballSize', type=int, help='The radius of the ball')
parser.add_argument('startHeight', type=int, help='Starting height of bouncing ball')
args = parser.parse_args()

#Initialize Maya
maya.standalone.initialize()

#Create Ball
ball="bouncingBall"
print("Creating a bouncy ball...")
cmds.polySphere(name=ball, radius=args.ballSize)
cmds.setAttr(ball+'.translateY',(int(args.ballSize)))
cmds.makeIdentity(ball, apply=True, t=1)
cmds.delete(ball, ch=True)
cmds.setAttr(ball+'.translateY',(int(args.startHeight)))

#Animate Ball
bounce=int(args.startHeight)
time = int(args.startHeight)
interval = float(args.startHeight)
cmds.setKeyframe(ball, attribute='translateY', t=0)

while bounce > 1:
    cmds.setAttr(ball+'.translateY',0)
    cmds.setKeyframe(ball, attribute='translateY', t=time)
    
    bounce = float(bounce/2)
    interval = interval/2
    time += int(interval)
    
    #print("Bounce:",bounce)
    #print("Interval:", interval)
    #print("Time:",time)
    
    cmds.setAttr(ball+'.translateY',bounce)
    cmds.setKeyframe(ball, attribute='translateY', t=time)
    
    time += int(interval)
    

#Save a Maya file to python script directory
savePath= os.getcwd()
print("Saving to...", savePath)
saveFile = savePath + '\\sis47_as02.ma'
cmds.file(rename=saveFile)
cmds.file(save=True, type="mayaAscii")

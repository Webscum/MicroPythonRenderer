#This loads an object, object selected from device memory, renders it and does some other intresting stuff

import MicroObjLoader # Seperate file that makes an obj file to an python dictionary
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
from math import sin,cos,acos,sqrt,degrees,pi

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)

MOL = MicroObjLoader.LoadObj("Models/monkelp.obj")

camPos = [0.0,0.0,20.0] # The x, y, z, of the camera position
camDir = [0.0,0.0,-1.0] # Angles in pitch (x), head (y), roll (z)
middle = [64, 32] #The middle of the screen

def Head(pos, sin, cos):
    
    x = pos[0]
    z = pos[2]
    
    pos[0] = x*cos + z*sin
    pos[2] = z*cos - x*sin
    
 
def Pitch(pos, sin, cos):
    
    y = pos[1]
    z = pos[2]
    
    pos[1] = cos*y - sin*z
    pos[2] = cos*z + sin*y
    
def Roll(pos, sin, cos):
    
    x = pos[0]
    y = pos[1]
    
    pos[0] = cos*x - sin*y
    pos[1] = cos*y + sin*x
    
def IndpFaceEulerRot(x = .0 ,y = .0,z = .0):    
    for f in MOL["Faces"]:
        EulerRot(f[1],x,y,z)

def IndpVertEulerRot(x = .0 ,y = .0,z = .0):    
    for v in MOL["Vertices"]:
        EulerRot(v,x,y,z)

def IndpEulerRot(x = .0 ,y = .0,z = .0):
    IndpVertEulerRot(x,y,z)
    IndpFaceEulerRot(x,y,z)

def EulerRot(v,x = .0,y = .0,z = .0):
    if x:
        Pitch(v, sin(x), cos(x))
    if y:
        Head(v, sin(y), cos(y))
    if z:
        Roll(v, sin(z), cos(z))
        
while 1:
    oled.fill(0)
         
    IndpVertEulerRot(y = 0.05)
    
         
    for face in MOL["Faces"]:
        EulerRot(face[1], y = 0.05)
        
        timed = face[1][0]*-camDir[0]+face[1][1]*-camDir[1]+face[1][2]*-camDir[2]
        
        fm = sqrt(face[1][0]**2 + face[1][1]**2 + face[1][2]**2)
        cdm = sqrt(camDir[0]**2 + camDir[1]**2 + camDir[2]**2)
        
        angle = abs(acos(timed/(fm*cdm)))
        
        if angle < pi/2:
            points = []
            for point in face[0]:
                points.append([round(MOL["Vertices"][point - 1][0] * camPos[2]) + middle[0], round(MOL["Vertices"][point - 1][1] * camPos[2]) + middle[1]])
            for p in range(len(points)):
                oled.line(points[p][0],points[p][1],points[(p+1)%len(face[0])][0],points[(p+1)%len(face[0])][1],1)
            
        
    oled.show()
    

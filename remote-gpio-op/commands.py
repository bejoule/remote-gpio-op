import struct
from utils import *

def blankRead():
    print('blank read called')
    return struct.pack('IIII',0,0,0,536904191)

def setMode(command,p1,p2):
    print('set mode called')
    success=True
    if(success):
        return struct.pack('IIII',command,p1,p2,0)
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def getMode(command,p1,p2):
    print('get mode called')
    success=True
    mode=0
    if(success):
        return struct.pack('IIII',command,p1,p2,i2u(mode))
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def writeDigital(command,p1,p2):
    print('write called')
    success=True
    if(success):
        return struct.pack('IIII',command,p1,p2,0)
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def readDigital(command,p1,p2):
    print('read called')
    success=True
    val=1
    if(success):
        return struct.pack('IIII',command,p1,p2,i2u(val))
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def getHwVersion(command,p1,p2):
    print('get hw version called')
    success=True
    val=1
    if(success):
        return struct.pack('IIII',command,p1,p2,10494082)
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def setPullUpDown(command,p1,p2):
    print('set pull up down called')
    success=True
    val=1
    if(success):
        return struct.pack('IIII',command,p1,p2,0)
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def defaultResponse(command,p1,p2):
    print(f'{command} called')
    return struct.pack('IIII',command,p1,p2,0)

def closeConnection(writer,remove):
    return [x for x in writer if x != remove]
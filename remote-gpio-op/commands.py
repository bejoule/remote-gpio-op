import struct
import wiringpi as pi
from utils import *

def init():
    try:
        pi.wiringPiSetup()
        return 
    except:
        print('Failed to initialize wiringpi')
        return 0

def blankRead():
    print('blank read called')
    buf = 0
    for i in range(22):
        try:
            buf = buf | pi.getAlt(i)<<i           
        except:
            print(f'Cannot read pin {i}')
            
    return struct.pack('IIII',0,0,0,536904191) #dummy black read return raspberry pi configuration

def setMode(command,p1,p2):
    print('set mode called')
    success=True
    try:
        pi.pinMode(p1,p2)
    except:
        success=False
        print(f'Cannot set mode on pin {p1}')
    
    if(success):
        return struct.pack('IIII',command,p1,p2,0)
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def getMode(command,p1,p2):
    print('get mode called')
    success=True
    try:
        mode = pi.getAlt(p1)
    except:
        success = False
        print(f'Cannot get mode on pin {p1}')
        
    if(success):
        return struct.pack('IIII',command,p1,p2,i2u(mode))
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def writeDigital(command,p1,p2):
    print('write called')
    success=True
    try:
        pi.digitalWrite(p1,p2)
    except:
        success = False
        print(f'Cannot write pin {p1}')
        
    if(success):
        return struct.pack('IIII',command,p1,p2,0)
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def readDigital(command,p1,p2):
    print('read called')
    success=True
    try:
        val = pi.digitalRead(p1)
    except:
        success = False
        print(f'Cannot read pin {p1}')
    
    if(success):
        return struct.pack('IIII',command,p1,p2,i2u(val))
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def getHwVersion(command,p1,p2):
    print('get hw version called')
    success=True
    
    if(success):
        return struct.pack('IIII',command,p1,p2,10494082) #dummy black read return raspberry pi configuration
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def setPullUpDown(command,p1,p2):
    print('set pull up down called')
    success=True
    try:
        pi.pullUpDnControl(p1,p2)
    except:
        success = False
        print(f'Cannot set pull up down pin {p1}')
    
    if(success):
        return struct.pack('IIII',command,p1,p2,0)
    else:
        return struct.pack('IIII',command,p1,p2,i2u(-1))

def defaultResponse(command,p1,p2):
    print(f'{command} called')
    return struct.pack('IIII',command,p1,p2,0)

def closeConnection(writer,remove):
    return [x for x in writer if x != remove]
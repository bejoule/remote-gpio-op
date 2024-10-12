import wiringpi
from constants import *

def readAll31():
	buf=0
	for i in range(32):
		try:
			buf = buf | wiringpi.readDigital(i)<<i
		exept:
			print(f'Cannot read pin {i}')

def setPinMode(pin,mode):
	try:
		wiringpi.pinMode(pin,mode)
	exept:
		print(f'Cannot set pin {pin} mode'

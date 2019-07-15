from gpiozero import LED
from time import sleep
from signal import pause

red = LED(17)
yellow = LED(15)
green = LED(14)


while True:
	red.on()
	sleep(1)
	red.off()
	green.on()
	sleep(1)
	green.off()
	yellow.on()
	sleep(1)
	yellow.off()

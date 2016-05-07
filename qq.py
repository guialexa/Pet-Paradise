
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(29,GPIO.IN)
GPIO.setup(18, GPIO.OUT)#trig
GPIO.setup(16, GPIO.IN) #echo

def OFF(pin):
    GPIO.setup(13 ,GPIO.OUT)
    GPIO.setup(12 ,GPIO.OUT)
    GPIO.setup(15 ,GPIO.OUT)
    GPIO.setup(11 ,GPIO.OUT)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(15,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    GPIO.setup(7 ,GPIO.OUT)
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(11,GPIO.HIGH)

def WALK(pin):
	GPIO.output(7,GPIO.LOW)
	GPIO.output(11,GPIO.HIGH)	
	GPIO.output(13,GPIO.HIGH)		
	GPIO.output(18, False)
	time.sleep(0.3)
	GPIO.output(18, True)
	time.sleep(0.00001)
	GPIO.output(18, False)

	while GPIO.input(16)==0:
		signalOff=time.time()

	while GPIO.input(16)==1:
		signalOn=time.time()

	timePassed=signalOn-signalOff
	distance=timePassed*17150

	print distance,"cm"

	if distance <=75:
		if distance >10:
			GPIO.output(11,GPIO.LOW)
			sleep(0.6)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(7, GPIO.LOW) 
			sleep(6)
			GPIO.output(7, GPIO.HIGH)
			GPIO.output(13, GPIO.LOW)
			sleep(0.6)
			GPIO.output(13, GPIO.HIGH)
			GPIO.output(7, GPIO.LOW)

def HOOK(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(15,GPIO.IN)
	GPIO.setup(12,GPIO.OUT)
	input_value=GPIO.input(15)
	if input_value ==False:
		print ('button1 has been pressed...')
		OFF(13)

		for i in range(0,1):
			sleep(30)
			GPIO.output(12,GPIO.LOW)
			sleep(20)
			GPIO.output(12,GPIO.HIGH)
			sleep(10)


	input_value=GPIO.input(15)

def DOG(pin):

    GPIO.output(11,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)		
    GPIO.output(18, False)
    time.sleep(0.5)
    GPIO.output(18, True)
    time.sleep(0.5)
    GPIO.output(18, False)

    while GPIO.input(16)==0:
		signalOff=time.time()

    while GPIO.input(16)==1:
		signalOn=time.time()

    timePassed=signalOn-signalOff
    distance=timePassed*17150

    print distance,"cm"

    if distance <= 75:
		if distance >10:
			GPIO.output(7,GPIO.HIGH)
        		GPIO.output(11,GPIO.LOW)
			sleep(0.6)
        		GPIO.output(11,GPIO.HIGH)
			GPIO.output(7, GPIO.LOW) 
			sleep(6)
			GPIO.output(7, GPIO.HIGH)
			GPIO.output(13, GPIO.LOW)
			sleep(1.8)
			GPIO.output(13, GPIO.HIGH)
			GPIO.output(7, GPIO.LOW)
			sleep(6)
			GPIO.output(7, GPIO.HIGH)
			GPIO.output(11, GPIO.LOW)	
			sleep(0.6)
			GPIO.output(11, GPIO.HIGH)
	
def TURN(pin):
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)		
    GPIO.output(18, False)
    time.sleep(0.5)
    GPIO.output(18, True)
    time.sleep(0.5)
    GPIO.output(18, False)

    while GPIO.input(16)==0:
		signalOff=time.time()

    while GPIO.input(16)==1:
		signalOn=time.time()

    timePassed=signalOn-signalOff
    distance=timePassed*17150

    print distance,"cm"
    GPIO.output(13, GPIO.LOW)
    sleep(8)
    GPIO.output(13,GPIO.HIGH)

while True:

	OFF(13)
	sleep(10)
	WALK(18)

	while WALK(18):
		HOOK(15)
		if HOOK(15):
			print 'hook'
			sleep(2)
			print 'dog'
			DOG(7)
			sleep(60)
			print 'turn'
			TURN(13)
			print 'walk'
			WALK(18)


GPIO.cleanup()
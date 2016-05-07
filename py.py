import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def Food(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	Servo=GPIO.PWM(pin,45)
	Servo.start(5)

	Servo.ChangeDutyCycle(5)
	time.sleep(1)            
	Servo.ChangeDutyCycle(100)
	time.sleep(1)
	Servo.ChangeDutyCycle(0.5)
	time.sleep(0.5)
	Servo.stop()

def On(pin):
	GPIO.setup(11 ,GPIO.OUT)
	GPIO.output(11,GPIO.HIGH)
	sleep(7)
	GPIO.output(11,GPIO.LOW)
	GPIO.cleanup()

def DoorO(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(23, GPIO.OUT)
	print "door:3 s"
	sleep(1)
	print "door:2 s"
	sleep(1)
	print "door:1 s"
	sleep(1)
	print "The door is opening"
	Servo=GPIO.PWM(23,45)
	Servo.start(5)

	Servo.ChangeDutyCycle(5)
	time.sleep(0)
	Servo.stop()
	sleep(20)

def DoorC(pin):
	Servo=GPIO.PWM(23,45)
	Servo.start(50)            
	Servo.ChangeDutyCycle(50)
	time.sleep(0.65)
	Servo.stop()

def Close(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(23, GPIO.OUT)
	Servo=GPIO.PWM(23,35)
	Servo.start(45)
	Servo.ChangeDutyCycle(1)
	time.sleep(2)
	Servo.stop(1)


def readInput (PiPin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PiPin,GPIO.IN)
	return GPIO.input(PiPin)

def ReadDistance(pin):
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)
	sleep(0.2)
	GPIO.output(pin,1)
	sleep(0.5)
	GPIO.output(pin,0)
	GPIO.setup(pin,GPIO.IN)
	
	while GPIO.input(pin)==0:
		starttime=time.time()
	
	while GPIO.input(pin)==1:
		endtime=time.time()

	duration=endtime-starttime
	distance=duration*17150
	return distance

def Water(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.IN)
	print "water:", readInput (12)
	print "light:", GPIO.input(7)
	time.sleep(2)
	if GPIO.input(12)==0:
        	GPIO.setup(13, GPIO.OUT)
		GPIO.output(13,GPIO.HIGH)

	if GPIO.input(12)==1:
        	GPIO.setup(13, GPIO.OUT)	
		GPIO.output(13,GPIO.LOW)

def Garage(pin):


	while True:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(40, GPIO.IN)
		distance= ReadDistance(40)
		print "distance:",distance
		if distance <7:
			if distance >2:
				GPIO.setup(18, GPIO.OUT)
				Servo=GPIO.PWM(18,60)
				Servo.start(10)

				for i in range(0,1):
					Servo.ChangeDutyCycle(0.5)
					time.sleep(0.1)                     
					Servo.ChangeDutyCycle(0.5)
					time.sleep(0.1)
					Servo.ChangeDutyCycle(0.5)
					time.sleep(0.1)                     
					Servo.ChangeDutyCycle(0.5)
					time.sleep(0.9)
                                        
                                                                   
				Servo.stop()
				sleep(7)
			Servo=GPIO.PWM(18,50)
			Servo.start(10)


			for i in range(0,7):
      
				Servo.ChangeDutyCycle(10)
				time.sleep(0.07)
 				Servo.ChangeDutyCycle(10)
				time.sleep(0.1)

			Servo.stop()

while True:
	sleep(2)
	Garage(40)
	sleep(7)
	On(11)
	DoorO(23)
	Water(7)
	Food(38)
	DoorC(23)
	sleep(5)
	Water(7)
	DoorO(23)
	Food(38)
	Water(7)
	DoorC(23)
	
	
	
	

if KeyboardInterrupt:
	GPIO.cleanup()


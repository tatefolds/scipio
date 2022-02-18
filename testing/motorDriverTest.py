import RPi.GPIO as GPIO
import time

pwmPin = 13
a1Pin = 17
a2Pin = 27
stbyPin = 22

#disables the warnings about restarting without cleanup, setmode reads GPIO number not board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#initializes pins
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.output(pwmPin, GPIO.LOW)
GPIO.setup(a1Pin, GPIO.OUT)
GPIO.output(a1Pin, GPIO.LOW)
GPIO.setup(a2Pin, GPIO.OUT)
GPIO.output(a2Pin, GPIO.LOW)
GPIO.setup(stbyPin, GPIO.OUT)
GPIO.output(stbyPin, GPIO.HIGH)

pwm = GPIO.PWM(pwmPin, 100000)      #sets PWM frequency to 100kHz
pwm.start(0)
#GPIO.output(pwmPin, GPIO.HIGH)     #test code for non pwm
time.sleep(0.4)

pwm.ChangeDutyCycle(100)
time.sleep(0.01)
GPIO.output(a1Pin, GPIO.HIGH)
print("one way")
time.sleep(3)
GPIO.output(a2Pin, GPIO.HIGH)
print("stop")
time.sleep(1)
GPIO.output(a1Pin, GPIO.LOW)
print("other way")
time.sleep(3)
GPIO.output(a2Pin, GPIO.LOW)
print("stop")
time.sleep(1)

#GPIO.output(pwmPin, GPIO.HIGH)     #test code for non-pwm
pwm.stop
GPIO.cleanup()
print("done")


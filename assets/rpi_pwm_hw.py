##python3
import RPi.GPIO as GPIO
#import the RPi.GPIO library

from time import sleep

print("startup")

GPIO.setwarnings(False)
#import the sleep from time library
GPIO.setmode(GPIO.BCM)

ledpin = 18

#declare the GPIO 18 pin for the output of LED

GPIO.setup(ledpin,GPIO.OUT)

#define the behaviour of the ledpin as output



#ignore the warnings

pwm = GPIO.PWM(ledpin,1000)

#create the pwm instance with frequency 1000 Hz

pwm.start(0)

#start the pwm at 0 duty cycle


pwm.ChangeFrequency(1000)   # where freq is the new frequency in Hz

pwm.ChangeDutyCycle(10)  # where 0.0 <= dc <= 100.0




foo = True

while foo:

#initialise the infinite while loop

    for duty in range(0,101):

#initialise the for loop

        pwm.ChangeDutyCycle(duty)

#changing the duty cycle according to the value of for loop

        sleep(0.01)

#generated the delay of 0.01 second in every iteration of for loop

    sleep(0.5)

#generated the delay of 0.5 seconds

    for duty in range(100,-1,-1):

#again started the for loop be setting its value of 100 and decremented by -1 till -1

        pwm.ChangeDutyCycle(duty)

#changing the duty cycle according to the value of for loop

        sleep(0.01)

#generated the delay of 0.01 second in every iteration of for loop

    sleep(0.5)
    
    foo = False

#generated the delay of 0.5 second

print ("foo")


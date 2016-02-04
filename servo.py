import RPi.GPIO as GPIO
import time

print " Values must be between -90 and 90"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)

pwm = GPIO.PWM(18,50)

pwm.start(5)

while (True):

    

    x = raw_input('--> ')
    
    if type(int(x)) == int and int(x) <= int(90) and x >= int(-90):
        DC = 1.9+(0.045*(int(x)+90))
        print "%r" % DC
        pwm.ChangeDutyCycle(DC)
        time.sleep(1)        
    else:
        print "Quitting..."
        break
    

    

pwm.stop()    
GPIO.cleanup()


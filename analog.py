import RPi.GPIO as GPIO
import ADC0834
from time import sleep
GPIO.setmode(GPIO.BCM)
button=21
LED=16

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
LEDstate=False
ADC0834.setup()

LEDpwm=GPIO.PWM(LED,1000)
LEDpwm.start(0)
buttonstateold=GPIO.input(button)

try:
    while True:
        X=ADC0834.getResult(0)
        Y=ADC0834.getResult(1)
        buttonstate=GPIO.input(button)
        print('Xvalue',X,'Yvalue',Y,'button',buttonstate)
        DC=(X/255)*100
        sleep(0.3)
        if buttonstate==GPIO.LOW and buttonstateold==GPIO.HIGH:
            LEDstate= not LEDstate
            GPIO.output(LED,LEDstate)
            sleep(0.3)
        if LEDstate:
            LEDpwm.ChangeDutyCycle(DC)
        else:
            LEDpwm.ChangeDutyCycle(0)
        buttonstateold=buttonstate            
except KeyboardInterrupt:
    LEDpwm.stop()
    GPIO.cleanup()

This is the code for SunFounder Da Vinci Kit for Raspberry Pi. This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied wa rranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

davinci-kit-for-raspberry-pi comes with ABSOLUTELY NO WARRANTY; for details run ./show w. This is free software, and you are welcome to redistribute it under certain conditions; run ./show c for details.

SunFounder, Inc., hereby disclaims all copyright interest in the program 'davinci-kit-for-raspberry-pi' (which makes passes at compilers).

Mike Huang, 21 August 2015

Mike Huang, Chief Executive Officer

Modified by ishi-0409, 2025

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

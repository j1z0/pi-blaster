import sys
import os

SERVO = 18
if __name__ == "__main__":
    #gpio.setmode(gpio.BOARD)
    #servo = PWM.Servo()
    #servo(12,7000) 
    #gpio.setup(SERVO, RPIO.OUT)

    for i in range(180):
        os.system('echo "%d=%f" > /dev/pi-blaster' % (SERVO, .7))
    




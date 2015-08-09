import RPi.GPIO as gpio
import time

class Motor(object):

    def __init__(self, on_pin, ctrl1pin=None, ctrl2pin=None, direction=None):
        self.on_pin = on_pin
        gpio.setup(self.on_pin, gpio.OUT, initial=0)

	self.ctrl1pin = ctrl1pin
        gpio.setup(self.ctrl1pin, gpio.OUT)

        self.ctrl2pin = ctrl2pin
        gpio.setup(self.ctrl2pin, gpio.OUT)

        if direction:
            self.direction = direction

    @property
    def direction(self):
      return self._direction

    @direction.setter
    def direction(self, dir):
        if dir == "clockwise":
            gpio.output(self.ctrl1pin, True)
            gpio.output(self.ctrl2pin, False)
        elif dir == "counter-clockwise":
            gpio.output(self.ctrl1pin, False)
            gpio.output(self.ctrl2pin, True)
        else:
            raise ValueError("please provider either 'clockwise' or 'counter-clockwise'")

        self._direction = dir

    def on(self,duration):
       try:
           duration = float(duration)
       except ValueError:
           raise ValueError("duration needs to be an integer or floating number, got %s" % (duration))

       gpio.output(self.on_pin, True)
       time.sleep(duration) 
       gpio.output(self.on_pin, False)


    def off(self):
        gpio.output(self.on_pin, False)

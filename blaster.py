import RPi.GPIO as gpio
import time
from servoctrl import Servo
from motorctrl import Motor


class Trigger(Motor):

   def __init__(self):
     super(Trigger, self).__init__(11,8,10, "counter-clockwise")

   def fire(self, shots=1):
     self.on(shots*0.7)


def sentry_mode(servo, trigger,fire=False):
    try:
      while True:
        for i in range(20, 160):
          servo.move(i)
          time.sleep(.05)
          if (not(i % 10)) and fire:
            trigger.fire(1)
            time.sleep(1)
            print "shot fired"

        for j in range(160,20,-1):
          servo.move(j)
          time.sleep(.05)
          if (not(j % 10)) and fire:
            trigger.fire(1)
            time.sleep(1)
            print "shot fired"
    except:
      pass


def start():
  print "Arming Blaster.."
  servo = Servo(18) #this uses broadcom pin numbering
  trigger = Trigger()
  
  print "Calibrating field of view"
  print servo.full_left
  print servo.center
  print servo.full_right
  #for i in range(180):
  #  servo.move(i)
  #  time.sleep(0.05)

  servo.move(servo.center)
  print "Ready for action"

  try:
    while True:
      response = raw_input("what is your command: ")
      if response:
          command = response[0]
          cmd_args = response[1:]
          if command == 'm':
              print "moving to angle", cmd_args 
              servo.move(int(cmd_args))
          elif command == 'f':
              print "Fire in the hole"
              trigger.fire(int(response[1:]))
          elif command == 's':
              print "Sentry Mode"
              sentry_mode(servo, trigger)
          elif command == 'k':
              print "Kill all Mode"
              sentry_mode(servo, trigger, fire = True)
          else:
	      print "command not recoqnized"
  except:
    servo.shutdown()
    gpio.cleanup()

if __name__ == "__main__":
  gpio.setmode(gpio.BOARD)
  start()
  '''
  trigger = 12
  trigger_ctr_1 = 8
  trigger_ctr_2 = 10
  gpio.setup(trigger, gpio.OUT)
  gpio.setup(trigger_ctr_1, gpio.OUT)
  gpio.setup(trigger_ctr_2, gpio.OUT)
  gpio.output(trigger_ctr_1, 0)
  gpio.output(trigger_ctr_2, 1)
  trigger = Trigger()
  while True:
    shots = raw_input("How many shots to fire:")
    trigger.fire(float(shots))
    #gpio.output(trigger, True)
    #time.sleep(.5)
    #gpio.output(trigger, False)
  '''

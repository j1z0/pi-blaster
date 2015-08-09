import RPi.GPIO as gpio

class Servo(object):

  def __init__(self,pin):
    self.pin = pin
    gpio.setup(self.pin, gpio.OUT)
    #most servo's need 50 hrtz
    self.pwm = gpio.PWM(self.pin, 50)
    self.pwm.start(self.calc_duty_cycle(self.center))

  def calc_duty_cycle(self, angle):
    return (1.0/18.0) * angle +2

  @property
  def center(self):
    return 90

  @property
  def full_left(self):
    return 0

  @property
  def full_right(self):
    return 180

  def move(self, angle):
    servo_pwr = self.calc_duty_cycle(angle)
    self.pwm.ChangeDutyCycle(servo_pwr)

  def shutdown(self):
    self.pwm.stop()

if __name__ == "__main__":
   gpio.setmode(gpio.BOARD)
   num = raw_input("using BOARD mode what pin is your servo connected to?")
   servo = Servo(int(num))
   print "started"
   try:
     while True:
       angle = raw_input("What angle? ")
       servo.move(int(angle))
       #servo.move(servo.full_right)
       #servo.move(servo.full_left)
   except:
     servo.shutdown()
     gpio.cleanup()

import pigpio

class Servo(object):

  def __init__(self,pin):
    '''
    we need Broadcom pin numbers, not the actuall pin numbers
    '''
    self.pin = pin
    self.pi = pigpio.pi()
    self.pi.set_mode(self.pin, pigpio.OUTPUT)
    #self.pi.set_servo_pulsewidth(self.pin, self.center)

  def calc_duty_cycle(self, angle):
    return (95.0/9.0) * angle + 550

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
    pw = self.calc_duty_cycle(angle)
    print(pw)
    self.pi.set_servo_pulsewidth(self.pin, pw)

  def shutdown(self):
    self.pi.set_servo_pulsewidth(self.pin, 0)
    self.pi.stop()

if __name__ == "__main__":
   num = raw_input("using Broadcome mode what pin is your servo connected to?")
   servo = Servo(int(num))
   print "started"
   try:
     while True:
       angle = raw_input("What angle? ")
       servo.move(int(angle))
   except Exception as e:
     print(e) 
     servo.shutdown()
     #gpio.cleanup()

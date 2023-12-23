from gpiozero import MotionSensor
from gpiozero import LED
from gpiozero import Buzzer
from time import sleep

# Looking at PIR sensor, where three pins are at the top,
# Left pin: +5V
# Middle pin: Control (P25 as below)
# Right pin: Ground
# Both potentiometers are turned all the way to the left
pir = MotionSensor(25)

led = LED(14)
buzzer = Buzzer(15) # will work when red button is on

while True:
  pir.wait_for_motion()
  led.on()
  buzzer.on()
  print("You moved ")
  pir.wait_for_no_motion()
  buzzer.off()
  led.off()
  #sleep(3)


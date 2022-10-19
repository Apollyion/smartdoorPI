import RPi.GPIO as GPIO
import time
import drivers

display = drivers.Lcd()
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
cont = 1
op = True
try:
  while True:
      
    time.sleep(0.005)
    display.lcd_clear()
    display.lcd_display_string(str(cont),1)
    print(cont)
    p.ChangeDutyCycle(cont)
    if op:
        cont = cont+1
        if cont >= 4:
            op = False
    else:
        cont = cont-1
        if cont <= 1:
            op = True

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

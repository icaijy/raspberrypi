# 在这里写上你的代码 :-)
from RPi import GPIO

pins = (10,11, 12,13)
GPIO.setmode(GPIO.BOARD)    # give GPIO actual pins
GPIO.setwarnings(False)   # ignore warning
GPIO.setup(pins, GPIO.OUT)  # set pin mode is out
GPIO.output(pins, GPIO.LOW)   # 0V, close

# init
for x in pins:
    a = GPIO.PWM(x, 2000)   # 2KHz
    a.start(1)
    input(str(x))
    a.stop()

GPIO.output(pins, GPIO.LOW)
GPIO.cleanup()
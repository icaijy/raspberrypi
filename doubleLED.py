from RPi import GPIO
from time import sleep

pins = (11, 12)
GPIO.setmode(GPIO.BOARD)    # give GPIO actual pins
GPIO.setwarnings(False)   # ignore warning
GPIO.setup(pins, GPIO.OUT)  # set pin mode is out
GPIO.output(pins, GPIO.LOW)   # 0V, close

# init
p_R = GPIO.PWM(pins[0], 2000)   # 2KHz
p_G = GPIO.PWM(pins[1], 2000)   # 2KHz

# init(led close)
try:
    while True:
        sleep(0.5)
        p_G.stop()
        p_R.start(1)
        sleep(0.5)
        p_R.stop()
        p_G.start(1)
except KeyboardInterrupt:
    p_G.stop()
    p_R.stop()
    GPIO.output(pins, GPIO.LOW)
    GPIO.cleanup()
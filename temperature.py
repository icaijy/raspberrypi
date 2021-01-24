with open('/sys/bus/w1/devices/28-012043f4ae4b/w1_slave', 'r') as tf:
    print(int(tf.read().split("\n")[1].split(" ")[-1].replace("t=", ""))/1000)
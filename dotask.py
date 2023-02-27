from __future__ import division
import time
import Adafruit_PCA9685
import numpy as np
import re, ast

#file = open('firsttask.txt','r')
#taskarray = a*teacharray+b
file = open('smoothtask.txt','r')
smootharray = file.read()
#smootharray = np.loadtxt('smoothtask.txt', dtype=int)
smootharray = re.sub('\s+', ',', smootharray)
smootharray = np.array(ast.literal_eval(smootharray))
file.close()
#print(content)
#content = file.read() 
#colist = smootharray.split("\n")
#def colist(zeilen):
    
    
#file.close()

pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

for i,row in enumerate(smootharray):
    pwm.set_pwm(0, 0, round(smootharray[i][0]))
    pwm.set_pwm(1, 0, round(smootharray[i][1]))
    pwm.set_pwm(2, 0, round(smootharray[i][2]))
    pwm.set_pwm(3, 0, round(smootharray[i][3]))
    pwm.set_pwm(4, 0, round(smootharray[i][4]))
    pwm.set_pwm(5, 0, round(smootharray[i][5]))
    time.sleep(0.001)


pwm = Adafruit_PCA9685.PCA9685()
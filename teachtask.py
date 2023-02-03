from time import sleep
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO
import numpy as np
SPI = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
MCP3008_CS = digitalio.DigitalInOut(board.D22)
MCP3008_SPI = MCP3008.MCP3008(SPI, MCP3008_CS)
ADC_CH0 = AnalogIn(MCP3008_SPI, MCP3008.P0)
ADC_CH1 = AnalogIn(MCP3008_SPI, MCP3008.P1)
ADC_CH2 = AnalogIn(MCP3008_SPI, MCP3008.P2)
ADC_CH3 = AnalogIn(MCP3008_SPI, MCP3008.P3)

file = open('firsttask.txt','w+')
try:
    while True:
        print(file.write(f"{ADC_CH0.voltage:4.2f}   {ADC_CH1.voltage:4.2f}  {ADC_CH2.voltage:4.2f}  {ADC_CH3.voltage:4.2f}\n"))
        sleep(1)
except KeyboardInterrupt:
    RPi.GPIO.cleanup()
file.close()
taskarray = np.loadtxt('firsttask.txt')
#print(taskarray[1][1])
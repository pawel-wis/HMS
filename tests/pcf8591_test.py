import smbus
import time
import unittest

BUS_ADDR = 1 # /dev/i2c-1
PCF8591_ADDR = 0x48
AIN1 = 0x40 # photoresistor jumpered to AIN1

class TestPCF8591(unittest.TestCase):

	def test_photoresistor_read(self):
		i2c = smbus.SMBus(BUS_ADDR)
		for _ in range(1, 10):
			i2c.write_byte(PCF8591_ADDR, AIN1)
			val = i2c.read_byte(PCF8591_ADDR)
			assert val >=0 and val <= 255
			time.sleep(0.2)

		i2c.close()


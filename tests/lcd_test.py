import sys
import os
import unittest
current = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(current)
sys.path.append(project_dir)
from lib.lcd_i2c import lcd
from time import sleep

class TestLCD(unittest.TestCase):

	def test_display(self):
		lcd_screen = lcd()
		lcd_screen.lcd_clear()
		lcd_screen.backlight(0)
		sleep(0.5)
		lcd_screen.backlight(1)
		lcd_screen.lcd_display_string_pos("test_tmp: ", 1, 1)
		lcd_screen.lcd_display_string_pos("test_hum: ", 2, 1)


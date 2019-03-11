import unittest
import datetime
from servo_control.servo_controll import Servo

'''
Test scenarios

1) current hour wrong, current minute wrong
2) current hour right, current minute wrong
3) current hour wrong, currnet minute right
4) current hour right, current minute right

'''

class TestTime(unittest.TestCase):

  def test_servo_initialization(self):
    servo = Servo()

    self.assertTrue(servo)
    self.assertEqual(servo.is_running, False)
    self.assertEqual(servo.on_hour, '00')
    self.assertEqual(servo.on_minute, '00')


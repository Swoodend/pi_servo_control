# import RPi.GPIO as GPIO
import datetime

class Servo:
  def __init__(self, on_time=datetime.time(0,0,0)): #pin_mode = GPIO.BOARD):
    self.on_time = on_time
    self.on_hour = on_time.hour
    self.on_minute = on_time.minute
    self.is_running = False

  def view_config(self):
    print(f'on_time: {self.on_time}')
    print(f'on_hour: {self.on_hour}')
    print(f'on_minute: {self.on_minute}')
    print(f'is_running: {self.is_running}')

  def set_is_running(self, status):
    self.is_running = status

  def should_run_servo(self, current_time):
    current_hour = current_time.hour
    current_minute = current_time.minute

    return current_hour == self.on_hour and current_minute == self.on_minute and not self.is_running

  def should_stop_servo(self, current_time):
    current_hour = current_time.hour
    current_minute = current_time.minute

    return current_minute > self.on_minute and self.is_running
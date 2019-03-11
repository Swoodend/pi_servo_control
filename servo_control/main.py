import datetime
import getopt
import sys
from servo_controll import Servo
from helpers import time_string_to_obj

def run(servo_on_time):
  servo = Servo(servo_on_time)
  while True:
    print('running')
    current_time = datetime.datetime.now().time()


    if (servo.should_run_servo(current_time)):
      servo.set_is_running(True)
      # servo.right()


    # set is running to False after the servo has turned right (180 deg)
    # this way 24 hours later, the servo will be ready to turn right again
    if (servo.should_stop_servo(current_time)):
      servo.set_is_running(False)
      #servo.neutral()

    

if __name__ == '__main__':

  options, remainder = getopt.getopt(sys.argv[1:], '', ['ON_TIME='])
  
  if "--ON_TIME" not in options[0] or not options[0][1]:
    sys.exit('an ON_TIME CLI argument must be passed to servo_control.py. Format should be hh:mm')

  specified_on_time = options[0][1]
  
  run(time_string_to_obj(specified_on_time))
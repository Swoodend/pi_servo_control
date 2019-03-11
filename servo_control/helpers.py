import datetime

def time_string_to_obj(date_string):
  hour, minute = date_string.split(':')
  
  if len(hour) == 2 and hour[0] == '0':
    hour = hour[1]

  hour, minute = map(lambda t: int(t), [hour, minute])
  return datetime.time(hour, minute)

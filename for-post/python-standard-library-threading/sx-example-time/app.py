import threading
import datetime

d=0
lt=datetime.datetime.now()
print(lt)
def loop():
  global d
  now = datetime.datetime.now()
  timeDelta = now - lt
  secs = timeDelta.total_seconds()
  print(secs)
  x = threading.Timer(1, loop)
  x.start()
loop()

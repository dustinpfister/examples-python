import threading
import datetime

# state
x=0
ticks=0
pps=256
secRate=0.25
lt=datetime.datetime.now()

# main app loop
def loop():
  global lt, x, ticks
  now = datetime.datetime.now()
  timeDelta = now - lt
  secs = timeDelta.total_seconds()
  x = x + pps * secs
  ticks = ticks + 1
  t = threading.Timer(secRate, loop)
  t.start()
  lt=datetime.datetime.now()
  
  a = int(x)
  b = int(ticks * (pps * secRate))
  c = abs(a - b)
  print(a, b, c)

# start loop
threading.Timer(secRate, loop).start()

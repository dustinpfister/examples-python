import threading

d=0
def loop():
  global d
  d = d + 1
  print(d)
  x = threading.Timer(1, loop)
  x.start()
loop()
import threading

def printMess():
  print('hello');

def loop(func, sec):
  def wrapper():
    loop(func, sec)
    func()
  t = threading.Timer(sec, wrapper)
  t.start()
  return t

t=loop(printMess, 1)
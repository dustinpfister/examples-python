import threading

def printMess():
  print('delay');

print('start');
t = threading.Timer(3, printMess)
t.start()
print('end');
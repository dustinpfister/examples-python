import threading

def heavy(id='none', count=100):
  i=0;
  while i < count:
    print(id, i)
    i = i + 1;

x = threading.Thread(target=heavy, args=['thread',10])
x.start()

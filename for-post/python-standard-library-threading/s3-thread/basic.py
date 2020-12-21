import threading

def heavy(id='none', count=100):
  i=0;
  while i < count:
    print(id, i)
    i = i + 1;

heavy('one', 1000)
heavy('two', 1000)

x = threading.Thread(target=heavy, args=['three',1000])
x.start()
heavy('four', 1000)

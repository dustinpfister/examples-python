import threading

a=0
def loop():
  global a
  a = a + 1
  print(a)

loop()
loop()


# x = threading.Thread(target=createLoop(), args=['three',1000])
# x.start()


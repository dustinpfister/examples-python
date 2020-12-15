import threading
from mcpi import minecraft

mc = minecraft.Minecraft.create()

def printPos():
  pos = mc.player.getPos()
  posText = 'player pos: ( ' + str(pos.x) + ', ' + str(pos.y) + ', ' + str(pos.z) + ' )'
  # print pos to python console
  print(posText);
  # print pos to minecraft chat
  mc.postToChat(posText)

def loop(func, sec):
  def wrapper():
    loop(func, sec)
    func()
  t = threading.Timer(sec, wrapper)
  t.start()
  return t

t=loop(printPos, 3)
t.cancel();
from mcpi import minecraft

mc = minecraft.Minecraft.create()

def setBeforePlayer(blockID):
  pos = mc.player.getPos()
  mc.setBlock(pos.x + 1, pos.y, pos.z, blockID)

setBeforePlayer(1);

# print pos to python console
# print(posText);
# print pos to minecraft chat
# mc.postToChat(posText)

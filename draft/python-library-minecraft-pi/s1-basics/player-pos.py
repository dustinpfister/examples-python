from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
posText = 'player pos: ( ' + str(pos.x) + ', ' + str(pos.y) + ', ' + str(pos.z) + ' )'

# print pos to python console
print(posText);
# print pos to minecraft chat
mc.postToChat(posText)
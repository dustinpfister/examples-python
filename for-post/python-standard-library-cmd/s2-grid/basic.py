import cmd


class BasicApp(cmd.Cmd):
    posX=0;
    posY=0;
    def printpos(self):
        print('pos is ', self.posX, self.posY)
    def do_home(self, line):
        self.posX = 0;
        self.posY = 0;
        self.printpos()
    def do_left(self, line):
        self.posX = self.posX + 1;
        self.printpos()
    def do_right(self, line):
        self.posX = self.posX - 1;
        self.printpos()

if __name__ == '__main__':
    BasicApp().cmdloop();
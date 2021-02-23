import cmd

class BasicApp(cmd.Cmd):
    "Basic Cmd App Example"
    i=0
    def do_set(self, line):
        "set i to line"
        self.i = int(line)
        print('i =', self.i)
    def do_step(self, line):
        "step the i prop by 1"
        self.i = self.i + 1
        print('i =', self.i)
    def default(self, line):
        print('command ' + str(line) + ' not known')
        print('use a command in help')
        self.onecmd('help')
    def emptyline(self):
        print('no command given, must give a command')
        self.onecmd('help')

if __name__ == '__main__':
    app=BasicApp()
    app.cmdloop()
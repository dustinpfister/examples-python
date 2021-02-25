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

if __name__ == '__main__':
    app=BasicApp()
    app.onecmd('set 9')
    #app.onecmd('step')
    app.cmdloop()
import cmd

class BasicApp(cmd.Cmd):
    "Basic Cmd App Example"
    i=0
    def do_thing(self, line):
        "step the i prop by 1"
        self.i = self.i + 1
        print('i =', self.i)
    def emptyline(self):
        "what to do for an empty line"
        self.onecmd('help')

if __name__ == '__main__':
    BasicApp().cmdloop()
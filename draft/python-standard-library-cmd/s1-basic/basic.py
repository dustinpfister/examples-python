import cmd

class BasicApp(cmd.Cmd):
    def do_greet(self, line):
        print('hello')

if __name__ == '__main__':
    BasicApp().cmdloop();
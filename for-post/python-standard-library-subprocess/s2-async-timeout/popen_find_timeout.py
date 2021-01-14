import subprocess

print('foo');
def findFromFolder(folder='/home'):
    r=None
    try:
        r=subprocess.Popen(['find', '.', '-name', '*.js'], cwd=folder)
    except (subprocess.TimeoutExpired):
        r='time out'
    return r

a=findFromFolder('/')
print('bar');

if(type(a).__name__ == 'str'):
    print('mess:', a)
elif(type(a).__name__ == 'CompletedProcess'):
   print(a.stdout)
else:
   print(a)

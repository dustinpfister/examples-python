import subprocess

print('foo');
def findFromFolder(f='/home', t=0.5):
    r=None
    try:
        r=subprocess.run(['find', '.',  '-name', '*.js'], cwd=f, timeout=t, capture_output=True)
    except (subprocess.TimeoutExpired):
        r='time out'
    return r


a=findFromFolder('/', 3)
print('bar');

if(type(a).__name__ == 'str'):
    print('mess:', a)
elif(type(a).__name__ == 'CompletedProcess'):
   print(a.stdout)
else:
   print(a)

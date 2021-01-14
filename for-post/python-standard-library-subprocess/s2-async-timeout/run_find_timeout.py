import subprocess

print('foo');
def findFromFolder(folder='/home', timeout=0.5):
    r=None
    try:
        r=subprocess.run(['find', '.',  '*.md'], cwd=folder, timeout=timeout, capture_output=True)
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

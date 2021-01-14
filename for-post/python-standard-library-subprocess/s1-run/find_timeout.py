import subprocess

def findFromFolder(folder='/home'):
    r=None
    try:
        r=subprocess.run(['find', '.',  '*.md'], cwd=folder, timeout=0.5, capture_output=True)
    except (subprocess.TimeoutExpired):
        r=None
    return r

a=findFromFolder('/home')
if(a == None):
    print('no result')
else:
   print(a.stdout)

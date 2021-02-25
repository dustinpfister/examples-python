import json

def getState():
    try:
        f=open('./state.json', 'r')
        j=json.loads(f)
        f.close()
        print('json load good');
        return j
    except:
        print('json load fail, started new state');
        return json.dumps({"count": 0})



state = getState()
print(state)

#j=f.read()
#print(j)
#if j == '':
#    print('okay');
#    startState = json.dumps({"count": 0})
#    f.write(startState)
#else:
#    print(f.read());
#f.write('hello world\n')
#f.close()
 
#f=open('./foo.txt', 'r')
#print(f.read())
#f.close()

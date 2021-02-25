import json

def get_state():
    try:
        f = open('./state.json', 'r')
        j = json.loads(f.read())
        f.close()
        print('json load good');
        return j
    except:
        print('json load fail, started new state');
        return {"c": 0}

def put_state(obj):
    f = open('./state.json', 'w+')
    j = json.dumps(obj)
    f.write( j )
    f.close()
    return j

state = get_state()
c = state['c']
state['c'] = int(c) + 1
put_state(state)
print(  )
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

import json, os

# resolve an absolute file path for the file
file_name = 'state.json'
file_path = os.path.abspath( os.path.join( os.getcwd(), file_name) )

def get_state():
    try:
        f = open(file_path, 'r')
        j = json.loads(f.read())
        f.close()
        print('json load good');
        return j
    except:
        print('json load fail, started new state');
        return {"c": 0}

def put_state(obj):
    f = open(file_path, 'w+')
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

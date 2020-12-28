# here is a function that does not return anything
def testN(n):
    if(n >= 10):
        if(n <= 20):
            return True

def goWith(n):
    t=testN(n)
    if(t is True):
        print('good');
    if(t is None):
        print('out of range')

goWith(5)  # 'out of range'
goWith(15) # 'good'
goWith(25) # 'out of range'
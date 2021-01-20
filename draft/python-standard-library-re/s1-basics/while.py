a='so abc is easy as abc'
b='things are not always so easy'

def find_string(string, sub_string):
    i=0
    sl = len(string)
    subl = len(sub_string)
    m=[]
    while i <= sl - subl:
        text=string[i: i + subl]
        if(text == sub_string):
            m.append({
                "start": i,
                "end": i + subl,
                "text": text
            })
        i = i + 1
    return m
        
print( find_string(a, 'abc') )
# [{'start': 3, 'end': 6, 'text': 'abc'}, {'start': 18, 'end': 21, 'text': 'abc'}]

print( find_string(b, 'abc') )
# []

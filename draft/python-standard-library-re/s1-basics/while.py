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
        
print( find_string('abc is easy as abc', 'abc') )
# [{'start': 0, 'end': 3, 'text': 'abc'}, {'start': 15, 'end': 18, 'text': 'abc'}]

print( find_string('things are not always so easy', 'abc') )
# []

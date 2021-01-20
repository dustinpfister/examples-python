def find_string(string, sub_string):
    i=0
    sl = len(string)
    subl = len(sub_string)
    while i <= sl - subl:
        print(i)
        i = i + 1
        
find_string('easy as abc', 'abc')
#find_string('not so easy', 'abc')
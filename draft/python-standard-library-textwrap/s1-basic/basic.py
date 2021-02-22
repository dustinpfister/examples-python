import textwrap


str = 'this is some text that I want to wrap to a list of lines'

lines = textwrap.wrap(str, width=20)

print(type(lines).__name__) # list

for item in lines:
    print(item)
# 'this is some text'
# 'that I want to wrap'
# 'to a list of lines'
import textwrap

str = 'use shorten to make some text fit a set width'

short = textwrap.shorten(str, width=20, placeholder='...')

print(type(short).__name__) # 'str'
print(short) # use shorten to...



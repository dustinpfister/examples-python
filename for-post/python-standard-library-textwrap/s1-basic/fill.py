import textwrap

str = 'So say I have a string like this the contains some text about something.'

filled = textwrap.fill(str, width=20)

print(type(filled).__name__) # 'str'
print(filled)
# So say I have a
# string like this the
# contains some text
# about something.

# ANother way to do this would be something liek this
filled = "\n".join( textwrap.wrap(str, width=20) )
print(filled)
# So say I have a
# string like this the
# contains some text
# about something.

## which allows for me to change what the break string is
filled = ";\r\n".join( textwrap.wrap(str, width=20) )
print(filled)
# So say I have a;
# string like this the;
# contains some text;
# about something


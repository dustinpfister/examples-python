mess='Hello'

# by default print will append a new line after each call
i=0
while i < 5:
  print(mess);
  i = i + 1;
print('')
# end can be used to change that
i=0
while i < 5:
  print(mess, end="");
  i = i + 1;
print('')

#Hello
#Hello
#Hello
#Hello
#Hello
#
#HelloHelloHelloHelloHello
#
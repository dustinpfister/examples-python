try:
    x = 5 + 'a'
except SyntaxError:
    print('looks like we have a Syntax Error.')
except TypeError:
    print('That is a type Error');

# That is a type Error
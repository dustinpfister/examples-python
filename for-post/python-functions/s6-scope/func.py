a=40
def foo():
    print(a)
def bar():
    a=5
    print(a)
foo() # 40
bar() # 5
print(a) # 40
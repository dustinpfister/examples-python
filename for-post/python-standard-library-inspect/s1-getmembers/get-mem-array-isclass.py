import inspect
import array as mod

m=inspect.getmembers(mod, inspect.isclass);
for i in m:
    print(i[0])
# ArrayType
# __loader__
# array

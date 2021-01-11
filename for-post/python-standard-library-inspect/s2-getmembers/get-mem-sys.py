import inspect
import sys as mod

m=inspect.getmembers(mod);
for i in m:
    if i[0].startswith('__') == False:
        # prop name
        print(i[0], ':')
        # prop type
        print(type(i[1]).__name__)
        print('')
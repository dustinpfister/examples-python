import inspect
import copy as mod

m=inspect.getmembers(mod, inspect.isfunction);
for n in m:
    if bool(n[0][0] != '_'):
        print(n[0])
# copy
# deepcopy
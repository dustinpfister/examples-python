import inspect
import copy as mod

m=inspect.getmembers(mod);
for n in m:
    if inspect.isfunction(n[1]) & bool(n[0][0] != '_'):
        print(n[0])
# copy
# deepcopy
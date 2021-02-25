import json
t=json.dumps(['foo', {'bar': 42}])
print(t)
# ["foo", {"bar": 42}]
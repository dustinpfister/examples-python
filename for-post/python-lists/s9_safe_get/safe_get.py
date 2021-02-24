def safe_list_get (l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default

l=[1,2,3]
print( safe_list_get(l, 0, 42) ) # 1
print( safe_list_get(l, 7, 42) ) # 42
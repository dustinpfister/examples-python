import random;

# safe list get method
def safe_list_get (l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default

# roll a single die of given sides
def roll_die(sides=6):
    return random.randint(1, sides)

# roll a set of dice
def roll_set(count=2, sides=[6, 6], defaultSides=6):
    set=[]
    i=0
    while i < count:
        s = safe_list_get(sides, i, defaultSides)
        set.append(roll_die(s))
        i = i + 1
    return set

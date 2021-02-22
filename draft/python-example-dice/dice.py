import random;

def roll_die():
    return random.randint(1, 6)

def roll_set(count=2):
    set=[]
    i=0
    while i < count:
        set.append(roll_die())
        i = i + 1;
    return set

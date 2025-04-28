a = 12

def scope(val):
    global a
    a = val
    return a

scope(10)
print(a)


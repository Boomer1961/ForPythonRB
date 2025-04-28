# Variable mutable

x = []
y = x

x.append(1)
x.append(2)
x.append(3)

print(x)
y.append(4)
print(y)
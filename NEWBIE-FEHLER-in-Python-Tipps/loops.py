x = [1,2,3,4,5]

# Bad Case
for index in range(len(x)):
    print(x[index]*3)
    
# Besser aber nicht toll
result = []

for item in x:
    new = item*2
    result.append(new)
    
print(result)    

# gewünschte Lösung
result = [item*2 for item in x]
print(result)

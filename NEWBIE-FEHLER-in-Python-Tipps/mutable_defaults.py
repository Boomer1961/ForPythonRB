def append_to_list(y,x=[]):
    x.append(y)
    return x

list_1 = append_to_list(2)
list_2 = append_to_list(5)

print(list_1)
print(list_2)
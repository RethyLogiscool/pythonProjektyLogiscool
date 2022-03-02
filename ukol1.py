pocet = 10
list = [0,1]
for i in range(pocet-2):
    list.append(list[i]+list[i+1])
print(list)
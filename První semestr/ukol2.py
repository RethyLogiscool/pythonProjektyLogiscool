radku = 4
pyramida = []
for i in range(radku):
    tempList = []
    for j in range(i+1):
        if((j==0) or (j==len(pyramida[i-1]))):
            tempList.append(1)
        else:
            tempList.append(pyramida[i-1][j]+pyramida[i-1][j-1])
    pyramida.append(tempList)

for i in pyramida:
    print(i)

"""
center = 0
for i in pyramida[-1]:
    center += str(i).count("")
center += len(pyramida[-1])+2
for line in pyramida:
    print(str(line).center(center))
"""



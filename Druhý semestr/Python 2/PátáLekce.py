import random

data = [
    ["Michael","David","Jan","Adam"],
    [14,22,45,98],
    [181,173,186,191]
]
x = 0
for i in data[2]:
    x+=i
x = x/data[2].__len__()-1

print(x)

data = [
    ["Michael",14,181],
    ["David",22,173]
]

print(data[0])

heightMap = [
    # 16 sloupců
    # 16 řádků
]

for x in range(4):
    temp = []
    for y in range(4):
        temp.append(random.randint(1,99))
    heightMap.append(temp)

for radek in heightMap:
    print(radek)

print("________")

heightMap.sort()
for radek in heightMap:
    radek.sort()


for radek in heightMap:
    print(radek)

print("\n\n\n\n\n\n")

piskvorky = [
    ["X","X",0],
    ["Y","Y","Y"],
    ["Y","X",0]
]

def genTable():
    board = []
    for x in range(3):
        temp = []
        for y in range(3):
            temp.append(0)
        board.append(temp)
    return board

piskvorky = genTable()

def displayGame(data):
    print("  1 2 3")
    print("  -----")
    x = 1
    for row in data:
        print(x, end="|")
        for box in row:
            print(box, end=" ")
        print("")
        x+=1

displayGame(piskvorky)

def checkGame(data,player): #player = "X"
    checker = [player,player,player] # ["X","X","X"]
    if(data[0] == checker):
        return True, player
    elif(data[1] == checker):
        return True, player
    elif(data[2] == checker):
        return True, player
    elif(data[0][0] == player) and (data[1][0] == player) and (data[2][0] == player):
        return True, player
    elif(data[0][1] == player) and (data[1][1] == player) and (data[2][1] == player):
        return True, player
    elif(data[0][2] == player) and (data[1][2] == player) and (data[2][2] == player):
        return True, player
    elif(data[0][0] == player) and (data[1][1] == player) and (data[2][2] == player):
        return True, player
    elif(data[0][2] == player) and (data[1][1] == player) and (data[2][0] == player):
        return True, player
    else:
        print(data)
        print(player)
        return False, "0"

def nextTurn(x,y,data,player):
    if(data[x][y] == 0):
        data[x][y] = player
        return False, data
    else:
        return True, data





win = False
player = "Y"
while(not win):
    if player == "X":
        player =  "Y"
    elif player == "Y":
        player = "X"
    displayGame(piskvorky)
    print(f"Hraje hráč {player}")
    nxt = True
    while(nxt):
        x = int(input("Zadej X: "))
        y = int(input("Zadej Y: "))
        nxt,piskvorky = nextTurn(x-1,y-1,piskvorky,player)
        if(nxt):
            print("Obsazeno, opakuj pokus")
    print("checking")
    win,winner = checkGame(piskvorky,player)
    print(win)
    if(win):
        displayGame(piskvorky)
        print(f"Vyhrál: {winner}")


    



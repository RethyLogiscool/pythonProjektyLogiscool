"""
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
    win,winner = checkGame(piskvorky,player)
    if(win):
        displayGame(piskvorky)
        print(f"Vyhrál: {winner}")

"""
"""

data = [0,0,0,X,0,0,0,0,0]

X => data[3]

data = [
    [0,0,0],
    [X,0,0],
    [0,0,0]
]

X => data[1][0]

player = "X"

...
...
...

"""

data = []

for i in range(9):
    data.append(0)

player = "Y"
win = False

while not win:
    print(f"{data[0:3]} \n {data[3:6]} \n {data[6:]}")
    print(f"Hraje hráč: {player}")
    played = False
    while not played:
        row = col = 10
        while row > 3 or row < 1:
            row = int(input("Zadej sloupec: "))
        while col > 3 or col < 1:
            col = int(input("Zadej řádek: "))
        datapos = (col-1)*3+(row-1)
        if data[datapos] == 0:
            data[datapos] = player
            played = True

    if data[0] == player and data[1] == player and data[2] == player:
        print(f"{player} vyhrál (‾)")
        win = True
    elif data[3] == player and data[4] == player and data[5] == player:
        print(f"{player} vyhrál (-)")
        win = True
    elif data[6] == player and data[7] == player and data[8] == player:
        print(f"{player} vyhrál (_)")
        win = True
    elif data[0] == player and data[3] == player and data[6] == player:
        print(f"{player} vyhrál (|--)")
        win = True
    elif data[1] == player and data[4] == player and data[7] == player:
        print(f"{player} vyhrál (-|-)")
        win = True
    elif data[2] == player and data[5] == player and data[8] == player:
        print(f"{player} vyhrál (--|)")
        win = True
    elif data[0] == player and data[4] == player and data[8] == player:
        print(f"{player} vyhrál (\)")
        win = True
    elif data[2] == player and data[4] == player and data[6] == player:
        print(f"{player} vyhrál (/)")
        win = True
    if win:
        print(f"{data[0:3]} \n {data[3:6]} \n {data[6:]}")
    
    if not win and 0 not in data:
        print("Remíza!")
    
    if not win and 0 in data:
        if player == "X":
            player = "Y"
        else:
            player = "X"
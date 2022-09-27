"""num_1 = int(input("Prvni čislo: "))
num_2 = int(input("Druhe čislo: "))
gdc = 1
for i in range(1,num_1+1):
    if num_1 % i == 0 and num_2 % i == 0:
        gdc = i
print(f"Nejvetší společný dělitel je {gdc}")

bin(42)"""

board = [".", "1", "2", "3","1","-","-","-","2","-","-","-","3","-","-","-"]
playerOneTurn = True
haveWinner = False
while not haveWinner:
    # Display board
    for i in range(0,16,4):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]} | {board[i+3]}")
    if playerOneTurn:
        print("Player 1 má hrát")
    else:
        print("Player 2 má hrát")
    # Ask position
    newPlace = False
    while not newPlace:
        row = column = 10
        while row > 3 or row < 1:
            row = int(input("Který řádek chceš?"))
        while column > 3 or column < 1:
            column = int(input("Který sloupec chceš?"))
        if board[4 * row + column] == "-":
            newPlace = True
    # Place mark
    if playerOneTurn:
        board[4 * row + column] = "O"
    else:
        board[4 * row + column] = "X"
    # Check rows
    if board[5] == board[6] and board[6] == board[7] and board[5] != "-":
        if playerOneTurn:
            print("Player 1 vyhrál")
        else:
            print("Player 2 vyhrál")
        haveWinner = True
    if board[9] == board[10] and board[10] == board[11] and board[9] != "-":
        if playerOneTurn:
            print("Player 1 vyhrál")
        else:
            print("Player 2 vyhrál")
        haveWinner = True
    if board[13] == board[14] and board[14] == board[15] and board[13] != "-":
        if playerOneTurn:
            print("Player 1 vyhrál")
        else:
            print("Player 2 vyhrál")
        haveWinner = True
    # Check columns
    if board[5] == board[9] and board[9] == board[13] and board[5] != "-":
        if playerOneTurn:
            print("Player 1 vyhrál")
        else:
            print("Player 2 vyhrál")
        haveWinner = True
    if board[6] == board[10] and board[10] == board[14] and board[6] != "-":
        if playerOneTurn:
            print("Player 1 vyhrál")
        else:
            print("Player 2 vyhrál")
        haveWinner = True
    if board[7] == board[11] and board[11] == board[15] and board[7] != "-":
        if playerOneTurn:
            print("Player 1 vyhrál")
        else:
            print("Player 2 vyhrál")
        haveWinner = True
    # Check diagonals
    if board[5] == board[10] and board[10] == board[15] and board[5] != "-":
        if playerOneTurn:
            print("Player 1 vyhrál")
        else:
            print("Player 2 vyhrál")
        haveWinner = True
    if board[7] == board[10] and board[10] == board[13] and board[7] != "-":
        if playerOneTurn:
            print("Player 1 vyhrál")
        else:
            print("Player 2 vyhrál")
        haveWinner = True
    # Tie
    if not haveWinner and "-" not in board:
        haveWinner = True
        print("Je to remíze")
    playerOneTurn = not playerOneTurn

for i in range(0,16,4):
    print(f"{board[i]} | {board[i+1]} | {board[i+2]} | {board[i+3]}")
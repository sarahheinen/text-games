board1 = [" ", " ", " "]
board2 = [" ", " ", " "]
board3 = [" ", " ", " "]

boardRows = board1, board2, board3
columnNames = {"A":1, "B":2, "C":3}
xColumnPlaces = []
xRowPlaces = []
oColumnPlaces = []
oRowPlaces = []
xPlaces = []
oPlaces = []

def win():
    endGame = False
    for row in boardRows: #check for wins across rows
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == "X":
                print("Player 1 wins!!")
                endGame = True
            if row[0] == "O":
                print("Player 2 wins!!")
                endGame = True

    for column in range(0, 3): #check for wins in columns
        if board1[column] == board2[column] and board2[column] == board3[column]:
            if board1[column] == "X":
                print("Player 1 wins!!")
                endGame = True
            if board1[column] == "O":
                print("Player 2 wins!!")
                endGame = True
    if [board1[0], board2[1]] == [board2[1], board3[2]] or [board1[2], board2[1]] == [board2[1], board3[0]]: #check for diagonal wins
        if board2[1] == "X":
            print("Player 1 wins!!")
            endGame = True
        if board2[1] == "O":
            print("Player 2 wins!!")
            endGame = True
    return endGame #returns status of game - whether or not game has ended


def TicTacToeText():
    print("Welcome to TicTacToeText! Choose where you'd like to go. \nLetters are columns and numbers are rows, so C1 is the top right corner.")
    turn = 0
    for round in range(0, 10):
        win() #checks for wins each round
        if round == 9: #checks if all spaces are filled without a win
            print("It's a tie!")
            break
        if round % 2 == 0: #check round remainder for which player's turn
            while turn == 0:
                x = input("Player 1's turn: ")
                xColumn = columnNames[x[0]] - 1 #assigns column to letter in player turn
                xRow = int(x[1]) - 1 #assigns row to number in player turn
                if boardRows[xRow][xColumn] == " ": #checks if space is empty
                    boardRows[xRow][xColumn] = "X"
                    xPlaces.append(x) #keeps track of where X's are
                    xColumnPlaces.append(x[0])
                    xRowPlaces.append(x[1])
                    turn = 1 #only changes to next player's turn if space is empty

        if round % 2 == 1: #same as X's
            while turn == 1:
                o = input("Player 2's turn: ")
                oColumn = columnNames[o[0]] - 1
                oRow = int(o[1]) - 1
                if boardRows[oRow][oColumn] == " ":
                    boardRows[oRow][oColumn] = "O"
                    oColumnPlaces.append(o[0])
                    oRowPlaces.append(o[1])
                    oPlaces.append(o)
                    turn = 0
        for row in boardRows: #prints board
            print("+", end = "")
            for square in row:
                print(square, end = "+")
            print()
        if win() == True: #ends game
            break


TicTacToeText()
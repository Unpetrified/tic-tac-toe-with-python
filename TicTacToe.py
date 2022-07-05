print("""****************************************************************************************
To play, enter the co-ordinate to move e.g to move to the top left corner, play: top-L,
to move to the center of the board play: mid-M and to move to the bottom right, play: low-R
********************************************************************************************
""")
theBoard = {"top-L":" ","top-M":" ","top-R":" ",
            "mid-L":" ","mid-M":" ","mid-R":" ",
            "low-L":" ","low-M":" ","low-R":" "
            }
def printBoard(board):
    print(board["top-L"]+"|"+board["top-M"]+"|"+board["top-R"], "       top")  
    print("-+-+-")
    print(board["mid-L"]+"|"+board["mid-M"]+"|"+board["mid-R"], "       mid")
    print("-+-+-")
    print(board["low-L"]+"|"+board["low-M"]+"|"+board["low-R"], "       low")
    print()
    print("L M R")

def run_game():
    printBoard(theBoard)
    turn = "X"
    i = 0
    while i != 9:
        move = input("Turn for "+turn+". Where would you like to move? ")
        if move not in theBoard.keys():
            print("Enter a valid space!")
            continue
        if theBoard[move] != " ":
            print("Already occupied!")
            continue
        theBoard[move] = turn
        printBoard(theBoard)
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        if theBoard["top-L"] == theBoard["top-M"] \
            and theBoard["top-R"] == theBoard["top-M"] \
            and theBoard["top-L"] != " ":
            print(theBoard["top-L"]+ " wins")
            break
        elif theBoard["top-L"] == theBoard["mid-M"] \
            and theBoard["low-R"] == theBoard["mid-M"] \
            and theBoard["top-L"] != " ":
            print(theBoard["top-L"]+ " wins")
            break
        elif theBoard["top-L"] == theBoard["mid-L"] \
            and theBoard["low-L"] == theBoard["mid-L"] \
            and theBoard["top-L"] != " ":
            print(theBoard["top-L"] + " wins")
            break
        elif theBoard["low-L"] == theBoard["mid-M"] \
            and theBoard["top-R"] == theBoard["mid-M"] \
            and theBoard["low-L"] != " ":
            print(theBoard["low-L"] + " wins")
            break
        elif theBoard["low-L"] == theBoard["low-M"] \
            and theBoard["low-L"] == theBoard["low-R"] \
            and theBoard["low-L"] != " ":
            print(theBoard["low-L"] + " wins")
            break
        elif theBoard["top-M"] == theBoard["mid-M"] \
            and theBoard["low-M"] == theBoard["mid-M"] \
            and theBoard["low-M"] != " ":
            print(theBoard["top-M"] + " wins")
            break
        elif theBoard["mid-L"] == theBoard["mid-M"] \
            and theBoard["mid-R"] == theBoard["mid-M"] \
            and theBoard["mid-L"] != " ":
            print(theBoard["mid-L"] + " wins")
            break
        elif theBoard["low-R"] == theBoard["mid-R"] \
                and theBoard["top-R"] == theBoard["low-R"] \
                and theBoard["low-R"] != " ":
            print(theBoard["low-R"] + " wins")
            break
        i += 1
    else:
        print("Stalemate")

    for key in theBoard:
        theBoard[key] = " "

check = "y"
while check == "y":
    run_game()
    check = input("Would you like to restart? y for yes, n for no ").lower()

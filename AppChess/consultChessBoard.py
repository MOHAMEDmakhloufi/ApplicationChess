def consultChessBoard (chessBoard) :
    print("\n_________________________________________________________") 
    for line in chessBoard :
        for column in line :
            if column >= 0 and abs(column)!= 500 :
                print("|  ",column, end="  ")
            elif column== 500 :
                print("|  ",column, end="")
            elif column== -500 :
                print("| ",column, end="")
            else : 
                 print("|  ",column, end=" ")   

        else :
            print("\n|______|______|______|______|______|______|______|______|")    
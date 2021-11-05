def searchPiece (chessBoard, valueOfPeice) :
    for i, line in enumerate(chessBoard) :
        if valueOfPeice in line :
            return i, line.index(valueOfPeice)
    #return 0, 0        
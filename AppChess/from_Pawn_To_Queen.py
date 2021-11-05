def pawnTOqueen(chessBoard, Fpos=(100,100), Tpos=(100, 100)) :

    pieceNumber= chessBoard[Fpos[0]][Fpos[1]] 

    if abs(pieceNumber) == 1 and Tpos[0] in {0, 7} :
        new = 9 if pieceNumber > 0 else -9
        chessBoard[Tpos[0]][Tpos[1]], chessBoard[Fpos[0]][Fpos[1]] = 9, 0
        return True
    return False    
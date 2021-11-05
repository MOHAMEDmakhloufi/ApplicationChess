from the_possibilities_of_movements.searchPiece import searchPiece

def King_And_Tour(chessBoard : list, Fpos, Tpos) :
    king = searchPiece(chessBoard, 500 if chessBoard[Fpos[0]][Fpos[1]] > 0 else -500 )
    
    if king == Fpos and (king[1] - Tpos[1]) in {-2, 2} :
     
        if king[1] - Tpos[1] == -2 :
             chessBoard [Fpos[0]][Tpos[1]-1], chessBoard [Fpos[0]][7] = chessBoard [Fpos[0]][7], 0
        elif king[1] - Tpos[1] == 2 :
             chessBoard [Fpos[0]][Tpos[1]+1], chessBoard [Fpos[0]][0] = chessBoard [Fpos[0]][0], 0
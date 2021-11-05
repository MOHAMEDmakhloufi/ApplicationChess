from the_possibilities_of_movements.possibility import possibility
def inCheck (ChessBoard, king, piece= (100, 100)) :
    if piece == (100, 100) :
        #value of piece                                                                         
        pieceNumber= ChessBoard[king[0]][king[1]] 
        for i, line in enumerate(ChessBoard) :
            for j, column in enumerate(line) :
                                                #if the piece color is different
                if ChessBoard[i][j] != 0 and (ChessBoard[i][j] * pieceNumber ) < 0 :
                    if king in possibility(ChessBoard, (i, j)) :
                        return True 
    elif king in possibility(ChessBoard, piece) :
                        return True 
                                              
    return False                

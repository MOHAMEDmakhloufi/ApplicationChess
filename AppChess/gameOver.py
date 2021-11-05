from the_possibilities_of_movements.possibiltyWithoutCheck import possibiltyWithoutCheck
from the_possibilities_of_movements.searchPiece import searchPiece
def gameOver (chessBoard, color) : 

    for i, line in enumerate(chessBoard) :
        for j, column in enumerate(line) :
                                        #if the piece color is not  different
            if chessBoard[i][j] != 0 and (chessBoard[i][j] * color ) >= 0 :
                    
                if possibiltyWithoutCheck(chessBoard, (i, j)) != [] :
                    return False                  
    return True                

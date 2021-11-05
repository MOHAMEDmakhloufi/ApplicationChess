from the_possibilities_of_movements.rook import ROOKpossibility
from the_possibilities_of_movements.bishop import BISHOPpossibility
from the_possibilities_of_movements.queen import QUEENpossibility
from the_possibilities_of_movements.knight import KNIGHTpossibility
from the_possibilities_of_movements.pawn import PAWNpossibility
from the_possibilities_of_movements.king import KINGpossibility
def possibility (chessBoard, piece) :
    pieceNumber= abs(chessBoard[piece[0]][piece[1]])
    if pieceNumber == 5 :
        return ROOKpossibility(chessBoard, piece)
    elif pieceNumber == 2 :
        return KNIGHTpossibility(chessBoard, piece)     
    elif pieceNumber == 3 :
        return BISHOPpossibility(chessBoard, piece)
    elif pieceNumber == 9 :
        return QUEENpossibility(chessBoard, piece)    
    elif pieceNumber == 1 :
        return PAWNpossibility(chessBoard, piece)
    elif pieceNumber == 500 :
        return KINGpossibility(chessBoard, piece)          
    return []    
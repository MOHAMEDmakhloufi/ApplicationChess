from the_possibilities_of_movements.rook import *
from the_possibilities_of_movements.bishop import *

def QUEENpossibility(chessBoard, piece) :
    return ROOKpossibility(chessBoard, piece) + BISHOPpossibility(chessBoard, piece) 

    